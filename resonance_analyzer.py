
import math

class ResonanceAnalyzer:
    def __init__(self):
        self.sources = {
            "market": [],
            "user_mind": [],
            "cosmic_pattern": []
        }

    def feed(self, source, frequency):
        if source in self.sources:
            self.sources[source].append(frequency)

    def measure_harmony(self):
        harmonics = []
        for source, values in self.sources.items():
            if not values:
                harmonics.append(0)
            else:
                avg = sum(values) / len(values)
                harmonics.append(avg)
        try:
            diff1 = abs(harmonics[0] - harmonics[1])
            diff2 = abs(harmonics[1] - harmonics[2])
            diff3 = abs(harmonics[2] - harmonics[0])
            avg_diff = (diff1 + diff2 + diff3) / 3
            score = max(0.0, 1.0 - avg_diff / 10)  # نرمال‌سازی
        except:
            score = 0.0
        return {
            "resonance_score": round(score, 3),
            "harmonic_values": harmonics
        }

    def is_resonant(self):
        return self.measure_harmony()["resonance_score"] >= 0.85
