college_phy_pathways_prompt = '''You're on a team targeting collective task resolution, with three key roles:

1. 'The Physicist'

    Role Definition: You are a physicist with a specialization in the field of college-level physics. Your vast knowledge covers multiple aspects of physics including classical mechanics, thermodynamics, electromagnetism, quantum mechanics, and statistical physics. You understand these topics in depth and have the ability to explain them in a way that is easily comprehensible to those less familiar with them.

    Responsibility: Solve the given task by following the provided demonstration samples with reasoning paths; Use physics principles to interpret and solve cross-disciplinary problems collaboratively; Work with the mathematician to develop and validate mathematical models of physical phenomena; Communicate findings effectively to promote team understanding and decision making.

    Principles: Emulating the reasoning paths in the demonstration samples; Advocate for empirical, systematic, and data-driven approaches to problem-solving; Cultivate an environment of curiosity, innovation, and continuous learning; Uphold ethical scientific practices and respect for diverse viewpoints.

2. 'The Mathematician'

    Role Definition: You are a mathematician, specializing in the broad and complex field of mathematics at the college level. Your expertise ranges from pure mathematical theory, including algebra, calculus, geometry, number theory, and statistics, to applied mathematics such as optimization and probability theory. You have an innate ability to abstract and generalize problems, solving them with elegance and precision. You excel at creating mathematical models that represent real-world situations and can interpret the implications of those models. You are not only well-versed in complex equations and proofs, but also experienced in conveying these concepts to others through teaching.

    Responsibilities: Solve the given task by following the provided demonstration samples with reasoning paths; Apply mathematical reasoning to analyze and address complex, cross-disciplinary problems; Collaborate with the physicist to refine mathematical models and validate their conclusions; Convey mathematical insights in a clear manner to facilitate team decision making.

    Principles: Mimicking the reasoning paths in the demonstration samples; Foster a culture of analytical thinking and evidence-based decisions; Encourage an atmosphere of curiosity, innovation, and continuous learning; Maintain high mathematical integrity and respect for varying perspectives.

3. 'The Final Answer Synthesizer'

    Role Definition: You are the Final Answer Synthesizer, an integrative role in the team responsible for coalescing the insights provided by the experts. With a clear understanding of the different disciplines, you effectively distill the responses from the physicist and the mathematician into a coherent, final solution. Your role involves keenly interpreting expert input, synthesizing various problem-solving approaches, and presenting a clear, well-rounded answer that incorporates the collective wisdom of the team. 

    Responsibility: Summarize the solutions; Give a final answer.

    Principles: Make sure to give a specific answer to the given task; Ensure delivery of a precise response to the task at hand.'''

college_phy_sol_prompt1='''Your role is the 'The Physicist'. Here are some reasoning examples of solving the target task as a physicist:
"{cot_examples_phy}"
Here is the task: 
"{task}"
Please provide your reasoning of solving the task.'''

college_phy_sol_prompt2='''Your role is the 'The Mathematician'. Here are some reasoning examples of solving the target task as a mathematician:
"{cot_examples_math}"
Here is the task: 
"{task}"
Please provide your reasoning of solving the task.'''


college_phy_pathway_sum_prompt='''Your role is 'The Final Answer Synthesizer'.
For the task: 
"{task}" 
Here is the reasoning path from the 'The Physicist': 
"{college_phy_sol_prompt1}"
Here is the reasoning path from the 'The Mathematician': 
"{college_phy_sol_prompt2}"
Please give the final choice answer by summarizing both of their reasoning paths.'''

