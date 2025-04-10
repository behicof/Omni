
class ExperientialProfitModel:
    def __init__(self):
        self.journal = []

    def log_trade(self, decision, result, context):
        self.journal.append({
            "decision": decision,
            "profit": result,
            "context": context
        })

    def analyze_experience(self):
        if not self.journal:
            return {"message": "No data"}
        profitable = [entry for entry in self.journal if entry["profit"] > 0]
        avg_profit = round(sum(e["profit"] for e in profitable) / len(profitable), 2) if profitable else 0.0
        return {
            "total_trades": len(self.journal),
            "profitable_trades": len(profitable),
            "average_profit": avg_profit
        }

    def last_experience(self):
        return self.journal[-1] if self.journal else None
