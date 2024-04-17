from crewai import Agent
from langchain_community.llms import Ollama

class DataGatheringAgents:
	def __init__(self):
		self.Ollama = Ollama(model="codellama")  # Or any suitable LLM

	def youtube_transcript_agent(self):
		return Agent(
			role="YouTube Transcript Extractor",
			goal="Download and save transcripts from YouTube videos as .txt files",
			backstory="""
				You are an expert at extracting information from YouTube videos. You can utilize various tools and APIs to download video transcripts and save them in a structured text format for further processing and analysis. 
			""",
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama,
			tools={
				"youtube_api": "youtube_transcript_api",  # Placeholder for actual API or tool
				"file_saver": "save_to_txt"  # Placeholder for file saving functionality
			}
		)

	def web_scraping_agent(self):
		return Agent(
			role="Web Scraper",
			goal="Extract information from websites and save it as structured text data",
			backstory="""
				You are skilled at navigating the web and extracting relevant information from websites. You can utilize web scraping techniques and tools to gather text, data, and other content from specified web pages and store it in a structured format for further use.
			""",
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama,
			tools={
				"web_scraper": "beautiful_soup",  # Placeholder for a scraping library like Beautiful Soup
				"file_saver": "save_to_txt"
			}
		)
