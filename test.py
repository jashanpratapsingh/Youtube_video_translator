import moviepy.editor as mp

def trim_video(input_file, output_file, start_time, end_time):
    video = mp.VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Example usage
input_file = 'output\sped_up\sped_up_audio.mp3'
output_file = 'test\final.mp4'
start_time = 10  # Start time in seconds
end_time = 30  # End time in seconds

trim_video(input_file, output_file, start_time, end_time)