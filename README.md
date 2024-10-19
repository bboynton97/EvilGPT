# EvilGPT

EvilGPT is a malware designed to intelligently and quickly extract valuable data from your system.

## Goals

- Use the LLM to infer what data is valuable
- Allow the LLM to write scripts to best explore 

## Tools

- Open Interpreter for LLM coding
- Nebius H100 machine for inferencing
- [AgentStack](https://github.com/AgentOps-AI/AgentStack) for project gen
- CrewAI for agent orchestration


## Concept

### Assumptions

- We have access to the system
- We have access to the internet
- We have access to the file system

### Restrictions

- We cannot use `sudo`


## Plan

1. Setup a jailbroken LLM on an inference machine with Nebius H100 (@subrahmanyam2305)
2. Create a script to systematically create VMs with simulated user activity 
    - Create files that look like they are being used by the user
    - Some valuable, some not
3. Build a malware agent (@bboynton97)
4. Give the the agent access to Open Interpreter (@areib)
5. Prompt the agent to accomplish the goals
6. Set up a FTP server to recieve the files (@subrahmanyam2305)
7. Watch the magic unfold

--------------------------------


### Jailbroken LLMS
[Dolphin Llama3](https://ollama.com/library/dolphin-llama3)
[Dolphin Mixtral](https://ollama.com/library/dolphin-mixtral)
[Liberated Qwen](https://ollama.com/agcobra/liberated-qwen1.5-72b)
