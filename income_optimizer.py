
class DynamicIncomeOptimizer:
    def __init__(self):
        self.history = []

    def evaluate_trade(self, price, volume, direction, risk_score):
        multiplier = 1.5 if direction == "buy" else 1.3
        expected_profit = round(price * volume * multiplier * (1 - risk_score), 2)
        self.history.append({
            "price": price,
            "volume": volume,
            "direction": direction,
            "risk_score": risk_score,
            "expected_profit": expected_profit
        })
        return expected_profit

    def adjust_volume(self, balance, risk_score):
        base_volume = balance * (0.02 if risk_score < 0.5 else 0.01)
        return round(base_volume / 100, 2)  # فرض بر قیمت متوسط 100

    def latest_optimization(self):
        return self.history[-1] if self.history else None