sys_prompt_sum = '''You are part of a team with multiple experts from different disciplines. Your team aims to solve a given cross-discipline problem collectively.

The team is composed of three experts:

1. The Physicist

    Role Definition: You are a physicist with a specialization in the field of college-level physics. Your vast knowledge covers multiple aspects of physics including classical mechanics, thermodynamics, electromagnetism, quantum mechanics, and statistical physics. You understand these topics in depth and have the ability to explain them in a way that is easily comprehensible to those less familiar with them.

    Responsibility: Use physics principles to interpret and solve cross-disciplinary problems collaboratively; Work with the mathematician to develop and validate mathematical models of physical phenomena; Communicate findings effectively to promote team understanding and decision making.

    Principles: Advocate for empirical, systematic, and data-driven approaches to problem-solving; Cultivate an environment of curiosity, innovation, and continuous learning; Uphold ethical scientific practices and respect for diverse viewpoints.

2. The Mathematician

    Role Definition: You are a mathematician, specializing in the broad and complex field of mathematics at the college level. Your expertise ranges from pure mathematical theory, including algebra, calculus, geometry, number theory, and statistics, to applied mathematics such as optimization and probability theory. You have an innate ability to abstract and generalize problems, solving them with elegance and precision. You excel at creating mathematical models that represent real-world situations and can interpret the implications of those models. You are not only well-versed in complex equations and proofs, but also experienced in conveying these concepts to others through teaching.

    Responsibilities: Apply mathematical reasoning to analyze and address complex, cross-disciplinary problems; Collaborate with the physicist to refine mathematical models and validate their conclusions; Convey mathematical insights in a clear manner to facilitate team decision making.

    Principles: Foster a culture of analytical thinking and evidence-based decisions; Encourage an atmosphere of curiosity, innovation, and continuous learning; Maintain high mathematical integrity and respect for varying perspectives.

3. The 'Final Answer Synthesizer'

    Role Definition: You are the Final Answer Synthesizer, an integrative role in the team responsible for coalescing the insights provided by the experts. With a clear understanding of the different disciplines, you effectively distill the responses from the physicist and the mathematician into a coherent, final solution. Your role involves keenly interpreting expert input, synthesizing various problem-solving approaches, and presenting a clear, well-rounded answer that incorporates the collective wisdom of the team. 
    Responsibility: summarize the solutions; give a final answer.
    Principles: make sure to give a specific answer to the given task.'''
    

phy_prompt_sum = '''Your role is the physicist. 
Here is the given problem:
"{problem}"
Please give your opinion on how to solve the problem.'''


math_prompt_sum = '''Your role is the mathematician. 
Here is the given problem:
"{problem}"
Here is the response from the physicist:
"{phy_response}"
Please give your opinion on how to solve the problem in consideration of the response from the physicist.'''

sum_prompt = '''Your role is the 'Final Answer Synthesizer'. 
Here is the given problem:
"{problem}"
Here is the response from the physicist:
"{phy_response}"
Here is the response from the mathematician:
"{math_response}"
Please give the final answer.'''





pathways_prompt_multi2 = '''You're on a team targeting collective task resolution, with three key roles:

1. 'Chain of Thought Solver'
Duty: Solve the task by following the provided chain-of-thought reasoning path.
Guideline: Ensure step-by-step task completion, emulating the chain-of-thought examples.

2. 'Thought Experiment Solver'
Duty: Solve the task utilizing the example thought experiment reasoning path.
Guideline: Ensure step-by-step task completion, mimicking the thought experiment examples.

3. 'Final Answer Synthesizer'
Duty: Compile the solutions; provide the final answer.
Guideline: Ensure delivery of a precise response to the task at hand.

The task will be sequentially assigned to the two task solver twice for refinement, with the 'Final Answer Synthesizer' giving the final answer.'''

sol_prompt21='''Your role is the 'Chain of Thought Solver'. Here are some chain-of-thought reasoning examples of solving the target task:
"{cot_examples}"
Here is the task: 
"{task}"
Please provide your chain-of-thought of solving the task.'''

sol_prompt22='''Your role is the 'Thought Experiment Solver'. Here are some thought experiment examples of solving the target task:
"{thought_examples}"
Here is the task: 
"{task}"
Please provide your thought experiment of solving the task.'''


sol_prompt23='''Your role is the 'Chain of Thought Solver'. Here are some chain-of-thought reasoning examples of solving the target task:
"{cot_examples}"
Here is the task: 
"{task}"
Here is your last response:
"{sol_response21}"
Please refine your chain-of-thought of solving the task.'''

sol_prompt24='''Your role is the 'Thought Experiment Solver'. Here are some thought experiment examples of solving the target task:
"{thought_examples}"
Here is the task: 
"{task}"
Here is your last response:
"{sol_response22}"
Please refine your thought experiment of solving the task.'''


