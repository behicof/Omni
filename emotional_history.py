
class EmotionalHistorySimulator:
    def __init__(self):
        self.events = []

    def log_event(self, year, title, fear_level, greed_level):
        self.events.append({
            "year": year,
            "title": title,
            "fear": fear_level,
            "greed": greed_level
        })

    def replay(self):
        story = "Historical Emotional Replay:\n"
        for e in sorted(self.events, key=lambda x: x["year"]):
            tone = "Fearful" if e["fear"] > e["greed"] else "Greedy"
            story += f"{e['year']} - {e['title']} [{tone}] (Fear: {e['fear']}, Greed: {e['greed']})\n"
        return story

    def most_extreme_event(self):
        return max(self.events, key=lambda e: abs(e["fear"] - e["greed"]), default=None)
