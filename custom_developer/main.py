from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import WebsiteTasks
from frontend_agents import FrontendAgents

# Initialize tasks and agents
tasks = WebsiteTasks()
agents = FrontendAgents()

print("## Welcome to the Website Development Crew")
print("-" * 40)
website_description = input("Describe the website you want to create: What is its purpose and target audience?\n")

# Create Agents
ui_ux_designer = agents.ui_ux_designer_agent()
senior_frontend_engineer = agents.senior_frontend_engineer_agent()
frontend_qa_engineer = agents.frontend_qa_engineer_agent()

# Create Tasks
design_phase = tasks.design_task(ui_ux_designer, website_description)
development_phase = tasks.frontend_development_task(senior_frontend_engineer, design_phase.output)  
qa_phase = tasks.frontend_qa_task(frontend_qa_engineer, development_phase.output)

# Create Crew
website_crew = Crew(
	agents=[
		ui_ux_designer,
		senior_frontend_engineer,
		frontend_qa_engineer
	],
	tasks=[
		design_phase,
		development_phase,
		qa_phase
	],
	verbose=True
)

final_result = website_crew.kickoff()

# Print results
print("\n\n########################")
print("## Website Development Summary")
print("########################\n")

print("**Design Phase Output:**")
print(design_phase.output)

print("\n**Development Phase Output:**")
print(development_phase.output)

print("\n**QA Phase Output:**")
print(qa_phase.output) 
