from pathlib import Path
from threading import Thread

from playsound import playsound

def play(sound):
    if not sound:
        return
    thread = Thread(target=_play, args=(sound,))
    thread.start()

def _play(sound):
    playsound(Path().cwd() / "assets" / "sound" / sound, block=True)
