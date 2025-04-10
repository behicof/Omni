
import random

class InnovationGenerator:
    def __init__(self):
        self.ideas = []

    def generate_trading_strategy(self):
        indicators = ['RSI', 'MACD', 'BollingerBands', 'MovingAverage']
        rules = ['crosses above', 'crosses below', 'diverges', 'converges']
        idea = {
            "indicator": random.choice(indicators),
            "rule": random.choice(rules),
            "logic": f"If {random.choice(indicators)} {random.choice(rules)} {random.choice(indicators)}, then signal."
        }
        self.ideas.append(idea)
        return idea

    def list_ideas(self):
        return self.ideas
