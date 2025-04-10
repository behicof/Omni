
class CollectiveIntuition:
    def __init__(self):
        self.signals = []

    def share_signal(self, agent_id, intuition_data):
        self.signals.append({"agent": agent_id, "intuition": intuition_data})

    def align(self):
        if not self.signals:
            return "No signals received."
        tally = {}
        for entry in self.signals:
            signal = entry["intuition"]
            tally[signal] = tally.get(signal, 0) + 1
        dominant = max(tally.items(), key=lambda x: x[1])[0]
        return {"dominant_intuition": dominant, "distribution": tally}

    def reset(self):
        self.signals = []
        return "Collective signals cleared."
