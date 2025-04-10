
class SharedLearningMatrix:
    def __init__(self):
        self.models = {}

    def upload_model(self, agent_id, model_data):
        self.models[agent_id] = model_data

    def aggregate_insights(self):
        insights = []
        for model in self.models.values():
            insights.append(model.get("insight", ""))
        return list(set(insights))  # یکتا‌سازی نتایج

    def suggest_improvements(self):
        return f"{len(self.models)} agents contributed. Combined insight: {self.aggregate_insights()}"
