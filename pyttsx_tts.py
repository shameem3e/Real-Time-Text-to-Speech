# pyttsx_tts.py
import pyttsx3

def speak(text, voice=None, rate=150):
    """Speak text using offline pyttsx3 engine."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice:
        for v in voices:
            if voice.lower() in v.name.lower():
                engine.setProperty('voice', v.id)
                break

    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
