
class PatternMemoryEngine:
    def __init__(self):
        self.pattern_library = []

    def save_pattern(self, pattern_name, structure):
        self.pattern_library.append({
            "name": pattern_name,
            "structure": structure
        })

    def match_pattern(self, current_structure):
        for p in self.pattern_library:
            if p["structure"] == current_structure:
                return {
                    "matched": True,
                    "name": p["name"]
                }
        return {
            "matched": False,
            "name": None
        }

    def library_summary(self):
        return [p["name"] for p in self.pattern_library]
