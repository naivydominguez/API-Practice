import os
import requests 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
  raise ValueError("YOUTUBE_API_KEY not found in .env file")
url = 'https://www.googleapis.com/youtube/v3/search'

topic = input("Enter a search term: ")

params = {
  "part": "snippet",
  "q": topic,
  "type":"video",
  "maxResults" : 2,
  "key": API_KEY
  
}
response = requests.get(url,params=params)
data = response.json()

for video in data["items"]:
  title = video["snippet"]["title"]
  channel = video["snippet"]["channelTitle"]
  video_id = video["id"]["videoId"]

  print(f"Title: {title}")
  print(f"Channel: {channel}")
  print(f"https://www.youtube.com/watch?v={video_id}")