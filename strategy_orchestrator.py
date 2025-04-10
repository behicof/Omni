
class LiveStrategyOrchestrator:
    def __init__(self):
        self.strategies = {}
        self.active_strategy = None
        self.performance_log = {}

    def register_strategy(self, name, logic_function):
        self.strategies[name] = logic_function
        self.performance_log[name] = []

    def execute(self, market_data):
        if not self.active_strategy:
            self.active_strategy = list(self.strategies.keys())[0]
        logic = self.strategies[self.active_strategy]
        decision = logic(market_data)
        self.performance_log[self.active_strategy].append(decision.get("profit", 0))
        return decision

    def switch_strategy(self):
        avg_performance = {
            name: sum(log[-5:]) / len(log[-5:]) if log[-5:] else 0
            for name, log in self.performance_log.items()
        }
        self.active_strategy = max(avg_performance, key=avg_performance.get)
        return self.active_strategy
