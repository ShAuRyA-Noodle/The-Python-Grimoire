"""
Voice-Controlled AI Assistant (Jarvis)

Description
-----------
This module implements a voice-controlled personal assistant capable of:
- Listening for a wake word ("Jarvis")
- Processing spoken commands
- Opening websites
- Playing music
- Reading news headlines
- Answering general questions using an LLM

Concepts Demonstrated
---------------------
- Speech recognition (SpeechRecognition)
- Text-to-speech (gTTS / pyttsx3)
- API integrations (OpenAI, NewsAPI)
- Event loops and command routing
- Audio playback (pygame)
- Exception handling and runtime robustness

Security Note
-------------
The OpenAI API key must be stored in an environment variable:
    export OPENAI_API_KEY="your_key_here"
"""

# ─────────────────────────────
# Imports
# ─────────────────────────────
import os
import webbrowser
import requests
import pygame
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from openai import OpenAI
import music_library


# ─────────────────────────────
# Initialization
# ─────────────────────────────
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"

client = OpenAI()  # API key automatically read from environment variable


# ─────────────────────────────
# Speech Utilities
# ─────────────────────────────
def speak_offline(text: str) -> None:
    """
    Speak text using offline TTS (pyttsx3).
    Faster but less natural sounding.
    """
    tts_engine.say(text)
    tts_engine.runAndWait()


def speak(text: str) -> None:
    """
    Speak text using Google TTS and pygame playback.
    Produces more natural speech but requires internet access.
    """
    filename = "temp.mp3"
    tts = gTTS(text)
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(filename)


# ─────────────────────────────
# AI Processing
# ─────────────────────────────
def ai_process(command: str) -> str:
    """
    Send a command to the OpenAI model and return its response.
    """
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful assistant. Respond concisely."},
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message.content


# ─────────────────────────────
# Command Processing
# ─────────────────────────────
def process_command(command: str) -> None:
    """
    Route a recognized voice command to the appropriate action.
    """
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    elif command.startswith("play"):
        song = command.split(" ")[1]
        webbrowser.open(musicLibrary.music[song])

    elif "news" in command:
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        )

        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:
                speak(article["title"])

    else:
        output = ai_process(command)
        speak(output)


# ─────────────────────────────
# Main Execution Loop
# ─────────────────────────────
def main() -> None:
    """
    Main assistant loop:
    1. Listen continuously for wake word ("Jarvis")
    2. Capture command
    3. Execute requested action
    """
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                process_command(command)

        except Exception as error:
            print(f"Runtime error: {error}")


# ─────────────────────────────
# Entry Point
# ─────────────────────────────
if __name__ == "__main__":
    main()
