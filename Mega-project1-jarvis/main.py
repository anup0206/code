

import webbrowser
import pyttsx3
import subprocess
import speech_recognition as sr

recognizer = sr.Recognizer()



def speak(text):
    try:
        subprocess.run(["espeak", text])
    except Exception as e:
        print("espeak failed:", e)

if __name__ == "__main__":
    speak("Hello Anupam, fallback mode active.")

