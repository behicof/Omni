
class ScenarioEngine:
    def __init__(self):
        self.scenarios = {}

    def define_scenario(self, name, context):
        self.scenarios[name] = context

    def get_scenario(self, name):
        return self.scenarios.get(name)

    def list_scenarios(self):
        return list(self.scenarios.keys())

    def simulate(self, name):
        scenario = self.get_scenario(name)
        if not scenario:
            return "Scenario not found."
        return f"Simulating scenario: {name} with context {scenario}"
