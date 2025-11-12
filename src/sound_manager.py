import pygame
import os

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

class SoundManager:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(os.path.dirname(current_dir), "assets", "sounds")

        self.sounds = {}
        sound_files = {
            "bgm": "bgm.wav",
            "start": "click.wav",
            "high_score": "high_score.wav",
            "botHigh_score": "botHigh_score.wav",
            "upLow_score": "upLow_score.wav",
            "low_score": "low_score.wav",
        }

        for sound_name, filename in sound_files.items():
            filepath = os.path.join(assets_dir, filename)
            if os.path.exists(filepath):
                try:
                    self.sounds[sound_name] = pygame.mixer.Sound(filepath)
                except Exception as e:
                    print(f"Could not load sound '{filename}': {e}")
            else:
                print(f"Sound file not found: {filepath}")

    def play(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            print(f"Sound '{sound_name}' tidak tersedia.")

    def stop(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()
