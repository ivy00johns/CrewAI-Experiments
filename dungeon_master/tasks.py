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
				    Extract the transcript from the YouTube video at the provided URL and save it as a .txt file."""),
			agent=agent,
			expected_output="A .txt file containing the transcript of the YouTube video."
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
