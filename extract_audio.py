# Install the Google API client library for Python
!pip install --upgrade google-api-python-client

# Authenticate the YouTube API
from googleapiclient.discovery import build

# Replace API_KEY with the provided API key
api_key = 'API_KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

# Replace VIDEO_ID with the actual video ID
video_id = 'VIDEO_ID'

# Retrieve audio stream information
response = youtube.videos().list(part='contentDetails', id=video_id).execute()
audio_information = response['items'][0]['contentDetails']['audioStreams'][0]

# Analyze audio stream information
stream_map = audio_information['muxingStream']['audioStreamList'][0]['channelLayout']['map']
stream_index = stream_map[0]

# Extract audio track
command = f"ffmpeg -i https://www.youtube.com/watch?v={video_id} -map 0:a:{stream_index} -ab 160k -ac 2 -ar 44100 -vn audio.mp3"
!{command}

print("Audio track has been extracted and saved to audio.mp3.")