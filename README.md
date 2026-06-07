## Human Communication and AI Alignment with Non-Linear Reward Functions and Negative Reward
The paper is based on the work of **How to talk so your AI will learn: Instructions, descriptions, and autonomy** by Theodore R Sumers, Robert D Hawkins, Mark K Ho, Thomas L Griffiths, and Dylan Hadfield-Menell.

How to Talk GitHub: https://github.com/tsumers/how-to-talk/tree/master

How to Talk Paper: https://arxiv.org/abs/2206.07870

### Algorithm Changes
Major changes to the algorithm are contained to the pragmatic_listener.py file. Additionally, a Social_and_Reinforcement_Learning and Speakers_and_Listeners file has been created for each model-risk combination.

### Contents
The data folder contains the human responses organized into files by model-risk combinations. They also contain the resulting utterance_posterior_rewards.csv for each combination.

The figures folder contines the figures used in the paper. The raw data folder contains the data before being split into the different csv files.

### Reproducability
1. Install the environment via Conda: conda env create -f environment.yml.
2. Run Social_and_Reinforcement_Learning for each condition, make sure to have it use the corresponding json file (DMU_Risk, DMU, IMU_Risk, etc).
3. Rename each cached_inference and cached_thompson_sampling folder after creation so the future models do not override each other.
4. Rename the desired cache folders back to cached_inference and cached_thompson_sampling when being used.
5. Run Speakers_and_Listeners after cache creation, make sure to use the corresponding cache folders, json, and ipynb files.
6. Run the resulting utterance_posterior_rewards.csv file with analysis.Rmd to see paired t-test results.
