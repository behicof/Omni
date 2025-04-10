
class DecisionPlotEngine:
    def __init__(self):
        self.chapters = []

    def add_decision(self, decision_type, context, result):
        stage = "inciting action" if decision_type == "entry" else "climax" if result == "profit" else "crisis"
        self.chapters.append({
            "stage": stage,
            "context": context,
            "result": result
        })

    def structure_plot(self):
        plot = "Trading Story Arc:\n"
        for chapter in self.chapters:
            plot += f"* {chapter['stage'].title()}: {chapter['context']} -> {chapter['result']}\n"
        return plot

    def reset_plot(self):
        self.chapters = []
