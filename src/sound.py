from pathlib import Path

from playsound import playsound

def play(sound):
    if not sound:
        return
    playsound(Path().cwd() / "assets" / "sound" / sound, False)
