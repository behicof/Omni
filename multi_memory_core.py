
class MultiModalMemoryCore:
    def __init__(self):
        self.visual_memory = []
        self.text_memory = []
        self.numeric_memory = []
        self.behavior_memory = []

    def store_experience(self, modality, content):
        if modality == "visual":
            self.visual_memory.append(content)
        elif modality == "text":
            self.text_memory.append(content)
        elif modality == "numeric":
            self.numeric_memory.append(content)
        elif modality == "behavior":
            self.behavior_memory.append(content)

    def retrieve_context(self, modality):
        if modality == "visual":
            return self.visual_memory[-5:]
        elif modality == "text":
            return self.text_memory[-5:]
        elif modality == "numeric":
            return self.numeric_memory[-5:]
        elif modality == "behavior":
            return self.behavior_memory[-5:]
        return []
