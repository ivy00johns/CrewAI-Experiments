import os
import json
import requests

from bs4 import BeautifulSoup
from langchain.tools import tool
from helpers import is_already_downloaded, download_file 

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

@tool("Google Search")
def google_search(query): 
	"""
	Searches the web using the Google Custom Search JSON API.
	""" 
	api_key = os.environ.get("GOOGLE_API_KEY")
	search_engine_id = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")

	if not api_key or not search_engine_id:
		return "Error: Missing GOOGLE_API_KEY or GOOGLE_SEARCH_ENGINE_ID environment variables."

	url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"

	try:
		response = requests.get(url)
		response.raise_for_status()

		results = response.json()
		items = results.get("items", [])

		if items:
			return "\n".join([f"{item['title']}: {item['link']}" for item in items[:5]])  # Return top 5 results
		else: 
			return "No results found."
	except Exception as e:
		return f"Error during web search: {e}"

@tool("Archive.org DnD Content Downloader")
def download_dnd_content(search_term, output_directory):
	"""
	Searches archive.org for DnD content using the advanced search API and downloads relevant files, avoiding duplicates.
	"""
	try:
		# Construct the advanced search API URL
		base_url = "https://archive.org/advancedsearch.php"
		params = {
			"q": search_term,
			"fl[]": "identifier, format, name",  # Retrieve relevant fields
			"rows": "50",  # Number of results per page (adjust as needed)
			"page": "1",
			"output": "json",
			"callback": "callback",
			"save": "yes"
		}
		response = requests.get(base_url, params=params)
		response.raise_for_status()

		# Extract JSON data from the response (handling the 'callback(...)' wrapper)
		json_data = json.loads(response.text[9:-1])  

		# Process search results and download files
		downloaded_files = []
		for item in json_data["response"]["docs"]:
			identifier = item["identifier"]
			name = item["name"]
			format = item["format"]

			# Check if already downloaded (implement your chosen method here)
			if is_already_downloaded(identifier, output_directory):
				continue  

			# Prioritize .txt, then consider other formats
			if format == "Text":
				file_url = f"https://archive.org/download/{identifier}/{name}.txt"
			elif format in ["PDF", "Torrent"]:
				# Handle other formats as needed
				pass
			else: 
				continue  # Skip unsupported formats

			# Download the file (implement download logic here)
			download_file(file_url, output_directory, name)
			downloaded_files.append(name)

		return f"Downloaded {len(downloaded_files)} files: {downloaded_files}" 

	except Exception as e:
		return f"Error downloading content: {e}"
