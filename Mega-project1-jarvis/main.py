

import webbrowser
import pyttsx3
import subprocess
import speech_recognition as sr

recognizer = sr.Recognizer()

def speak(text):
    try:
        # Female voice, slower speed, and pleasant pitch
        subprocess.run(["espeak", "-v", "en+f3", "-s", "110", "-p", "70", text])
    except Exception as e:
        print("espeak failed:", e)




if __name__ == "__main__":
    speak("Hey baby, What's up ")

