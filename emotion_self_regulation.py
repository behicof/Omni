
class EmotionSelfRegulation:
    def __init__(self):
        self.state = {
            "stress": 0.3,
            "fatigue": 0.2,
            "excitement": 0.5
        }

    def update_state(self, result):
        if result == "success":
            self.state["excitement"] = min(1.0, self.state["excitement"] + 0.1)
            self.state["stress"] = max(0.0, self.state["stress"] - 0.1)
        elif result == "fail":
            self.state["stress"] = min(1.0, self.state["stress"] + 0.2)
            self.state["excitement"] = max(0.0, self.state["excitement"] - 0.1)
            self.state["fatigue"] = min(1.0, self.state["fatigue"] + 0.1)

    def get_state(self):
        return self.state

    def regulate(self):
        if self.state["stress"] > 0.7 or self.state["fatigue"] > 0.8:
            return "Pause"
        if self.state["excitement"] > 0.9:
            return "Calm down"
        return "Stable"
