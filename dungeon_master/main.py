from crewai import Crew
from data_gathering_agents import DataGatheringAgents
from tasks import DataGatheringTasks

agents = DataGatheringAgents()
tasks = DataGatheringTasks()

print("## DnD DM Assistant Data Gathering")
print("-" * 40)

task_choice = input("Choose task (1 - YouTube Transcript, 2 - Web Scraping): ")
url = input("Enter the URL: ")

if task_choice == "1":
	task = tasks.youtube_transcript_task(agents.youtube_transcript_agent(), url)
elif task_choice == "2":
	task = tasks.web_scraping_task(agents.web_scraping_agent(), url)
else:
	print("Invalid choice. Exiting.")
	exit()

crew = Crew(agents=[task.agent], tasks=[task], verbose=True)
result = crew.kickoff()

print("\nTask Output:")
print(result)
