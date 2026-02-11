"""
text_to_speech.py
-----------------

This module demonstrates basic offline text-to-speech (TTS) synthesis using
the `pyttsx3` library. Unlike cloud-based solutions, pyttsx3 operates locally
and does not require an internet connection.

Typical use cases:
- Accessibility tools
- Voice assistants
- Notification systems
- Educational software
"""

import pyttsx3


# ---------------------------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------------------------

def initialize_engine() -> pyttsx3.Engine:
    """
    Initialize and return a configured pyttsx3 text-to-speech engine.

    Returns:
        Configured pyttsx3 engine instance.
    """
    engine = pyttsx3.init()

    # Optional configuration (can be customized)
    engine.setProperty("rate", 170)   # Speech speed
    engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

    return engine


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def speak_text(engine: pyttsx3.Engine, text: str) -> None:
    """
    Convert text to speech using the provided TTS engine.

    Args:
        engine: Initialized pyttsx3 engine
        text: Text string to speak
    """
    engine.say(text)
    engine.runAndWait()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    """
    Main execution function for speaking a sample message.
    """
    engine = initialize_engine()
    speak_text(engine, "Hey, I am good.")


if __name__ == "__main__":
    main()
