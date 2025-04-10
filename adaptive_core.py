
class AdaptiveIntelligenceCore:
    def __init__(self):
        self.memory = []
        self.parameters = {"threshold": 0.5, "multiplier": 1.0}

    def observe(self, outcome):
        self.memory.append(outcome)
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]
        self.adjust()

    def adjust(self):
        profits = [o["profit"] for o in self.memory if "profit" in o]
        if profits:
            avg_profit = sum(profits) / len(profits)
            self.parameters["multiplier"] = 1.0 + (avg_profit / 1000)
            self.parameters["threshold"] = 0.5 + (avg_profit / 2000)

    def get_params(self):
        return self.parameters
