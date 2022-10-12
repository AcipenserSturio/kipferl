from playsound import playsound

def play(sound):
    if not sound:
        return
    playsound(f"assets/sound/{sound}", False)
