
class EmotionalStateTracker:
    def __init__(self):
        self.states = []

    def log_state(self, timestamp, mood, intensity):
        self.states.append({
            "time": timestamp,
            "mood": mood,
            "intensity": intensity
        })

    def current_state(self):
        return self.states[-1] if self.states else None

    def mood_distribution(self):
        dist = {}
        for s in self.states:
            mood = s["mood"]
            dist[mood] = dist.get(mood, 0) + 1
        return dist
