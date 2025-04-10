
class OmniAvatar:
    def __init__(self):
        self.emotion = "neutral"
        self.expression = "idle"
        self.message = ""

    def express(self, emotion, message=""):
        self.emotion = emotion
        self.expression = self.map_emotion_to_expression(emotion)
        self.message = message
        return f"[{self.expression}] {self.message}"

    def map_emotion_to_expression(self, emotion):
        mapping = {
            "neutral": "idle",
            "happy": "smile",
            "fear": "worried",
            "confident": "bold",
            "angry": "serious"
        }
        return mapping.get(emotion, "idle")

    def current_state(self):
        return {
            "emotion": self.emotion,
            "expression": self.expression,
            "message": self.message
        }
