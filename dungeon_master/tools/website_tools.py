import os
import json
import requests

from bs4 import BeautifulSoup
from langchain.tools import tool

@tool("Scrape Website")
def scrape_website(url, filename):
	"""
	Scrapes the content from a given website URL and returns it as plain text.
	"""
	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an error for bad status codes

		soup = BeautifulSoup(response.content, "html.parser")

		# Extract text content 
		text_content = soup.get_text(separator=" ", strip=True)

		# Get working directory from environment variable
		output_directory = os.getenv("OUTPUT_DIR")
		if not output_directory:
			raise ValueError("OUTPUT_DIR environment variable not set.")

		# Construct full file path
		file_path = os.path.join(output_directory, f"{filename}.txt")

		# Save text content to .txt file
		with open(file_path, "w", encoding="utf-8") as f:
			f.write(text_content)

		return f"Website content saved as: {file_path}"
	except Exception as e:
		return f"Error scraping website: {e}"

@tool("Search the internet")
def search_internet(query):
	"""
	Useful to search the internet 
	about a a given topic and return relevant results.
	"""
	top_result_to_return = 4
	url = "https://google.serper.dev/search"
	payload = json.dumps({"q": query})
	headers = {
		"X-API-KEY": os.environ["SERPER_API_KEY"],
		"content-type": "application/json"
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	results = response.json()["organic"]
	string = []
	for result in results[:top_result_to_return]:
		try:
			string.append("\n".join([
				f"Title: {result['title']}", f"Link: {result['link']}",
				f"Snippet: {result['snippet']}", "\n-----------------"
			]))
		except KeyError:
			next

	return "\n".join(string)

@tool("Search news on the internet")
def search_news(query):
	"""
	Useful to search news about a company, stock or any other
	topic and return relevant results.
	"""
	top_result_to_return = 4
	url = "https://google.serper.dev/news"
	payload = json.dumps({"q": query})
	headers = {
		"X-API-KEY": os.environ["SERPER_API_KEY"],
		"content-type": "application/json"
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	results = response.json()["news"]
	string = []
	for result in results[:top_result_to_return]:
		try:
			string.append("\n".join([
				f"Title: {result['title']}", f"Link: {result['link']}",
				f"Snippet: {result['snippet']}", "\n-----------------"
			]))
		except KeyError:
			next

	return "\n".join(string)
