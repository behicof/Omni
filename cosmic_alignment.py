
import math
from datetime import datetime

class CosmicAlignment:
    def __init__(self):
        self.alignment_score = 0.0

    def calculate_fibonacci_ratio(self, value1, value2):
        try:
            return round(value1 / value2, 3)
        except ZeroDivisionError:
            return 0.0

    def evaluate_alignment(self, market_value, solar_cycle_value):
        fib_ratio = self.calculate_fibonacci_ratio(market_value, solar_cycle_value)
        harmony = abs(fib_ratio - 1.618)
        self.alignment_score = max(0.0, 1.0 - harmony)
        return {
            "fib_ratio": fib_ratio,
            "alignment_score": round(self.alignment_score, 3)
        }

    def is_aligned(self):
        return self.alignment_score >= 0.8
