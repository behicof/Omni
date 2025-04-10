
class EmotionInformedDecisionFilter:
    def __init__(self):
        self.history = []

    def evaluate(self, decision, mood, expected_profit):
        approved = False
        if mood in ["calm", "confident"] and expected_profit > 0:
            approved = True
        elif mood in ["anxious", "fearful"] and expected_profit > 50:
            approved = True
        self.history.append({
            "decision": decision,
            "mood": mood,
            "expected_profit": expected_profit,
            "approved": approved
        })
        return approved

    def summary(self):
        approved_count = sum(1 for h in self.history if h["approved"])
        return {
            "total_decisions": len(self.history),
            "approved": approved_count,
            "approval_rate": round(approved_count / len(self.history), 2) if self.history else 0
        }
