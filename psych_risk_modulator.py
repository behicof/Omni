
class PsychologicalRiskModulator:
    def __init__(self):
        self.mood_risk_map = {
            "calm": 0.02,
            "confident": 0.03,
            "anxious": 0.01,
            "fearful": 0.005,
            "greedy": 0.015
        }

    def get_risk_limit(self, mood):
        return self.mood_risk_map.get(mood, 0.01)

    def adjust_position_size(self, balance, mood):
        risk_limit = self.get_risk_limit(mood)
        return round(balance * risk_limit, 2)