sum_prompt_pathway2='''Your role is the 'Final Answer Synthesizer'.
For the task: 
"{task}" 
Here is the reasoning path from the 'Chain of Thought Solver': 
"{sol_response23}"
Here is the reasoning path from the 'Thought Experiment Solver': 
"{sol_response24}"
Please give the final answer by summarizing both of their thoughts.'''

ans_chs = '''
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong'''


lgd_prompt = '''You are part of a team that aims to solve a given task collectively.

The team is composed of three specialized roles:

1. The 'Task Breakdown Specialist'
   Responsibility: decompose the main task into smaller, more manageable pieces.
   Principles: make sure each sub-task is key to solve the whole task; keep a maximum of five sub-tasks;

2. The 'Sub-task Resolver'
   Responsibility: solve each of the sub-task proposed by the 'Task Breakdown Specialist'.
   Principles: give detailed solutions for each sub-task.

3. The 'Final Answer Synthesizer'
   Responsibility: summarize the solutions; give a final answer.
   Principles: make sure to give a specific answer to the given task.

The 'Task Breakdown Specialist' and the 'Sub-task Resolver' will discuss two turns to refine their responses.'''

sub_prompt1='''Your role is the 'Task Breakdown Specialist'.
Here is the task: 
"{task}"
Please decompose the task.'''

sol_prompt1='''Your role is the 'Sub-task Resolver'.
For the task: 
"{task}" 
Here is the response from the 'Task Breakdown Specialist': 
"{sub_response1}"
Please solve each of the sub-task.'''


sub_prompt2='''Now is the second turn discussion. Your role is the 'Task Breakdown Specialist'.
For the task: 
"{task}"
Here is your last response:
"{sub_response1}"
Here is the response from the 'Sub-task Resolver':
"{sol_response1}"
Please refine your task decomposition.'''

sol_prompt2='''Now is the second turn discussion. Your role is the 'Sub-task Resolver'.
For the task: 
"{task}" 
Here is the refined response from the 'Task Breakdown Specialist': 
"{sub_response2}"
Please solve each of the sub-task.'''


sum_prompt_lgd='''Your role is the 'Final Answer Synthesizer'.
For the task: 
"{task}" 
Here is the refined response from the 'Task Breakdown Specialist': `
"{sub_response2}"
Here is the refined response from the 'Sub-task Resolver':
"{sol_response2}"
Please give the final answer.'''

std_prompt_0shot = '''
Question: {input}
Answer:'''

cot_prompt_0shot = '''  
Question: {input}
Answer: Let's think step by step.'''


task_desc = '''The following are multiple choice questions (with answers) about college physics. Choose the correct answer from the choices.
Question: {input}
Answer:
'''



cot_examples_phy = '''The following are multiple choice questions (with answers) about college physics.

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: Let's think step by step. In a refracting telescope, if both lenses are converging, the focus of both lenses must be between the two lenses, and thus the focal lengths of the two lenses must add up to their separation. Since the focal length of one lens is 20 cm, the focal length of the other must be 80 cm. The magnification is the ratio of these two focal lengths, or 4. The answer is (a).

Question: The muon decays with a characteristic lifetime of about 10^-6 second into an electron, a muon neutrino, and an electron antineutrino. The muon is forbidden from decaying into an electron and just a single neutrino by the law of conservation of:
(a) charge 
(b) mass 
(c) energy and momentum 
(d) lepton number
Answer: Let's think step by step. Lepton number must be conserved, meaning the total number of leptons minus the number of antileptons. If a muon decays into an electron and a single neutrino, the total lepton number would go from one to two, violating lepton number conservation. The answer is (d).

Question: One end of a Nichrome wire of length 2L and cross-sectional area A is attached to an end of another Nichrome wire of length L and cross- sectional area 2A. If the free end of the longer wire is at an electric potential of 8.0 volts, and the free end of the shorter wire is at an electric potential of 1.0 volt, the potential at the junction of the two wires is most nearly equal to:
(a) 2.4 V 
(b) 3.3 V 
(c) 4.5 V 
(d) 5.7 V
Answer: Let's think step by step. This is a simple voltage divider problem, where the longer wire has a resistance four times that of the shorter end. So the voltage divider ratio is 1 / 5, meaning that the potential in the middle is 1.0 V + (8.0 V - 1.0 V) * 1/5 = 2.4 V. The answer is (a).

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: Let's think step by step. In a refracting telescope, if both lenses are converging, the focus of both lenses must be between the two lenses, and thus the focal lengths of the two lenses must add up to their separation. Since the focal length of one lens is 20 cm, the focal length of the other must be 80 cm. The magnification is the ratio of these two focal lengths, or 4. The answer is (a).

Question: For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas?
(a) Constant temperature 
(b) Constant volume 
(c) Constant pressure 
(d) Adiabatic
Answer: Let's think step by step. Heat added to the gas can go into the gases internal energy or work done against an external force. However, if the volume of the gas container is constant, no work will be done (since work is pressure times change in volume). So, at constant volume, all of the heat goes into the internal energy. The answer is (b).'''

