from crewai import Agent
from langchain_community.llms import Ollama  # Corrected import

class CustomAgents:
	def __init__(self):
		self.Ollama = Ollama(model="codellama")  # Replace with your Ollama model

	def html_engineer_agent(self):
		return Agent(
			role='HTML Engineer',
			goal='Create the HTML structure for the webpage',
			backstory="You are skilled in building the basic layout of websites using HTML.",
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama
		)

	def css_stylist_agent(self):
		return Agent(
			role='CSS Stylist',
			goal='Style the HTML elements with CSS',
			backstory="You have a keen eye for design and can make webpages look beautiful using CSS.",
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama
		)

	def javascript_developer_agent(self):
		return Agent(
			role='JavaScript Developer',
			goal='Implement interactivity and animation with JavaScript',
			backstory="You are proficient in JavaScript and can bring webpages to life with dynamic features.",
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama
		)
