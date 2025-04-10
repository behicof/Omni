
class GlobalDataSync:
    def __init__(self):
        self.sources = {
            "gold": [],
            "stocks": [],
            "crypto": [],
            "energy": []
        }

    def feed(self, market, data_point):
        if market in self.sources:
            self.sources[market].append(data_point)

    def get_latest(self, market):
        return self.sources[market][-1] if self.sources[market] else None

    def summarize(self):
        return {market: len(data) for market, data in self.sources.items()}
