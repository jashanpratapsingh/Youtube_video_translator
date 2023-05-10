from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from deep_translator import GoogleTranslator
from pydub import AudioSegment
from pytube import YouTube
import moviepy.editor as mp

def translate_text(source_lang, target_lang, text):
    gt = GoogleTranslator(source=source_lang, target=target_lang)
    result = gt.translate(text)
    return result

def get_transcript(video_url):
    video_id = video_url.split("watch?v=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([i['text'] for i in transcript])
    return text

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("output/google-trans/google.mp3")
    
def truncate_string(string, max_length):
    if len(string) > max_length:
        return string[:max_length]
    return string

def speed_up_audio(input_file, output_file, speed_factor):
    audio = AudioSegment.from_file(input_file)
    faster_audio = audio.speedup(playback_speed=speed_factor)
    faster_audio.export(output_file, format='mp3')
    
def download_video(url, output_path, filename):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first().download(output_path=output_path, filename=filename)
    
def combine_audio_with_video(video_path, audio_path, output_path):
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)
    audio = audio.set_duration(video.duration)
    video_with_audio = video.set_audio(audio)
    video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')
    
def get_video_title(url):
    yt = YouTube(url)
    return yt.title

def get_audio_length(audio_file):
    audio = AudioSegment.from_file(audio_file)
    length_in_seconds = len(audio) / 1000  # Convert milliseconds to seconds
    return length_in_seconds

def trim_video(input_file, output_file, start_time, end_time):
    video = mp.VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
    
    
# this is for getting the video url from user and will remain same for all the users   
video_url = input("Enter youtube video URL: ") 
title = get_video_title(video_url)


#getting the transcript of the youtube video
transcript_text = get_transcript(video_url)
print("Got the transcript")


# This is for translating the transcript
# !truncating because the API doesn't support length above 5000
print("Translating the Text")
max_length = 4999
text = truncate_string(transcript_text, max_length)
source_lang = 'en'
target_lang = "hi"
translated_text = translate_text(source_lang, target_lang, text)

# Storing the text to speech from google speech
print("--------------------------------")
print("Running command for text to speech")
text_to_speech(translated_text, target_lang)


# Speeding up the audio because the audio from google is very slow
print("Speeding up audio")
input_file = 'output/google-trans/google.mp3'
output_file = 'output/sped_up/sped_up_audio.mp3'
speed_factor = 1.5
speed_up_audio(input_file, output_file, speed_factor)
length = get_audio_length(output_file)

print("Downloading the video file")
output_path_downloaded_video = "output/video"  # Output path for the downloaded video
filename = "final.mp4"
download_video(video_url, output_path_downloaded_video, filename)


print("Trimming video")
input_file = f"output/video/final.mp4"
output_file = 'output/trimmed/video/file.mp4'
start_time = 0
end_time = length
trim_video(input_file, output_file, start_time, end_time)

#Combining the sped up audio with the video files
print("Combining everything together")
video_path = 'output/trimmed/video/file.mp4'  # Assuming you have the video downloaded as .mp4
audio_path = "output/sped_up/sped_up_audio.mp3"  # Path to your audio file
output_path = "output/combined/combined_video.mp4"  # Output path for the combined video

combine_audio_with_video(video_path, audio_path, output_path)