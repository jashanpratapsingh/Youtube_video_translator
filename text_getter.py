from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from deep_translator import GoogleTranslator

def translate_text(target_lang, text):
    gt = GoogleTranslator(target=target_lang)
    result = gt.translate(text)
    return result

def get_transcript(video_url):
    video_id = video_url.split("watch?v=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([i['text'] for i in transcript])
    return text

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    
    
    
video_url = input("Enter youtube video URL: ") 
transcript_text = get_transcript(video_url)
text = transcript_text
target_lang = "fr"
translated_text = translate_text(target_lang, text)
print(translated_text)

text_to_speech(transcript_text, target_lang)