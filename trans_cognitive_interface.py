
class TransCognitiveInterface:
    def __init__(self):
        self.symbol_map = {}
        self.conceptual_path = []

    def ingest_thought_symbol(self, symbol, weight=1.0):
        if symbol not in self.symbol_map:
            self.symbol_map[symbol] = weight
        else:
            self.symbol_map[symbol] += weight
        self.conceptual_path.append(symbol)

    def interpret_path(self):
        dominant = max(self.symbol_map, key=self.symbol_map.get, default="unknown")
        length = len(self.conceptual_path)
        return {
            "dominant_concept": dominant,
            "path_length": length,
            "path": self.conceptual_path[-5:]
        }

    def clear_path(self):
        self.symbol_map = {}
        self.conceptual_path = []
