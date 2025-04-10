
import random

class IntuitionEmulator:
    def __init__(self):
        self.memory = []
        self.bias_level = 0.3

    def embed_experience(self, snapshot):
        self.memory.append(snapshot)

    def infer_decision(self, current_context):
        # وزن‌دهی مبهم بر اساس تجربه و شدت تغییرات
        if not self.memory:
            return "WAIT"
        pattern_match = random.random() > self.bias_level
        if pattern_match:
            return "BUY" if random.random() > 0.5 else "SELL"
        return "WAIT"

    def adjust_bias(self, feedback):
        if feedback == "wrong":
            self.bias_level = min(1.0, self.bias_level + 0.1)
        elif feedback == "correct":
            self.bias_level = max(0.0, self.bias_level - 0.1)