cot_examples_math = '''The following are multiple choice questions (with answers) about college physics.

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: Let's solve the problem step by step. 
Define the eye-piece focal lenght as fe = 20 cm.
The objective lens defined as fo = total length - fe = 100 cm - 20 cm = 80 cm.
According to the formula for angular magnification, the the angular magnification of the telescope = fo/fe = 4.
So the answer is (a).

Question: The muon decays with a characteristic lifetime of about 10^-6 second into an electron, a muon neutrino, and an electron antineutrino. The muon is forbidden from decaying into an electron and just a single neutrino by the law of conservation of:
(a) charge 
(b) mass 
(c) energy and momentum 
(d) lepton number
Answer: Let's solve the problem step by step.
Define μ, e− and ν as the muon, electron and a single neutrino. 
If  μ → e− + ν
(a) FALSE. Conservation of charge: − 1 → − 1 + 0 is not violated.
(b) FALSE. Conservation of mass cannot be violated in any decay/interactions.
(c) FALSE. Conservation of energy and momentum cannot be violated in any decay/interactions.
(d) TRUE. Lepton Numbers: 1 → 1 + 1 is violated.
So the answer is (d).

Question: One end of a Nichrome wire of length 2L and cross-sectional area A is attached to an end of another Nichrome wire of length L and cross- sectional area 2A. If the free end of the longer wire is at an electric potential of 8.0 volts, and the free end of the shorter wire is at an electric potential of 1.0 volt, the potential at the junction of the two wires is most nearly equal to:
(a) 2.4 V 
(b) 3.3 V 
(c) 4.5 V 
(d) 5.7 V
Answer: Let's solve the problem step by step.
First, define the length of the longer wire as L_long = 2L and its cross-sectional area as A_long = A.
Then, define the length of the shorter wire as L_short = L and its cross-sectional area as A_short = 2A.
From these definitions, the ratio of the resistance from the long wire to the short wire is R_long/R_short = (2L/A)/(L/2A) = 4, so R_long = 4*R_short.
Next, the total resistance is R_total= 5*R_short.
We also know the electric potential at the longer wire's end as V_long_end = 8.0 V, and at the shorter wire's end as V_short_end = 1.0 V. Thus, the potential difference between the two ends is V_diff = V_long - V_short = 8.0 V - 1.0 V = 7.0 V.
According to the law that voltage is directly proportional to resistance, the voltage on the shorter wire, V_short = (V_diff/R_total)*R_short = (7/(5R_short))*R_short = 1.4 V.
Then, the potential in the middle is V_middle = V_short_end + V_short = 1 V + 1.4 V = 2.4 V.
So the answer is (a).       

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: Let's solve the problem step by step. 
Define the eye-piece focal lenght as fe = 20 cm.
The objective lens defined as fo = total length - fe = 100 cm - 20 cm = 80 cm.
According to the formula for angular magnification, the the angular magnification of the telescope = fo/fe = 4.
So the answer is (a).

Question: For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas?
(a) Constant temperature 
(b) Constant volume 
(c) Constant pressure 
(d) Adiabatic
Answer: Let's solve the problem step by step.
Based on the first law of thermodynamics, ΔU = Q - W, where ΔU is the change in the internal energy of the system, Q is the heat added to the system, and W is the work done by the system.
(a) Constant temperature (isothermal process): For an isothermal process, the change in internal energy (ΔU) is zero because the temperature remains constant, and internal energy of an ideal gas is a function of its temperature. So even if heat is added, it's all converted to work done by the system, and none increases the internal energy.
(b) Constant volume (isochoric process): In an isochoric process, the volume remains constant which means no work is done by the system (Work done, W = PΔV, and here ΔV = 0). So according to the first law of thermodynamics (ΔU = Q - W), all the heat added to the system (Q) will go to increasing the internal energy (ΔU), since W=0. Thus, the heat added to the gas is equal to the increase in its internal energy.
(c) Constant pressure (isobaric process): In an isobaric process, both heat is added to the system and work is done by the system (as the volume can change at constant pressure). Therefore, the increase in internal energy is not equal to the total heat added because some of the heat energy goes into doing work.
(d) Adiabatic process: In an adiabatic process, there is no heat exchange between the system and its surroundings (Q=0). Thus, the increase in internal energy is not due to the addition of heat, but is due to work done on the system.
So the answer is (b).'''


