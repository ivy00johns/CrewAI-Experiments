import os
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
