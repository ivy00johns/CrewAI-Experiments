import os

from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
from tools.youtube_tools import get_youtube_transcript
from tools.website_tools import scrape_website

class DataGatheringAgents:
	def __init__(self):
		self.Ollama = Ollama(model=f"{os.environ['MODEL_NAME']}")

	def youtube_transcript_agent(self):
		return Agent(
			role="YouTube Transcript Extractor",
			goal="Download and save transcripts from YouTube videos as .txt files",
			backstory=dedent("""\
				You are an expert at extracting information from YouTube videos.
				You can utilize various tools and APIs to download video
					transcripts and save them in a structured text format for
					further processing and analysis."""),
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama,
			tools=[
				get_youtube_transcript
			]
		)

	def web_scraping_agent(self):
		return Agent(
			role="Web Scraper",
			goal="Extract information from websites and save it as text files",
			backstory=dedent("""\
				You are skilled at extracting information from websites
					using web scraping techniques.
				You can navigate through HTML structures and gather text content,
					saving it for further processing."""),
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama,
			tools=[
				scrape_website
			]
		)
