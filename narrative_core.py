
class NarrativeCore:
    def __init__(self):
        self.timeline = []

    def add_event(self, title, impact, emotion):
        self.timeline.append({
            "title": title,
            "impact": impact,
            "emotion": emotion
        })

    def build_narrative(self):
        story = "The Market Saga Begins...

"
        for event in self.timeline:
            story += f"- {event['title']} | Impact: {event['impact']} | Emotion: {event['emotion']}
"
        story += "\n...To be continued."
        return story

    def clear_narrative(self):
        self.timeline = []
