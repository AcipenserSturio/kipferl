"""
Handles sound output.
"""

from pathlib import Path
from threading import Thread

from playsound import playsound

from ..assets.assets import read_defines

def play(sound):
    """
    Play a WAV file asynchronously.
    """
    if not sound:
        return
    if not read_defines()["use_sound"]:
        return
    thread = Thread(target=_play, args=(sound,))
    thread.start()

def _play(sound):
    playsound(Path().cwd() / "assets" / "sound" / sound, block=True)
