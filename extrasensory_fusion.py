
class ExtrasensoryFusion:
    def __init__(self):
        self.channels = {
            "emotion": [],
            "text": [],
            "visual": [],
            "audio": [],
            "history": []
        }

    def feed(self, channel, data):
        if channel in self.channels:
            self.channels[channel].append(data)

    def fuse(self):
        fusion_score = 0.0
        if self.channels["emotion"]:
            fusion_score += 0.2
        if self.channels["text"]:
            fusion_score += 0.2
        if self.channels["visual"]:
            fusion_score += 0.2
        if self.channels["audio"]:
            fusion_score += 0.2
        if self.channels["history"]:
            fusion_score += 0.2
        return {"fusion_score": fusion_score, "status": self.interpret(fusion_score)}

    def interpret(self, score):
        if score >= 0.8:
            return "Strong Intuition"
        elif score >= 0.5:
            return "Moderate Signal"
        return "Weak Insight"
