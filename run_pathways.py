import openai
import re
import os
import time
import datetime
import json
import pandas as pd
import argparse
from pathways_expert import *



api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
    print('Find OPENAI_API_KEY', api_key)
else:
    print("Warning: OPENAI_API_KEY is not set")
    

# This function will return error type
def call_chat_gpt(messages, model='gpt-3.5-turbo', stop=None, temperature=0.,max_tokens=128, n=1):
    wait = 1
    while True:
        try:
            ans = openai.ChatCompletion.create(
                model=model,
                max_tokens=max_tokens,
                stop=stop,
                messages=messages,
                temperature=temperature,
                n=n,
            )
            return ans
        except (openai.error.ServiceUnavailableError, openai.error.RateLimitError, openai.error.APIError) as e:
            time.sleep(min(wait, 60))
            wait *= 2


def chatgpt(messages, model="gpt-3.5-turbo", temperature=0.7, max_tokens=5500, stop=None) -> list:
    outputs = []
    res = call_chat_gpt(messages=messages, model=model, temperature=temperature, max_tokens=max_tokens, n=1, stop=stop)
    outputs.extend([choice["message"]["content"] for choice in res["choices"]])
    return outputs



def run(args):
    data_path = os.path.join(args.task_file_path, '{}_test.csv'.format(args.task))
    data = pd.read_csv(data_path, sep=',', names=['Q','(a)','(b)','(c)','(d)','Ans'])
    print('data size:',len(data))
    task_end_index = min(args.task_end_index, len(data))
    log_file = f'logs/{args.task}/{args.backend}_{args.temperature}_{args.prompt_type}_{args.context}_sample_{args.max_tokens}_start{args.task_start_index}_end{task_end_index}_{datetime.datetime.now()}.json'
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logs = []

    for i in range(args.task_start_index, task_end_index):
        print(args.prompt_type, args.task)
        print('sample:',i, data.iloc[i,:])
        sample = data.iloc[i,:]
        question = sample['Q']
        choices = [str(item).strip('"') for item in sample[['(a)','(b)','(c)','(d)']]]
        idx_map = ['(a)','(b)','(c)','(d)']
        choices_format = 'Answer Choices:\n'
        for j,ch in enumerate(choices):
            choices_format += idx_map[j]+' '+ch+'\n'
        answer = sample['Ans']


        if args.prompt_type == 'multi_agent'  and args.task == 'college_physics':
            prompt = '\n'.join([question+'?', choices_format.strip()]) # rewording
            while True: # in case of any API errors
                try:
                    phy_msg=[
                    {"role": "system", "content": sys_prompt_sum},
                    {"role": "user", "content": phy_prompt_sum.format(problem=task_desc.format(input=prompt))}]
                    phy_response = chatgpt(phy_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    math_msg=[
                    {"role": "system", "content": sys_prompt_sum},
                    {"role": "user", "content": math_prompt_sum.format(problem=task_desc.format(input=prompt), phy_response=phy_response)}]
                    math_response = chatgpt(math_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sum_msg=[
                    {"role": "system", "content": sys_prompt_sum},
                    {"role": "user", "content":sum_prompt.format(problem=task_desc.format(input=prompt), phy_response=phy_response, math_response=math_response)}]
                    sum_response = chatgpt(sum_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                except:
                    print('error')
                    continue
                break
            info = {'idx': i, 'input':','.join([str(item[1]) for item in sample.items()]), 'phy_response':phy_response, 'math_response':math_response, 'sum_response':sum_response}
            logs.append(info)


        elif args.prompt_type == 'pathways' and args.task == 'college_physics':
            prompt = '\n'.join([question+'?', choices_format.strip()])
            max_trials = 2
            while True: # in case of any API errors
                if not max_trials:
                    break
                try:
                    sub_msg=[
                    {"role": "system", "content": college_phy_pathways_prompt},
                    {"role": "user", "content": college_phy_sol_prompt1.format(cot_examples_phy = cot_examples_phy,task=task_desc.format(input=prompt))}]
                    sub_response = chatgpt(sub_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sol_msg=[
                    {"role": "system", "content": college_phy_pathways_prompt},
                    {"role": "user", "content": college_phy_sol_prompt2.format(cot_examples_math = cot_examples_math,task=task_desc.format(input=prompt))}]
                    sol_response = chatgpt(sol_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sum_msg=[
                    {"role": "system", "content": college_phy_pathways_prompt},
                    {"role": "user", "content": college_phy_pathway_sum_prompt.format(task=task_desc.format(input=prompt), college_phy_sol_prompt1=sub_response, college_phy_sol_prompt2=sol_response)}]
                    sum_response = chatgpt(sum_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    max_trials -= 1
                    if not find_answer_letter(sum_response):
                        continue
                except:
                    print('error')
                    continue
                break
            info = {'idx': i, 'input':','.join([str(item[1]) for item in sample.items()]), 'phy_response':sub_response, 'math_response':sol_response, 'sum_response':sum_response}
            logs.append(info)

        elif args.prompt_type == 'multi_agent' and args.task == 'moral_scenarios':
            question = sample['Q'].strip('"').split('?')[0].strip()
            scenarios = sample['Q'].strip('"').split('?')[1].strip()
            scenarios = scenarios.split('Scenario 2')
            scenarios_format = scenarios[0].strip().replace('|', '—') + '\n' + 'Scenario 2' + scenarios[1].replace('|', '—')
            prompt = '\n'.join([question+'?', scenarios_format, ans_chs.strip()]) # rewording
            while True: # in case of any API errors
                try:
                    sub_msg1=[
                    {"role": "system", "content": lgd_prompt},
                    {"role": "user", "content": sub_prompt1.format(task=task_desc.format(input=prompt))}]
                    sub_response1 = chatgpt(sub_msg1, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sol_msg1=[
                    {"role": "system", "content": lgd_prompt},
                    {"role": "user", "content": sol_prompt1.format(task=task_desc.format(input=prompt), sub_response1=sub_response1)}]
                    sol_response1 = chatgpt(sol_msg1, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sub_msg2=[
                    {"role": "system", "content": lgd_prompt},
                    {"role": "user", "content": sub_prompt2.format(task=task_desc.format(input=prompt), sub_response1=sub_response1, sol_response1=sol_response1)}]
                    sub_response2 = chatgpt(sub_msg2, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sol_msg2=[
                    {"role": "system", "content": lgd_prompt},
                    {"role": "user", "content": sol_prompt2.format(task=task_desc.format(input=prompt),  sub_response2=sub_response2)}]
                    sol_response2 = chatgpt(sol_msg2, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sum_msg=[
                    {"role": "system", "content": lgd_prompt},
                    {"role": "user", "content": sum_prompt_lgd.format(task=task_desc.format(input=prompt), sub_response2=sub_response2, sol_response2=sol_response2)}]
                    sum_response = chatgpt(sum_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                except:
                    print('error')
                    continue
                break
            info = {'idx': i, 'input':','.join([str(item[1]) for item in sample.items()]), 'sub_response1':sub_response1, 'sol_response1':sol_response1,  'sub_response2':sub_response2, 'sol_response2':sol_response2,'sum_response':sum_response}
            logs.append(info)

        elif args.prompt_type == 'pathways' and args.task == 'moral_scenarios':
            question = sample['Q'].strip('"').split('?')[0].strip()
            scenarios = sample['Q'].strip('"').split('?')[1].strip()
            scenarios = scenarios.split('Scenario 2')
            scenarios_format = scenarios[0].strip().replace('|', '—') + '\n' + 'Scenario 2' + scenarios[1].replace('|', '—')
            prompt = '\n'.join([question+'?', scenarios_format, ans_chs.strip()]) # rewording
            while True: # in case of any API errors
                try:
                    sol21_msg=[
                    {"role": "system", "content": pathways_prompt_multi2},
                    {"role": "user", "content": sol_prompt21.format(cot_examples = task_examples_cot,task=task_desc.format(input=prompt))}]
                    sol21_response = chatgpt(sol21_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    
                    sol22_msg=[
                    {"role": "system", "content": pathways_prompt_multi2},
                    {"role": "user", "content": sol_prompt22.format(thought_examples = task_examples_thought,task=task_desc.format(input=prompt))}]
                    sol22_response = chatgpt(sol22_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]

                    sol23_msg=[
                    {"role": "system", "content": pathways_prompt_multi2},
                    {"role": "user", "content": sol_prompt23.format(sol_response21=sol21_response,cot_examples = task_examples_cot,task=task_desc.format(input=prompt))}]
                    sol23_response = chatgpt(sol23_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    sol24_msg=[
                    {"role": "system", "content": pathways_prompt_multi2},
                    {"role": "user", "content": sol_prompt24.format(sol_response22=sol22_response, thought_examples = task_examples_thought,task=task_desc.format(input=prompt))}]
                    sol24_response = chatgpt(sol24_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]

                    sum_msg=[
                    {"role": "system", "content": pathways_prompt_multi2},
                    {"role": "user", "content": sum_prompt_pathway2.format(example=task_examples_cot,task=task_desc.format(input=prompt), sol_response23=sol23_response, sol_response24=sol24_response)}]
                    sum_response = chatgpt(sum_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
                    if not find_answer_letter(sum_response):
                        continue
                except:
                    print('error')
                    continue
                break

            info = {'idx': i, 'input':','.join([str(item[1]) for item in sample.items()]), 'sol21_response':sol21_response, 'sol22_response':sol22_response, 'sol23_response': sol23_response, 'sol24_response':sol24_response,'sum_response':sum_response}
            logs.append(info)

        else:
            if args.task == 'college_physics':
                prompt = '\n'.join([question+'?', choices_format.strip()]) 
            elif args.task == 'moral_scenarios':
                question = sample['Q'].strip('"').split('?')[0].strip()
                scenarios = sample['Q'].strip('"').split('?')[1].strip()
                scenarios = scenarios.split('Scenario 2')
                scenarios_format = scenarios[0].strip().replace('|', '—') + '\n' + 'Scenario 2' + scenarios[1].replace('|', '—')
                prompt = '\n'.join([question+'?', scenarios_format, ans_chs.strip()]) # rewording

            if args.prompt_type == 'std' and args.context == 'zero':
                sub_msg=[
                {"role": "user", "content": std_prompt_0shot.format(input=prompt)}]
            elif args.prompt_type == 'cot' and args.context == 'zero':
                sub_msg=[
                {"role": "user", "content": cot_prompt_0shot.format(input=prompt)}]

            elif args.prompt_type == 'std' and args.context == 'few' and args.task == 'college_physics':
                sub_msg=[
                {"role": "user", "content": college_phy_std_prompt_5shot.format(input=prompt)}]

            elif args.prompt_type == 'cot' and args.context == 'few' and args.task == 'college_physics':
                sub_msg=[
                {"role": "user", "content": college_phy_cot_prompt_5shot.format(input=prompt)}]

            elif args.prompt_type == 'std' and args.context == 'few' and args.task == 'moral_scenarios':
                sub_msg=[
                {"role": "user", "content": moral_std_prompt_5shot.format(input=prompt)}]

            elif args.prompt_type == 'cot' and args.context == 'few' and args.task == 'moral_scenarios':
                sub_msg=[
                {"role": "user", "content": moral_cot_prompt_5shot.format(input=prompt)}]
            response = chatgpt(sub_msg, model=args.backend, temperature=args.temperature, max_tokens=args.max_tokens)[0]
            info = {'idx': i, 'input':','.join([str(item[1]) for item in sample.items()]), 'response':response}
            logs.append(info)
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=4)



def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, choices=['gpt-3.5-turbo-0613', 'gpt-3.5-turbo'], default='gpt-3.5-turbo-0613')
    args.add_argument('--temperature', type=float, default=0.) 
    args.add_argument('--task', type=str, choices=['moral_scenarios', 'college_physics'], default='moral_scenarios')
    args.add_argument('--task_file_path', type=str, default='/home/ubuntu/autoprompt/CoMM/data/mmlu/test/')
    args.add_argument('--task_start_index', type=int, default=0)
    args.add_argument('--task_end_index', type=int, default=1000) 
    args.add_argument('--max_tokens', type=int, default=600) 
    args.add_argument('--prompt_type', type=str, choices=['std', 'cot', 'pathways', 'multi_agent'], default='pathways')  
    args.add_argument('--context', type=str, choices=['zero', 'few'], default='zero')
    args.add_argument('--n_generate_sample', type=int, default=1)
    args = args.parse_args()
    return args


def find_answer_letter(input_string):
    pattern = re.compile(r'\(a\)|\(b\)|\(c\)|\(d\)')
    match = re.findall(pattern, input_string)
    if match:
        answer_letter = match[-1]
        return answer_letter.strip('(').strip(')').upper()
    else:
        return None 

def evaluate():
    file_name = ''
    source_name = ''
    gold_answers = pd.read_csv(source_name, sep=',', names=['Q','(a)','(b)','(c)','(d)','Ans'])['Ans']
    results = json.load(open(file_name, 'r'))
    ans = []
    for exmpl in results:
        try:
            sum_response = exmpl['response']
        except:
            sum_response = exmpl['sum_response']
        answer = find_answer_letter(sum_response) 
        ans.append(answer)
    assert len(ans) ==  len(gold_answers)
    # rigorous evaluation
    acc = sum([ans[i] == gold_answers[i] for i in range(len(gold_answers))])/len(gold_answers)
    print('Test Acc:', acc)




if __name__ == '__main__':
    # For prediction.
    args = parse_args()   
    print(args)
    start_time = datetime.datetime.now()
    run(args)
    end_time = datetime.datetime.now()
    print('time cost:', round((end_time-start_time).total_seconds()/60,2), ' mins')

    # # For evaluation.
    # evaluate()

