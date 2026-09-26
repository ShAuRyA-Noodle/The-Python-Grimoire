import unittest
from unittest.mock import patch

import Sheet_02 as assistant
from Sheet_03 import get_song_url


class VoiceAssistantTests(unittest.TestCase):
    @patch.object(assistant.webbrowser, "open")
    def test_play_multiword_song(self, open_browser):
        assistant.process_command("Play lose my mind")
        open_browser.assert_called_once_with(get_song_url("lose my mind"))

    @patch.object(assistant, "speak")
    @patch.object(assistant.webbrowser, "open")
    def test_unknown_song_does_not_open_browser(self, open_browser, speak):
        assistant.process_command("play unknown song")
        open_browser.assert_not_called()
        speak.assert_called_once()

    @patch.object(assistant.requests, "get")
    @patch.object(assistant, "speak")
    def test_news_without_key_skips_request(self, speak, get):
        with patch.object(assistant, "NEWS_API_KEY", None):
            assistant.process_command("news")
        get.assert_not_called()
        speak.assert_called_once()

    @patch.object(assistant, "OpenAI")
    def test_openai_client_is_created_when_needed(self, client_type):
        client_type.return_value.chat.completions.create.return_value.choices = [
            type("Choice", (), {"message": type("Message", (), {"content": "Hello"})()})()
        ]
        self.assertEqual(assistant.ai_process("hello"), "Hello")
        client_type.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
