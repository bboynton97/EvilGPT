from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools

@CrewBase
class EvilgptCrew():
	"""evilgpt crew"""

	# Agent definitions

	# Task definitions

	@crew
	def crew(self) -> Crew:
		"""Creates the Test crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)