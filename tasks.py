from crewai import Task

class CustomTasks:
	def create_html_structure(self, agent, num_shapes):
		return Task(
			description=f"""
				Create the HTML structure for a webpage with:
				- An input field to specify the number of shapes (default to {num_shapes}).
				- Buttons for 'Start,' 'Stop,' and 'Reset.'
				- A container where the shapes will be displayed.
			""",
			agent=agent,
			expected_output="HTML code for the webpage structure"  # Added expected output
		)

	def style_webpage(self, agent):
		return Task(
			description="""
				Style the HTML elements with CSS to:
				- Set a fixed size for the container.
				- Make the shapes circular with a specified size and color.
				- Position the shapes within the container.
			""",
			agent=agent,
			expected_output="CSS code for styling the webpage elements"  # Added expected output
		)

	def implement_javascript(self, agent, num_shapes):
		return Task(
			description=f"""
				Implement JavaScript code to:
				- Get the user input for the number of shapes.
				- Create {num_shapes} shapes with random initial positions and directions.
				- Animate the shapes to bounce around the container.
				- Start, stop, and reset the animation based on button clicks.
			""",
			agent=agent,
			expected_output="JavaScript code for interactivity and animation"  # Added expected output
		)
