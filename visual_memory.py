
class VisualPatternMemory:
    def __init__(self):
        self.memory_bank = []

    def store_pattern(self, pattern_name, metadata):
        self.memory_bank.append({
            "pattern": pattern_name,
            "metadata": metadata
        })

    def recall_similar(self, current_context):
        results = []
        for entry in self.memory_bank:
            if entry["pattern"] == current_context.get("pattern"):
                results.append(entry)
        return results

    def memory_summary(self):
        return [entry["pattern"] for entry in self.memory_bank]
