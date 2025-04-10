
import random

class FuturescapeDesigner:
    def __init__(self):
        self.futures = []

    def generate_futures(self, current_price):
        self.futures = []
        for i in range(3):
            direction = random.choice(["up", "down", "sideways"])
            shift = random.uniform(0.01, 0.1) * current_price
            if direction == "up":
                future_price = current_price + shift
            elif direction == "down":
                future_price = current_price - shift
            else:
                future_price = current_price
            self.futures.append({
                "path": direction,
                "price_projection": round(future_price, 2),
                "probability": round(random.uniform(0.25, 0.5), 2)
            })
        return self.futures

    def summarize_outlook(self):
        summary = {"up": 0, "down": 0, "sideways": 0}
        for f in self.futures:
            summary[f["path"]] += f["probability"]
        return summary
