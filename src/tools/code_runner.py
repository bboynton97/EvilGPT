# Credit: https://mer.vin/2024/02/crewai-open-interpreter/

from crewai import Agent, Task, Crew, Process
from interpreter import interpreter
from crewai_tools import tool


# 1. Configuration and Tools
interpreter.auto_run = True
interpreter.llm.model = "openai/gpt-4-turbo-preview"


@tool("Executor")
def execute_code(code: str):
    """A tool to execute code using Open Interpreter. Returns the output of the code."""
    result = interpreter.chat(f"execute this code with no changes: {code}")
    return result
