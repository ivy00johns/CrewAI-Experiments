from youtube_transcript_api import YouTubeTranscriptApi
from crewai_tools import tool

@tool("Get Youtube Transcript")
def get_youtube_transcript(youtube_url):
	"""
	Extracts the transcript from a YouTube video given its URL. 
	"""
	try:
		# Extract video ID from URL
		video_id = youtube_url.split("v=")[1]

		# Fetch transcript using youtube_transcript_api
		transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

		# Convert transcript to text format
		transcript_text = " ".join([item["text"] for item in transcript_list])

		return transcript_text
	except Exception as e:
		return f"Error extracting transcript: {e}"
