# CoMM

This repo contains the code and data for the CoMM (Collaborative Multi-Agent, Multi-Reasoning-Path Prompting) system.

## Model

## Experiments

### College Physics - Few Shot
```commandline
python run_pathways.py --task college_physics --prompt_type pathways
```
### College Physics - Zero Shot

```commandline
python run_pathways.py --task college_physics --prompt_type multi_agent
```

### Moral Scenarios - Few Shot
```commandline
python run_pathways.py --task moral_scenarios --prompt_type pathways
```

### Moral Scenarios - Zero Shot
```commandline
python run_pathways.py --task moral_scenarios --prompt_type multi_agent
```

### Baselines

You can also reproduce the standard and chain-of-thought baselines by changing the `prompt_type` argument as `std` or `cot`, and the `context` argument as `zero` or `few`. 


## Evaluation

Please use the `evaluate()` function for evaluation, with the generated result files in the `logs` and the source test data files. 
