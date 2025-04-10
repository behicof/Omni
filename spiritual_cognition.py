
class SpiritualCognition:
    def __init__(self):
        self.anchors = {
            "purpose": None,
            "trust": 0.5,
            "resonance": [],
        }

    def define_purpose(self, description):
        self.anchors["purpose"] = description
        return f"Purpose set to: {description}"

    def register_resonance(self, moment):
        self.anchors["resonance"].append(moment)
        return f"Spiritual resonance recorded."

    def reflect_trust(self, market_state):
        if market_state == "volatile":
            self.anchors["trust"] = max(0.0, self.anchors["trust"] - 0.1)
        elif market_state == "stable":
            self.anchors["trust"] = min(1.0, self.anchors["trust"] + 0.1)
        return self.anchors["trust"]

    def introspect(self):
        return {
            "purpose": self.anchors["purpose"],
            "trust_level": self.anchors["trust"],
            "resonance_events": self.anchors["resonance"][-3:]
        }
