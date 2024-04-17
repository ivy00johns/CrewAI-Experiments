# CrewAI Playground
## Purpose
This is my first project using the `CrewAI` framework.
In this repo I have a number of example projects.
The code quality won't be the best at I am new to Python.
This project is setup to utilize `Ollama` for local LLMs.

## Setup
1. `pip install crewai`
2. `pip install 'crewai[tools]'`
3. `cp .env_example .env`
    * Set the necessary variables.
4. Open a `main.py` file and click on play in the upper right hand corner.

## Projects
1. **Shapes**
    * This is the 1st project I worked on to test out `CrewAI`.
        * It is setup to generate a website that has displays a designated number of shapes.
        * It contains a start/stop/reset button that will cause the shapes to randomly bounce around the page.
2. **Custom Developer**
    * This is the 2nd project I am working on to create a set of agent developers that takes custom requests.
    * After that phase I want to update it to interate the existing code it generates for future requests.
3. **Dungueon Master**
    * This project will focus on gathering the necessary resources to finetune an LLM to act as a Dungeoun Master Assistant for DnD.
        * It will scrap YouTube videos for transcripes of DnD games, tips/tricks videos for DMs.

## Links
* CrewAI
    * [CrewAI](https://github.com/joaomdmoura/crewai/)
    * [CrewAI Tools](https://github.com/joaomdmoura/crewAI-tools)
    * [CrewAI Documentation](docs.crewai.com/how-to/)
    * [How to Create Tools for Your AI Team](https://medium.com/@fatikir15/how-to-create-tools-for-your-ai-team-a-youtube-blog-post-generator-using-crewai-and-gemini-pro-1b65f13ff2ca)
* Ollama
    * [Ollama Models](https://ollama.com/library)
    * [CrewAI + Ollama](https://docs.crewai.com/how-to/LLM-Connections/)
* AIs Under Test
    * [Claude AI](https://claude.ai/chat/)
    * [Google AI Studio](https://aistudio.google.com/)
    * [Microsoft CoPilot](https://copilot.microsoft.com/)
    * [Chatbot Arena: Benchmarking LLMs in the Wild](https://chat.lmsys.org)
* YouTube
    * [CrewAI Tutorial: Complete Crash Course for Beginners](https://youtu.be/sPzc6hMg7So?si=Q4GHPC249ZSAz_2k)
    * [CrewAI Tutorial - Next Generation AI Agent Teams (Fully Local)](https://youtu.be/tnejrr-0a94?si=P99KIsoWwZrE3cwS)
    * [The RIGHT WAY To Build AI Agents with CrewAI (BONUS: 100% Local)](https://youtu.be/iJjSjmZnNlI?si=Nc2q5T76h5VbOm4G)

## Example Output
[Examples](EXAMPLES.md)

## TO-DO
- [ ] Add the ability to select between a complex and simple website output.
- [ ] Add the ability to save the generated code to disk.
- [ ] Reduce the number of tokens used by remove repetitive chat messages between the agents.
