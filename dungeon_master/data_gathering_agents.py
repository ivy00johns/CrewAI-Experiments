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
				You can utilize tools like the 'youtube_transcript_api' library to download video transcripts in various formats, including plain text, SRT, and VTT. 
				You are adept at handling errors and cases where transcripts are not available, and you can even extract timestamps and identify speakers within the transcripts. 
			"""),
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
				You are skilled at extracting information from websites using various web scraping techniques, including HTML parsing, CSS selectors, and XPath expressions.
				You can effectively gather text content, tables, images, and links from diverse website structures and layouts.
				You are also adept at bypassing anti-scraping measures like CAPTCHAs and IP blocking to access valuable data.
			"""),
			allow_delegation=False,
			verbose=True,
			llm=self.Ollama,
			tools=[
				scrape_website
			]
		)
