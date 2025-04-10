
import numpy as np

class VisualPerceptionModule:
    def __init__(self):
        self.recent_prices = []

    def observe(self, price):
        self.recent_prices.append(price)
        if len(self.recent_prices) > 50:
            self.recent_prices.pop(0)

    def detect_pattern(self):
        if len(self.recent_prices) < 5:
            return "insufficient data"
        window = self.recent_prices[-5:]
        if window == sorted(window):
            return "ascending"
        elif window == sorted(window, reverse=True):
            return "descending"
        elif abs(window[-1] - window[0]) < 1.0:
            return "sideways"
        return "volatile"

    def last_pattern(self):
        return self.detect_pattern()
