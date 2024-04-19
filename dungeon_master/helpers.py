import os
import hashlib
import requests

def is_already_downloaded(identifier, output_directory):
	"""
	Checks if a file with the given identifier has already been downloaded in the output directory.

	This example uses file hashing for duplicate detection. You can adapt it to use a filename list or other methods.
	"""
	filename = f"{identifier}.txt"  # Assuming .txt files
	file_path = os.path.join(output_directory, filename)
	if os.path.exists(file_path):
		with open(file_path, "rb") as f:
			existing_file_hash = hashlib.sha256(f.read()).hexdigest() 
		return existing_file_hash == identifier  # Compare hash to identifier
	else:
		return False

def download_file(file_url, output_directory, filename):
	"""
	Downloads a file from the given URL and saves it to the specified output directory. 
	"""
	file_path = os.path.join(output_directory, filename)
	with requests.get(file_url, stream=True) as r:
		r.raise_for_status()
		with open(file_path, "wb") as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
