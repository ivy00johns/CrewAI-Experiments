import os

from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
from tools.youtube_tools import get_youtube_transcript

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
