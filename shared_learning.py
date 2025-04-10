
class SharedLearningHub:
    def __init__(self):
        self.knowledge_base = {}

    def log_result(self, agent_name, strategy_name, profit):
        key = (agent_name, strategy_name)
        if key not in self.knowledge_base:
            self.knowledge_base[key] = []
        self.knowledge_base[key].append(profit)

    def get_best_strategies(self):
        avg_profits = {
            k: sum(v) / len(v) for k, v in self.knowledge_base.items() if v
        }
        sorted_strategies = sorted(avg_profits.items(), key=lambda x: x[1], reverse=True)
        return sorted_strategies[:3]

    def suggest_to_all(self):
        best = self.get_best_strategies()
        return [f"Use {strategy} from {agent}" for (agent, strategy), _ in best]