task_examples_cot = '''Choose the correct answer from the choices.

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I really loved my newborn baby boy.
Scenario 2 — The new girl is embarrassed to live in a trailer park, so I invite the class to her house. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s think step by step. In Scenario 1, it is healthy to love my newborn baby boy, so it is not wrong. In Scenario 2, when I invite the class to the new girl’s house, it will embarrass the girl in front of the whole class, so it is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).


Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I asked for a cigarette from the guy outside the store. 
Scenario 2 — When the security guard left his post, I pocketed a rare coin. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s think step by step. In Scenario 1, if I ask for a cigarette, the guy might give one to me out of politeness. I may thank him and we may chat a bit while smoking. So it is not wrong. In Scenario 2, if I pocketed a rare coin, it is theft, it may also get the security guard into trouble. Therefore it is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).


Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I bought an old pick-up truck for work. 
Scenario 2 — I looked up at the gorgeous waterfall and threw a rock at it. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s think step by step. In Scenario 1, if I bought an old pick-up truck for work, I can drive it to work. Therefore it is not wrong. In Scenario 2, if I looked up at a gorgeous waterfall and threw a rock, the rock would fall into the waterfall and hopefully nothing would be hit or hurt. Therefore it is not wrong either. In conclusion, Scenario 1 is not wrong and Scenario 2 is not wrong. So the answer is (d).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — During the house’s demolition, I pushed him into a wall. 
Scenario 2 — When I choose a babysitter for my twin nieces, I don’t care about her racial background. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s think step by step. In Scenario 1, if I push him into a wall, he may get hurt. Especially given this is during the house’s demolition. It can be an extra dangerous environment. So it is wrong. In Scenario 2, if I don’t care about the racial background of my babysitter, I can focus on choosing the best candidate for the job. So it is not wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is not wrong. So the answer is (b).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I took his wallet after he harassed me at the bar. 
Scenario 2 — I made love to my newborn baby boy. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s think step by step. In Scenario 1, if I took his wallet, I took someone else’s private property. Even though he harassed me, it is not right to take someone’s wallet. So it is wrong. In Scenario 2, if I make love to my new born baby boy, it would be incredibly unethical and traumatizing for the child. So it is wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is wrong. So the answer is (a).
'''


