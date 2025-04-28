

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet():
    """Greets the user"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

def take_command():
    """Listens for voice input and returns text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return ""
        
    return query.lower()

def main():
    greet()
    while True:
        query = take_command()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'anime' in query:
            speak("Opening Anime")
            webbrowser.open("https://www.kisskh.co")
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break
        elif query:
            speak("I'm not sure how to help with that yet.")

if __name__ == "__main__":
    main()
