
class MotivationEmbeddingLayer:
    def __init__(self):
        self.motivations = []

    def embed(self, decision, motive):
        self.motivations.append({
            "decision": decision,
            "motive": motive
        })

    def review_motives(self):
        return {
            "total": len(self.motivations),
            "distribution": self._motive_distribution()
        }

    def _motive_distribution(self):
        dist = {}
        for m in self.motivations:
            motive = m["motive"]
            dist[motive] = dist.get(motive, 0) + 1
        return dist
