
class HybridStrategyLab:
    def __init__(self):
        self.components = {
            "technical": [],
            "statistical": [],
            "ml": [],
            "psychological": []
        }
        self.results = []

    def register_component(self, category, logic_fn):
        if category in self.components:
            self.components[category].append(logic_fn)

    def test_hybrid(self, data_input):
        combined_result = {}
        for cat, funcs in self.components.items():
            cat_result = [f(data_input) for f in funcs]
            combined_result[cat] = cat_result
        self.results.append(combined_result)
        return combined_result

    def best_performer(self):
        return max(self.results[-1].items(), key=lambda x: sum(map(float, x[1])), default=("none", []))
