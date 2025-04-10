
class NeuroSensoryBridge:
    def __init__(self):
        self.signals = {
            "focus": 0.0,
            "stress": 0.0,
            "calm": 0.0,
            "engagement": 0.0
        }

    def receive_signal(self, signal_type, value):
        if signal_type in self.signals:
            self.signals[signal_type] = float(value)
        return self.interpret_state()

    def interpret_state(self):
        if self.signals["stress"] > 0.7:
            return "high_stress"
        if self.signals["focus"] > 0.7 and self.signals["engagement"] > 0.7:
            return "peak_performance"
        if self.signals["calm"] > 0.6:
            return "relaxed"
        return "neutral"
