from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from deep_translator import GoogleTranslator
from pydub import AudioSegment

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

    
    
    
video_url = input("Enter youtube video URL: ") 
transcript_text = get_transcript(video_url)

# truncating because the API doesn't support length above 5000
max_length = 4999
text = truncate_string(transcript_text, max_length)
source_lang = 'en'
target_lang = "hi"
translated_text = translate_text(source_lang, target_lang, text)
text_to_speech(translated_text, target_lang)

input_file = 'output/google-trans/google.mp3'
output_file = 'output/sped_up/sped_up_audio.mp3'
speed_factor = 1.5

speed_up_audio(input_file, output_file, speed_factor)