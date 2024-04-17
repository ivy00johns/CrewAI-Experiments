from crewai import Task
from textwrap import dedent

class DataGatheringTasks:
	def youtube_transcript_task(self, agent, youtube_url):
		return Task(
			description=dedent(f"""
				**Task**
				Download YouTube Transcript

				**Objective**
				Use the `Get YouTube Transcript` tool with the following URL: {youtube_url}
				Return the extracted transcript as plain text. 
			"""),
			agent=agent,
			expected_output="The transcript of the YouTube video as plain text."
		)
