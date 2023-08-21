from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_file, audio_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file)
    audio_clip.close()
    video_clip.close()

if __name__ == "__main__":
    video_filename = "English in a Minute Party Animal.mp4"  # Replace with your input video file
    audio_filename = "output_audio.wav"  # Replace with desired output audio file name

    extract_audio(video_filename, audio_filename)
    print(f"Audio extracted from '{video_filename}' and saved as '{audio_filename}'")
