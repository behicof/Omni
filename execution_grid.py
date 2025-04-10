
class SynchronizedExecutionGrid:
    def __init__(self):
        self.tasks = []
        self.executions = []

    def assign_task(self, agent, symbol, action, volume):
        task = {
            "agent": agent,
            "symbol": symbol,
            "action": action,
            "volume": volume
        }
        self.tasks.append(task)

    def execute_all(self):
        for task in self.tasks:
            execution = {
                "agent": task["agent"],
                "symbol": task["symbol"],
                "action": task["action"],
                "volume": task["volume"],
                "status": "executed"
            }
            self.executions.append(execution)
        self.tasks = []
        return self.executions

    def summary(self):
        return {
            "executed_trades": len(self.executions),
            "last_execution": self.executions[-1] if self.executions else None
        }
