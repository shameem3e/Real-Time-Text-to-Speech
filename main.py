# main.py
from config import MODE, VOICE, RATE
import sys

def main():
    print("🎤 Real-Time Text-to-Speech")
    print(f"[INFO] Mode: {MODE.upper()}")
    print("Type 'quit' to exit.\n")

    if MODE.lower() == "pyttsx":
        from pyttsx_tts import speak
    elif MODE.lower() == "gtts":
        from gtts_tts import speak
    else:
        print("[ERROR] Invalid MODE in config.py")
        sys.exit(1)

    while True:
        text = input("Enter text: ")
        if text.strip().lower() == "quit":
            break
        if MODE.lower() == "pyttsx":
            speak(text, voice=VOICE, rate=RATE)
        else:
            speak(text)

if __name__ == "__main__":
    main()
