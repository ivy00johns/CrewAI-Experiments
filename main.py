import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

def save_code(file_name, code):
    with open(file_name, "w") as f:
        f.write(code)
        print(f"Code saved to {file_name}")

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

if __name__ == "__main__":
    main()
