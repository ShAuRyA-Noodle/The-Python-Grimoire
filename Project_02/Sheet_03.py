"""
Music Library Module

Description
-----------
This module stores a mapping between voice-command song keywords and
their corresponding playback URLs. It is designed to be imported by
the Jarvis assistant so that voice commands such as:

    "Play vertigo"

can automatically open the associated streaming link.

Usage
-----
from music_library import MUSIC_LIBRARY
webbrowser.open(MUSIC_LIBRARY["vertigo"])
"""

from typing import Dict

# Dictionary mapping song command keywords to streaming URLs
MUSIC_LIBRARY: Dict[str, str] = {
    "vertigo": (
        "https://www.youtube.com/watch?v=nkm_sz5J8aI"
        "&list=RDnkm_sz5J8aI&start_radio=1&ab_channel=TomFrane-Topic"
    ),
    "lose my mind": (
        "https://www.youtube.com/watch?v=WWEs82u37Mw"
        "&list=RDWWEs82u37Mw&start_radio=1&ab_channel=DonToliver"
    ),
}


def get_song_url(song_name: str) -> str | None:
    """
    Retrieve the URL associated with a given song keyword.

    Args:
        song_name (str): Keyword identifying the song.

    Returns:
        str | None: URL of the song if found, otherwise None.
    """
    return MUSIC_LIBRARY.get(song_name.lower())
