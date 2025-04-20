#!/usr/bin/env python3
import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine  = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ =="__main__":
    speak("Hey , myself pptsx3")
    


