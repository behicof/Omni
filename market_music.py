
import numpy as np
import wave

class MarketMusic:
    def __init__(self, framerate=44100):
        self.framerate = framerate

    def tone(self, frequency, duration=0.5):
        t = np.linspace(0, duration, int(self.framerate * duration), endpoint=False)
        wave_data = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
        return wave_data

    def generate_sequence(self, market_pattern, output_file="market_melody.wav"):
        mapping = {
            "bullish": [440, 660, 880],
            "bearish": [330, 220, 165],
            "neutral": [440, 440, 440]
        }
        notes = mapping.get(market_pattern, [440])
        song = np.concatenate([self.tone(f, 0.3) for f in notes])
        with wave.open(output_file, "w") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(self.framerate)
            f.writeframes(song.tobytes())
        return output_file
