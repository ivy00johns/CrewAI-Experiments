from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from agents import DataGatheringAgents
from tasks import DataGatheringTasks

dataAgents = DataGatheringAgents()
dataTasks = DataGatheringTasks()

print("## DnD DM Assistant Data Gathering")
print("-" * 40)

task_choice = input("Choose task (1 - YouTube Transcript, 2 - Web Scraping): ")

if task_choice == "1":
	url = input("Enter the YouTube video URL: ")
	task = dataTasks.youtube_transcript_task(dataAgents.youtube_transcript_agent(), url)
elif task_choice == "2":
	website_url = input("Enter the website URL: ")
	filename = input("Enter the desired filename for the extracted content: ")
	task = dataTasks.web_scraping_task(dataAgents.web_scraping_agent(), website_url, filename) 
else:
	print("Invalid choice. Exiting.")
	exit()

crew = Crew(agents=[task.agent], tasks=[task], verbose=True)
result = crew.kickoff()

print("\nTask Output:")
print(result)
