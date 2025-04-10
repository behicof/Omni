
class ScenarioBuilder:
    def __init__(self):
        self.historical_patterns = []

    def store_memory(self, pattern, outcome):
        self.historical_patterns.append({"pattern": pattern, "outcome": outcome})

    def match_scenario(self, current_pattern):
        for memory in self.historical_patterns:
            if memory["pattern"] == current_pattern:
                return {
                    "matched": True,
                    "predicted_outcome": memory["outcome"]
                }
        return {
            "matched": False,
            "predicted_outcome": "unknown"
        }

    def retrieve_all_memories(self):
        return self.historical_patterns
