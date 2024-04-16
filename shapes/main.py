import os
from dotenv import load_dotenv
from crewai import Crew
from shapes.tasks import CustomTasks
from shapes.agents import CustomAgents

load_dotenv()  # Load environment variables from .env

def save_code(file_name, code):
	output_dir = os.getenv("OUTPUT_DIR", "./workspace")
	file_path = os.path.join(output_dir, file_name)
	with open(file_path, "w") as f:
		text_content = code  # Or use appropriate method to get text
		f.write(text_content)
		print(f"Code saved to {file_path}.")

def main():
	num_shapes = 10  # Default number of shapes

	agents = CustomAgents()
	tasks = CustomTasks()

	html_engineer = agents.html_engineer_agent()
	css_stylist = agents.css_stylist_agent()
	js_developer = agents.javascript_developer_agent()

	create_html_task = tasks.create_html_structure(html_engineer, num_shapes)
	style_webpage_task = tasks.style_webpage(css_stylist)
	implement_js_task = tasks.implement_javascript(js_developer, num_shapes)

	crew = Crew(
		agents=[html_engineer, css_stylist, js_developer],
		tasks=[create_html_task, style_webpage_task, implement_js_task],
		verbose=True
	)

	result = crew.kickoff()
	print(result)

	for task in crew.tasks:
		if task.output:
			file_name = f"{task.agent.role}.txt"  # Customize file names as needed
			save_code(file_name, task.output)

if __name__ == "__main__":
	main()
