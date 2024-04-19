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

class ResearchTasks:
	def research_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify Research Tools

				**Your Role**
				{agent.role}

				**Objective**
				Based on your expertise and goals, identify and list the essential tools and resources that would be most helpful in achieving your objectives. 
				Consider both traditional resources (books, websites, communities) and AI-powered tools that could enhance your research capabilities.
			"""),
			agent=agent,
			expected_output="A list of tools and resources relevant to your role and goals."
		)

	def content_curation_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify Content Curation Tools

				**Your Role**
				{agent.role}

				**Objective**
				Identify and list the tools and methods that would be most effective in gathering, organizing, and preparing high-quality DnD content for use in training an LLM assistant.
				Consider tools for accessing various content sources, filtering and categorizing information, and ensuring data quality and consistency.
			"""),
			agent=agent,
			expected_output="A list of tools and methods for effective DnD content curation."
		)

	def llm_training_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify LLM Training Tools

				**Your Role**
				{agent.role}

				**Objective**
				List the tools and resources necessary to design and implement an effective training process for an LLM assistant for DnD.
				Consider tools for data preprocessing, model selection, training pipelines, and evaluation metrics. 
			"""),
			agent=agent,
			expected_output="A list of tools and resources for LLM training in the context of DnD." 
		)

	def campaign_assistance_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify Campaign Assistance Tools

				**Your Role**
				{agent.role}

				**Objective**
				List the tools and resources that would be most helpful in assisting Dungeon Masters during DnD campaigns. 
				Consider tools for generating encounters, managing NPCs, creating maps, and providing real-time support and inspiration.
			"""),
			agent=agent,
			expected_output="A list of tools and resources to assist Dungeon Masters during campaigns."
		)

	def lore_expertise_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify Lore Expertise Tools

				**Your Role**
				{agent.role}

				**Objective**
				Identify and list the tools and resources that would enable you to access, analyze, and interpret the vast lore of Dungeons & Dragons effectively. 
				Consider tools for searching and retrieving lore information, summarizing complex narratives, and exploring connections between different aspects of the DnD universe.
			"""),
			agent=agent,
			expected_output="A list of tools and resources to enhance your DnD lore expertise."
		)

	def rules_and_mechanics_tools_task(self, agent):
		return Task(
			description=dedent(f"""
				**Task**
				Identify Rules and Mechanics Tools

				**Your Role**
				{agent.role}

				**Objective**
				List the tools and resources that would be most helpful in understanding, interpreting, and applying the rules and mechanics of Dungeons & Dragons.
				Consider tools for accessing rulebooks, searching for specific rules, and staying up-to-date with the latest rulings and interpretations.
			"""),
			agent=agent,
			expected_output="A list of tools and resources to enhance your understanding of DnD rules and mechanics." 
		)
