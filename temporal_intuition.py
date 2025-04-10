
import numpy as np

class TemporalIntuition:
    def __init__(self):
        self.history_window = []

    def feed_data(self, prices):
        self.history_window = prices[-30:]  # آخرین ۳۰ نقطه زمانی

    def project_future(self):
        if not self.history_window:
            return "No data"
        diffs = np.diff(self.history_window)
        avg_change = np.mean(diffs)
        projection = [self.history_window[-1] + avg_change * i for i in range(1, 6)]
        return {
            "intuition_curve": projection,
            "trend": "up" if avg_change > 0 else "down" if avg_change < 0 else "flat"
        }
