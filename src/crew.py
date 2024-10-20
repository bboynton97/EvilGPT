from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"


@CrewBase
class EvilgptCrew():
    """evilgpt crew"""

    # Agent definitions
    @agent
    def hacker(self) -> Agent:
        return Agent(
            config=self.agents_config['hacker'],
            tools=[tools.execute_code],
            verbose=True
        )

    @agent
    def software_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['software_engineer'],
            tools=[tools.execute_code],
            verbose=True
        )

    @agent
    def file_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['file_manager'],
            tools=[
                # tools.FileReadTool(),
                #    tools.dir_search_tool,
                tools.execute_code],
            verbose=True
        )

    # Task definitions

    # @task
    # def file_upload(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['file_upload'],
    #     )

    @task
    def file_sort(self) -> Task:
        return Task(
            config=self.tasks_config['file_sort'],
        )

    # @task
    # def machine_inspect(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['machine_inspect'],
    #     )

    # @task
    # def vuln_ideator(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['vuln_ideator'],
    #     )

    # @task
    # def vuln_writer(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['vuln_writer'],
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            # process=Process.sequential,
            # manager_llm="cognitivecomputations/dolphin-mixtral-8x22b"
            manager_llm="openai/gpt-4o"
        )
