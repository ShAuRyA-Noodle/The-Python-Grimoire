"""
GUI Chat Automation with AI-Generated Responses
----------------------------------------------

This module monitors a specified chat window on the screen, detects whether the
latest message is sent by a target user, and automatically generates and sends
a context-aware reply using the OpenAI API.

Typical applications:
- Customer support automation
- Messaging productivity tools
- Personal assistant automation
- Social media response automation

Prerequisites:
- OPENAI_API_KEY environment variable configured
- Screen coordinates calibrated for the target chat interface
"""

import re
import time
import logging
import pyautogui
import pyperclip
from openai import OpenAI

# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------

# Screen coordinates for GUI interaction (must be calibrated manually)
CHROME_ICON = (1639, 1412)
SELECT_FROM = (972, 202)
SELECT_TO = (2213, 1278)
CLICK_CLEAR = (1994, 281)
INPUT_BOX = (1808, 1328)

TARGET_NAME = "Sandhu Ki Biwi"
POLL_INTERVAL_SECONDS = 5

# PyAutoGUI safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

# Initialize OpenAI client
client = OpenAI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------------------------------------------------------
# MESSAGE PARSING UTILITIES
# ---------------------------------------------------------------------

def is_last_message_from_sender(chat_log: str, sender_name: str) -> bool:
    """
    Determine whether the last parsed message in the chat log was sent
    by the specified sender.

    Args:
        chat_log: Full copied chat transcript.
        sender_name: Name of the sender to check.

    Returns:
        True if the last message belongs to the sender; otherwise False.
    """
    senders = re.findall(
        r"\[\d{4}-\d{2}-\d{2},.*?\]\s*(.*?):",
        chat_log
    )

    return bool(senders) and senders[-1].strip() == sender_name


def last_message_fingerprint(chat_log: str) -> str:
    """
    Generate a short fingerprint of the last message content.
    This is used to detect whether a new message has arrived and to
    prevent duplicate replies.

    Args:
        chat_log: Chat transcript text.

    Returns:
        Truncated string fingerprint of the last message.
    """
    matches = re.findall(
        r"\[\d{4}-\d{2}-\d{2},.*?\]\s*.*?:\s*(.*)$",
        chat_log,
        flags=re.DOTALL
    )

    return (matches[-1].strip() if matches else "")[:400]


# ---------------------------------------------------------------------
# AI RESPONSE GENERATION
# ---------------------------------------------------------------------

def generate_reply(history: str) -> str:
    """
    Generate an AI-driven reply using the OpenAI chat completion API.

    Args:
        history: Full chat history text used as conversation context.

    Returns:
        Generated response string.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a person named ShAuRyA who speaks Hindi/Punjabi "
                    "and a bit of Gujarati. Respond conversationally, "
                    "naturally, and return only the next chat message."
                )
            },
            {"role": "user", "content": history}
        ]
    )

    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------
# GUI AUTOMATION UTILITIES
# ---------------------------------------------------------------------

def copy_chat_region() -> str:
    """
    Select the chat transcript area using mouse automation,
    copy it to the clipboard, and return the copied text.
    """
    pyautogui.click(*CHROME_ICON)
    time.sleep(0.5)

    pyautogui.moveTo(*SELECT_FROM)
    pyautogui.dragTo(*SELECT_TO, duration=1.2, button="left")

    pyautogui.hotkey("command", "c")
    time.sleep(0.3)

    pyautogui.click(*CLICK_CLEAR)
    return pyperclip.paste()


def paste_and_send(message: str) -> None:
    """
    Paste the generated reply into the chat input box and send it.

    Args:
        message: Text message to send.
    """
    pyautogui.click(*INPUT_BOX)
    time.sleep(0.2)

    pyperclip.copy(message)
    pyautogui.hotkey("command", "v")

    time.sleep(0.2)
    pyautogui.press("enter")


# ---------------------------------------------------------------------
# MAIN BOT LOOP
# ---------------------------------------------------------------------

def main_loop():
    """
    Continuously monitor the chat window for new incoming messages
    from the target sender and respond automatically when detected.
    """
    logging.info("Auto-reply bot started. Move mouse to screen corner to abort.")

    last_fp = ""

    while True:
        time.sleep(POLL_INTERVAL_SECONDS)

        chat_history = copy_chat_region()
        if not chat_history.strip():
            continue

        current_fp = last_message_fingerprint(chat_history)
        if current_fp == last_fp:
            continue

        if is_last_message_from_sender(chat_history, TARGET_NAME):
            try:
                reply = generate_reply(chat_history)
                logging.info("Sending reply: %s", reply)
                paste_and_send(reply)
                last_fp = current_fp
            except Exception as exc:
                logging.error("Reply generation failed: %s", exc)
        else:
            last_fp = current_fp


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

if __name__ == "__main__":
    main_loop()
