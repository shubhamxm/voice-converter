import speech_recognition as sr
from googletrans import Translator

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        transcribed_text = recognizer.recognize_google(audio, language="en-US")
        return transcribed_text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error requesting results; {0}".format(e))

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

if __name__ == "__main__":
    english_audio_file = "output_audio.wav"  # Replace with the path to your English audio file

    transcribed_text = transcribe_audio(english_audio_file)
    translated_text = translate_text(transcribed_text, "en", "hi")
    
    print("Transcribed English Text:", transcribed_text)
    print("Translated Hindi Text:", translated_text)
