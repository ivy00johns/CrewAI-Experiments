from youtube_transcript_api import YouTubeTranscriptApi
from langchain.tools import tool
from pytube import YouTube

@tool("Get YouTube Transcript")
def get_youtube_transcript(url):
	"""
	Extracts the transcript from a YouTube video given its URL and saves it as a .txt file with the video title as the filename. 
	"""
	try:
		# Extract video ID and title
		yt = YouTube(url)
		video_id = yt.video_id
		video_title = yt.title

		# Remove special characters from title for filename
		safe_filename = "".join([c for c in video_title if c.isalnum() or c in "._- "]).rstrip()

		# Fetch transcript using youtube_transcript_api
		transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

		# Convert transcript to text format
		transcript_text = " ".join([item["text"] for item in transcript_list])

		# Save transcript to .txt file
		with open(f"{safe_filename}.txt", "w", encoding="utf-8") as f:
			f.write(transcript_text)

		return f"Transcript saved as: {safe_filename}.txt"
	except Exception as e:
		return f"Error extracting transcript: {e}"
