from moviepy.video.io.VideoFileClip import VideoFileClip
import pyttsx3

def extract_audio(video_file, audio_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file)
    audio_clip.close()
    video_clip.close()

def text_to_speech(text, lang, output_file):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust speech rate if needed
    engine.setProperty("volume", 1.0)  # Adjust volume if needed

    voices = engine.getProperty("voices")
    for voice in voices:
        if lang in voice.languages:
            engine.setProperty("voice", voice.id)
            break

    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    video_filename = "English in a Minute Party Animal.mp4"  # Replace with your input video file
    audio_filename = "output_audio.wav"  # Replace with desired output audio file name
    hindi_text = "यह एक उदाहरण टेक्स्ट है।"  # Replace with the desired Hindi text

    extract_audio(video_filename, audio_filename)
    print(f"Audio extracted from '{video_filename}' and saved as '{audio_filename}'")

    hindi_audio_output = "output_hindi_audio.wav"
    text_to_speech(hindi_text, "hi", hindi_audio_output)
    print(f"Hindi audio generated and saved as '{hindi_audio_output}'")
