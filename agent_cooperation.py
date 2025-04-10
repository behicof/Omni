
class AgentCooperationLayer:
    def __init__(self):
        self.agents = {}
        self.coop_log = []

    def register_agent(self, name):
        self.agents[name] = {"shared_data": [], "decisions": []}

    def share_decision(self, from_agent, decision):
        for agent in self.agents:
            if agent != from_agent:
                self.agents[agent]["shared_data"].append(decision)
        self.coop_log.append((from_agent, decision))

    def get_agent_view(self, name):
        return self.agents.get(name, {}).get("shared_data", [])

    def summarize_network(self):
        return {
            "total_agents": len(self.agents),
            "messages_shared": len(self.coop_log)
        }
