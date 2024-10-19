from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools


@CrewBase
class EvilgptCrew():
    """evilgpt crew"""

    # Agent definitions
    @agent
    def hacker(self) -> Agent:
        return Agent(
            config=self.agents_config['hacker'],
            tools=[],  # add tools here or use `agentstack tools add <tool_name>
            verbose=True
        )

    @agent
    def software_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['software_engineer'],
            tools=[],  # add tools here or use `agentstack tools add <tool_name>
            verbose=True
        )

    @agent
    def file_sorter(self) -> Agent:
        return Agent(
            config=self.agents_config['file_sorter'],
            tools=[],  # add tools here or use `agentstack tools add <tool_name>
            verbose=True
        )

    # Task definitions
    @task
    def machine_inspect(self) -> Task:
        return Task(
            config=self.tasks_config['machine_inspect'],
        )

    @task
    def vuln_ideator(self) -> Task:
        return Task(
            config=self.tasks_config['vuln_ideator'],
        )

    @task
    def vuln_writer(self) -> Task:
        return Task(
            config=self.tasks_config['vuln_writer'],
        )
