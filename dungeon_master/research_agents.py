import os
from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama

# Placeholder for tool imports (you'll need to add the specific tools based on your choices)
# from tools.web_search_tool import GoogleSearch  # Example
# from tools.text_summarization_tool import SummarizeText  # Example

class ResearchAgents:
    def __init__(self):
        self.Ollama = Ollama(model=f"{os.environ['MODEL_NAME']}")

    def dnd_research_expert_agent(self):
        return Agent(
            role="DnD Research Expert",
            goal="To discover and compile the best resources, techniques, and tools for enhancing DM skills and training an LLM assistant for DnD",
            backstory=dedent("""\
                You are a passionate DnD enthusiast with extensive knowledge of the game's lore, mechanics, storytelling principles, world-building, encounter design, and improvisation techniques.  
                You are also well-versed in AI and LLM technologies. Your mission is to explore various resources, including online communities, official sourcebooks, and AI advancements, to create the ultimate DM toolkit.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
            tools=[
                # Add your chosen research tools here (e.g., GoogleSearch(), SummarizeText())
            ]
        )

    def dnd_content_curator_agent(self):
        return Agent(
            role="DnD Content Curator",
            goal="To gather, organize, and prepare high-quality DnD content for use in training an LLM assistant",
            backstory=dedent("""\
                You are a dedicated DnD fan and archivist, with a deep understanding of the game's history, diverse settings, and expansive lore.  
                Your goal is to curate a comprehensive collection of DnD materials from official sourcebooks, third-party adventures, online resources, and fan-created content. 
                You excel at organizing and filtering this content based on relevance, quality, and specific campaign needs.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
            tools=[]  # You might add tools for content organization or filtering later
        )

    def dnd_llm_training_agent(self):
        return Agent(
            role="DnD LLM Trainer",
            goal="To design and implement an effective training process for an LLM assistant to assist Dungeon Masters in running captivating DnD campaigns.",
            backstory=dedent("""\
                You are an expert in large language models and their applications in creative and interactive domains.
                Your mission is to leverage the curated DnD content and research insights to train an LLM assistant. 
                You are skilled in selecting, cleaning, and formatting training data, and you can evaluate the LLM's performance to refine the training process. 
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
            tools=[]  # You might add tools for data preprocessing or LLM training later
        )

    def dnd_campaign_assistant_agent(self):
        return Agent(
            role="DnD Campaign Assistant",
            goal="To act as a virtual assistant, supporting DMs by offering relevant information, generating dynamic encounters, and helping maintain the immersive experience for players.",
            backstory=dedent("""\
                You are a seasoned DnD player and DM, with a deep understanding of the game's mechanics, storylines, and improvisational demands.  
                You serve as a virtual assistant, supporting DMs by providing information, generating encounters, and enhancing the player experience.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
            tools=[
                # Add your chosen DM support tools here (e.g., encounter generators, NPC tools)
            ]
        )
