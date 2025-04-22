import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import requests
import openai
from gtts import gTTS
import pygame

# Initialize text-to-speech engine (pyttsx3)
engine = pyttsx3.init()

# OpenAI API Key
openai.api_key = 'your-openai-api-key'

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# Wake word
WAKE_WORD = "alexa"

# Function to speak text
from gtts import gTTS
import os
import tempfile

def speak(text):
    try:
        tts = gTTS(text , lang='ne')
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            os.system(f"mpv --quiet {fp.name}")
    except Exception as e:
        print(f"[Error] Couldn't speak: {e}")


# Function to listen to voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Sorry, I'm having trouble reaching the speech recognition service.")
        return command.lower()

# Function to process commands
def process_command(command):
    if WAKE_WORD in command:
        speak("Yes?")
        command = listen()

        # Web Browsing
        if 'google' in command:
            webbrowser.open("https://www.google.com")
        elif 'facebook' in command:
            webbrowser.open("https://www.facebook.com")
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
        elif 'linkedin' in command:
            webbrowser.open("https://www.linkedin.com")
        
        # Music Playback
        elif 'play music' in command:
            song_url = "http://path_to_music_file"  # Add your music URL here
            webbrowser.open(song_url)

        # Fetching News
        elif 'news' in command:
            fetch_news()

        # OpenAI GPT-3 Integration
        elif 'ask' in command:
            ask_openai(command)

        # Exit
        elif 'exit' in command:
            speak("Goodbye")
            exit()

        else:
            speak("Sorry, I didn't understand that command.")
        
# Function to fetch latest news
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your-news-api-key"
    response = requests.get(url).json()
    if response['status'] == 'ok':
        articles = response['articles']
        speak("Here are the top news headlines:")
        for article in articles[:5]:
            print(article['title'])
            speak(article['title'])

# Function to ask OpenAI
def ask_openai(command):
    prompt = command.replace("ask", "").strip()
    response = openai.Completion.create(
        model="text-davinci-003",  # Change to your preferred model
        prompt=prompt,
        max_tokens=100
    )
    answer = response.choices[0].text.strip()
    speak(answer)

# Main function
def main():
    speak("Initializing Jarvis....")
    while True:
        command = listen()
        if WAKE_WORD in command:
            process_command(command)

if __name__ == "__main__":
    main()

# from gtts import gTTS
# import os

# tts = gTTS("Hello Anupam, this is Jarvis.")
# tts.save("jarvis.mp3")
# os.system("mpv jarvis.mp3")  # or use 'play', 'ffplay', or 'vlc'


