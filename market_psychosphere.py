
class MarketPsychosphere:
    def __init__(self):
        self.mental_energy = {
            "fear": 0.0,
            "greed": 0.0,
            "uncertainty": 0.0,
            "confidence": 0.0
        }

    def absorb_data(self, sentiment_data):
        for key in self.mental_energy:
            self.mental_energy[key] = sentiment_data.get(key, self.mental_energy[key])

    def summarize_state(self):
        dominant = max(self.mental_energy, key=self.mental_energy.get)
        total_energy = round(sum(self.mental_energy.values()), 3)
        return {
            "dominant_emotion": dominant,
            "total_energy": total_energy,
            "map": self.mental_energy
        }

    def forecast_shift(self):
        if self.mental_energy["fear"] > 0.6:
            return "Market likely to pull back (protective mode)"
        if self.mental_energy["greed"] > 0.6:
            return "Market overheating (possible correction)"
        return "Stable to volatile conditions"
