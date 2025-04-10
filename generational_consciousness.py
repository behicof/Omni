
class GenerationalConsciousness:
    def __init__(self):
        self.generation_models = {
            "Boomers": {"risk_aversion": 0.8, "reaction_speed": "slow"},
            "GenX": {"risk_aversion": 0.6, "reaction_speed": "medium"},
            "Millennials": {"risk_aversion": 0.4, "reaction_speed": "fast"},
            "GenZ": {"risk_aversion": 0.3, "reaction_speed": "hyperfast"}
        }

    def analyze_decision_style(self, generation):
        return self.generation_models.get(generation, "Unknown generation")

    def compare_generations(self):
        return {
            gen: self.generation_models[gen]["risk_aversion"]
            for gen in self.generation_models
        }
