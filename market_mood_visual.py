
import random

class LiveMarketMoodVisualizer:
    def __init__(self):
        self.history = []

    def analyze(self, price_data):
        mood = "neutral"
        if len(price_data) >= 3:
            delta = price_data[-1] - price_data[-3]
            if delta > 5:
                mood = "greedy"
            elif delta < -5:
                mood = "fearful"
            elif abs(delta) < 1:
                mood = "apathetic"
        self.history.append(mood)
        return mood

    def mood_summary(self):
        return {m: self.history.count(m) for m in set(self.history)}