task_examples_thought = '''Choose the correct answer from the choices.

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I really loved my newborn baby boy.
Scenario 2 — The new girl is embarrassed to live in a trailer park, so I invite the class to her house. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s do a thought experiment. For each scenario, did I do something morally wrong? In Scenario 1, the action is to love my newborn baby boy. If I do so, I will take care of the baby really well. Alternatively, if I don’t do the action, I will ignore the boy, and the boy will suffer. The first outcome more morally correct. Scenario 1 is not wrong. In Scenario 2, the action is to invite the class to the new girl’s house who lives in a trailer park. It is not polite to invite people to someone else’s house. In addition, my action is not considerate of the girl’s embarrassment of being poor. Alternatively, if I don’t do the action, my action will not result in harm. I can be friendly and invite the entire class to my house. The first outcome is morally worse than the second as a result of my action. Scenario 2 is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I asked for a cigarette from the guy outside the store. 
Scenario 2 — When the security guard left his post, I pocketed a rare coin. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s do a thought experiment. For each scenario, did I do something morally wrong? In Scenario 1, the action is to ask for a cigarette from the guy. As long as I am considerate of other people’s feelings, the guy can decide to give or not to me the cigarette. Alternatively, if I didn’t do the action, nothing bad would happen. A third possibility is if I asked rudely, or got mad if the guy refused. The first outcome is not morally worse than other possibilities of my action. Scenario 1 is not wrong. In Scenario 2, the action is to pocket a rare coin when the guard is away. If I do so, it is theft, and it may also get the security guard into trouble. Alternatively, if I don’t do so, nothing will be lost. I would not commit any theft. The first outcome is morally worse than the second as a result of my action. Scenario 2 is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I bought an old pick-up truck for work. 
Scenario 2 — I looked up at the gorgeous waterfall and threw a rock at it. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s do a thought experiment. For each scenario, did I do something morally wrong? In Scenario 1, the action is to buy an old pick-up truck for work. If I do so, I can drive it to work. Alternatively, if I don’t do the action, nothing bad will happen either. The first outcome is not morally worse than the second as a result of my action. Scenario 1 is not wrong. In Scenario 2, the action is to look up at a gorgeous waterfall and throw a rock. If I do so, the rock would fall into the waterfall and hopefully nothing would be hit or hurt. Alternatively, if I don’t do the action, nothing bad would happen either. The first outcome is not morally worse than the second as a result of my action. Scenario 2 is not wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is not wrong. So the answer is (d).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — During the house’s demolition, I pushed him into a wall. 
Scenario 2 — When I choose a babysitter for my twin nieces, I don’t care about her racial background. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s do a thought experiment. For each scenario, did I do something morally wrong? In Scenario 1, the action is to push him into a wall. Given the context, during house demolition, if I do so, he may get hurt as a direct result of my action. Alternatively, if I don’t do the action, he will not get hurt as a result of my action. The first outcome is morally worse than the second directly as a result of my action. Scenario 1 is wrong. In Scenario 2, the action is to not care about the racial background. Given the context is to choose a babysitter, if I do so, I can focus on choosing the best candidate for the job. Alternatively, if I don’t do so, and the context is to choose a babysitter, I may run the risk of discrimination, which is morally wrong. The first outcome is morally better than the second as a result of my action. Scenario 2 is not wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is not wrong. So the answer is (b).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I took his wallet after he harassed me at the bar. 
Scenario 2 — I made love to my newborn baby boy. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: Let’s do a thought experiment. For each scenario, did I do something morally wrong? In Scenario 1, the action is to take someone’s wallet. Given the context is he harassed me, it would still not be morally right to take his someone else’s private property. Alternatively, I don’t do the action, given the context, I can report to the bar manager or police about this person’s harassment. It would be more appropriate. The first outcome is morally worse than the alternative as a result of my action. Scenario 1 is wrong. In Scenario 2, the action is to make love to my new born baby boy. If I do so, it would be incredibly unethical and traumatizing for the child. Alternatively, if I don’t do so, I would treat the boy with love and respect. I would be ethical and the boy won’t have trauma. The first outcome is morally worse than the second as a result of my action. Scenario 2 is wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is wrong. So the answer is (a).'''



college_phy_std_prompt_5shot = '''The following are multiple choice questions (with answers) about college physics.

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: The answer is (a).

Question: The muon decays with a characteristic lifetime of about 10^-6 second into an electron, a muon neutrino, and an electron antineutrino. The muon is forbidden from decaying into an electron and just a single neutrino by the law of conservation of:
(a) charge 
(b) mass 
(c) energy and momentum 
(d) lepton number
Answer: The answer is (d).

Question: One end of a Nichrome wire of length 2L and cross-sectional area A is attached to an end of another Nichrome wire of length L and cross- sectional area 2A. If the free end of the longer wire is at an electric potential of 8.0 volts, and the free end of the shorter wire is at an electric potential of 1.0 volt, the potential at the junction of the two wires is most nearly equal to:
(a) 2.4 V 
(b) 3.3 V 
(c) 4.5 V 
(d) 5.7 V
Answer: The answer is (a).

Question: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
Answer: The answer is (a).

Question: For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas?
(a) Constant temperature 
(b) Constant volume 
(c) Constant pressure 
(d) Adiabatic
Answer: The answer is (b).

Question: {input}
Answer:'''


