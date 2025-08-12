# gtts_tts.py
import os
from gtts import gTTS
from playsound import playsound
from config import OUTPUT_DIR, LANGUAGE
from datetime import datetime

def speak(text):
    """Speak text using Google Text-to-Speech (requires internet)."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = f"tts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)

    tts = gTTS(text=text, lang=LANGUAGE)
    tts.save(filepath)
    playsound(filepath)
