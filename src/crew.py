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
	        tools=[tools.FileReadTool(), tools.dir_search_tool],  # add tools here or use `agentstack tools add <tool_name>
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

	@crew
	def crew(self) -> Crew:
		"""Creates the Test crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.hierarchical,
			verbose=True,
			manager_llm=""
		)