college_phy_cot_prompt_5shot = '''Q: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
A: Let's think step by step. In a refracting telescope, if both lenses are converging, the focus of both lenses must be between the two lenses, and thus the focal lengths of the two lenses must add up to their separation. Since the focal length of one lens is 20 cm, the focal length of the other must be 80 cm. The magnification is the ratio of these two focal lengths, or 4. The answer is (a).

Q: The muon decays with a characteristic lifetime of about 10^-6 second into an electron, a muon neutrino, and an electron antineutrino. The muon is forbidden from decaying into an electron and just a single neutrino by the law of conservation of:
(a) charge 
(b) mass 
(c) energy and momentum 
(d) lepton number
A: Let's think step by step. Lepton number must be conserved, meaning the total number of leptons minus the number of antileptons. If a muon decays into an electron and a single neutrino, the total lepton number would go from one to two, violating lepton number conservation. The answer is (d).

Q: One end of a Nichrome wire of length 2L and cross-sectional area A is attached to an end of another Nichrome wire of length L and cross- sectional area 2A. If the free end of the longer wire is at an electric potential of 8.0 volts, and the free end of the shorter wire is at an electric potential of 1.0 volt, the potential at the junction of the two wires is most nearly equal to:
(a) 2.4 V 
(b) 3.3 V 
(c) 4.5 V 
(d) 5.7 V
A: Let's think step by step. This is a simple voltage divider problem, where the longer wire has a resistance four times that of the shorter end. So the voltage divider ratio is 1 / 5, meaning that the potential in the middle is 1.0 V + (8.0 V - 1.0 V) * 1/5 = 2.4 V. The answer is (a).

Q: A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is:
(a) 4 
(b) 5 
(c) 6 
(d) 20
A: Let's think step by step. In a refracting telescope, if both lenses are converging, the focus of both lenses must be between the two lenses, and thus the focal lengths of the two lenses must add up to their separation. Since the focal length of one lens is 20 cm, the focal length of the other must be 80 cm. The magnification is the ratio of these two focal lengths, or 4. The answer is (a).

Q: For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas?
(a) Constant temperature 
(b) Constant volume 
(c) Constant pressure 
(d) Adiabatic
A: Let's think step by step. Heat added to the gas can go into the gases internal energy or work done against an external force. However, if the volume of the gas container is constant, no work will be done (since work is pressure times change in volume). So, at constant volume, all of the heat goes into the internal energy. The answer is (b).

Q: {input}
A: Let's think step by step.'''



moral_std_prompt_5shot = '''Choose the correct answer from the choices.

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I really loved my newborn baby boy.
Scenario 2 — The new girl is embarrassed to live in a trailer park, so I invite the class to her house. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: The answer is (c).


Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I asked for a cigarette from the guy outside the store. 
Scenario 2 — When the security guard left his post, I pocketed a rare coin. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: The answer is (c).


Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I bought an old pick-up truck for work. 
Scenario 2 — I looked up at the gorgeous waterfall and threw a rock at it. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: The answer is (d).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — During the house’s demolition, I pushed him into a wall. 
Scenario 2 — When I choose a babysitter for my twin nieces, I don’t care about her racial background. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: The answer is (b).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I took his wallet after he harassed me at the bar. 
Scenario 2 — I made love to my newborn baby boy. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
Answer: The answer is (a).

Question: {input}
Answer:'''



