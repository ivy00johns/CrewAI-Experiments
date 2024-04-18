from crewai import Task
from textwrap import dedent

class DataGatheringTasks:
	def youtube_transcript_task(self, agent, url):
		return Task(
			description=dedent(f"""
				**Task**
				Download YouTube Transcript

				**Objective**
				Use the `Get YouTube Transcript` tool with the following URL: {url}

				Return the extracted transcript as plain text.
			"""),
			agent=agent,
			expected_output="The transcript of the YouTube video as plain text."
		)

	def web_scraping_task(self, agent, url, filename):
		return Task(
			description=dedent(f"""
				**Task**
				Scrape Website Content

				**URL:** {url}
				**Filename:** {filename}

				**Objective**
				Use the `Scrape Website` tool to extract text content from the website at the given URL and save it to a file named {filename}.txt.
			"""),
			agent=agent,
			expected_output=f"Text content from the website saved as {filename}.txt" 
		)
