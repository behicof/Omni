
class ChartInsightExtractor:
    def __init__(self):
        self.chart_data = []

    def feed_data(self, prices):
        self.chart_data = prices[-20:]

    def extract_insight(self):
        if not self.chart_data or len(self.chart_data) < 5:
            return "insufficient data"
        highs = max(self.chart_data)
        lows = min(self.chart_data)
        range_size = highs - lows
        if range_size < 1:
            return "tight consolidation"
        elif self.chart_data[-1] > highs * 0.95:
            return "approaching resistance"
        elif self.chart_data[-1] < lows * 1.05:
            return "near support"
        return "neutral range"