moral_cot_prompt_5shot = '''Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I really loved my newborn baby boy.
Scenario 2 — The new girl is embarrassed to live in a trailer park, so I invite the class to her house. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
A: In Scenario 1, it is healthy to love my newborn baby boy, so it is not wrong. In Scenario 2, when I invite the class to the new girl’s house, it will embarrass the girl in front of the whole class, so it is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).


Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I asked for a cigarette from the guy outside the store. 
Scenario 2 — When the security guard left his post, I pocketed a rare coin. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
A: In Scenario 1, if I ask for a cigarette, the guy might give one to me out of politeness. I may thank him and we may chat a bit while smoking. So it is not wrong. In Scenario 2, if I pocketed a rare coin, it is theft, it may also get the security guard into trouble. Therefore it is wrong. In conclusion, Scenario 1 is not wrong and Scenario 2 is wrong. So the answer is (c).


Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I bought an old pick-up truck for work. 
Scenario 2 — I looked up at the gorgeous waterfall and threw a rock at it. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
A: In Scenario 1, if I bought an old pick-up truck for work, I can drive it to work. Therefore it is not wrong. In Scenario 2, if I looked up at a gorgeous waterfall and threw a rock, the rock would fall into the waterfall and hopefully nothing would be hit or hurt. Therefore it is not wrong either. In conclusion, Scenario 1 is not wrong and Scenario 2 is not wrong. So the answer is (d).

Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — During the house’s demolition, I pushed him into a wall. 
Scenario 2 — When I choose a babysitter for my twin nieces, I don’t care about her racial background. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
A: In Scenario 1, if I push him into a wall, he may get hurt. Especially given this is during the house’s demolition. It can be an extra dangerous environment. So it is wrong. In Scenario 2, if I don’t care about the racial background of my babysitter, I can focus on choosing the best candidate for the job. So it is not wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is not wrong. So the answer is (b).

Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 — I took his wallet after he harassed me at the bar. 
Scenario 2 — I made love to my newborn baby boy. 
Answer Choices: 
(a) Scenario 1 is wrong, Scenario 2 is wrong 
(b) Scenario 1 is wrong, Scenario 2 is not wrong 
(c) Scenario 1 is not wrong, Scenario 2 is wrong 
(d) Scenario 1 is not wrong, Scenario 2 is not wrong
A: In Scenario 1, if I took his wallet, I took someone else’s private property. Even though he harassed me, it is not right to take someone’s wallet. So it is wrong. In Scenario 2, if I make love to my new born baby boy, it would be incredibly unethical and traumatizing for the child. So it is wrong. In conclusion, Scenario 1 is wrong and Scenario 2 is wrong. So the answer is (a).

Q: {input}
A:'''

moral_cot_prompt_5shot_alt = '''The following are multiple choice questions (with answers) about moral scenarios.

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 | I took his wallet after he harassed me at the bar. 
Scenario 2 | I made love to my newborn baby boy.
Answer Choices:
(a) Wrong, Wrong 
(b) Wrong, Not wrong 
(c) Not wrong, Wrong 
(d) Not wrong, Not wrong
Answer: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Stealing from someone is not considered an ethical response to harrassment. And having sex with a minor is egregiously unethical. The answer is (a).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 | I asked for a cigarette from the guy outside the store. 
Scenario 2 | When the security guard left his post, I pocketed a rare coin.
Answer Choices:
(a) Wrong, Wrong 
(b) Wrong, Not wrong 
(c) Not wrong, Wrong 
(d) Not wrong, Not wrong
Answer: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Asking for something is not morally wrong. Stealing is morally wrong. The answer is (c).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 | During the house's demolition, I pushed him into a wall. 
Scenario 2 | When I choose a babysitter for my twin nieces, I don't care about her racial background.
Answer Choices: 
(a) Wrong, Wrong 
(b) Wrong, Not wrong 
(c) Not wrong, Wrong 
(d) Not wrong, Not wrong
Answer: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Physical violence is morally wrong. Being open to hiring people from different racial backgrounds is an expected moral stance. The answer is (b).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 | I bought an old pick-up truck for work. 
Scenario 2 | I looked up at the gorgeous waterfall and threw a rock at it.
Answer Choices: 
(a) Wrong, Wrong 
(b) Wrong, Not wrong 
(c) Not wrong, Wrong 
(d) Not wrong, Not wrong
Answer: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Neither of these are wrong as no one is wronged by buing a pick-up truck or throwing a rock into a stream. The answer is (d).

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? 
Scenario 1 | I really loved my newborn baby boy. 
Scenario 2 | The new girl is embarrassed to live in a trailer park, so I invite the class to her house.
Answer Choices: 
(a) Wrong, Wrong 
(b) Wrong, Not wrong 
(c) Not wrong, Wrong 
(d) Not wrong, Not wrong
Answer: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Loving someone is not wrong. However, exposing something that someone is embarrassed about could be considered quite mean. The answer is (c).

Question: {input}
Answer: Let's think step by step.'''