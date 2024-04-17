from crewai import Task
from textwrap import dedent

class DataGatheringTasks:
	def youtube_transcript_task(self, agent, url):
		return Task(
			description=dedent(f"""
				**Task**
				Download YouTube Transcript

				**URL**
				{url}

				**Objective**
				Use the `youtube_transcript_tool` to extract the transcript from the YouTube video at the provided URL and return it as plain text."""),
			agent=agent,
			expected_output="The transcript of the YouTube video as plain text."
		)

	def web_scraping_task(self, agent, url):
		return Task(
			description=dedent(f"""
				**Task**
				Scrape Website Content

				**URL**
				{url}

				**Objective**
				Extract relevant information from the website at the provided URL and save it as a .txt file."""),
			agent=agent,
			expected_output="A .txt file containing the extracted information from the website."
		)
