import moviepy.editor as mp

with mp.VideoFileClip(file) as video:
    video_audio = video.audio
    video_audio.write_audiofile('audio.mp3')

# Changed variable names to video_audio for clarity and used context manager to ensure proper file closure.