from pathlib import Path
import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets" / "sounds"

class SoundManager:
    def __init__(self):
        self.sounds = {}
        sound_files = {
            "bgm": "bgm.wav",
            "start": "click.wav",
            "high_score": "high_score.wav",
            "botHigh_score": "botHigh_score.wav",
            "upLow_score": "upLow_score.wav",
            "low_score": "low_score.wav",
        }

        for name, filename in sound_files.items():
            path = ASSETS_DIR / filename
            if path.exists():
                self.sounds[name] = pygame.mixer.Sound(str(path))
            else:
                print(f"[WARNING] File sound tidak ditemukan: {path}")

    def play(self, sound_name):
        """Mainkan suara berdasarkan nama yang terdaftar."""
        sound = self.sounds.get(sound_name)
        if sound:
            sound.play()
        else:
            print(f"[WARNING] Sound '{sound_name}' tidak ditemukan atau belum dimuat.")

    def stop(self, sound_name):
        """Hentikan suara tertentu jika sedang dimainkan."""
        sound = self.sounds.get(sound_name)
        if sound:
            sound.stop()
        else:
            print(f"[WARNING] Sound '{sound_name}' tidak ditemukan atau belum dimuat.")
