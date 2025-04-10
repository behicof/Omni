
class ExternalAIInterface:
    def __init__(self):
        self.sources = []

    def connect_api(self, name, endpoint):
        self.sources.append({"name": name, "endpoint": endpoint})
        return f"Connected to external AI source: {name}"

    def send_query(self, name, query):
        return f"[Simulated] Query sent to {name}: '{query}'"

    def list_sources(self):
        return self.sources
