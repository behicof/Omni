
class EmotionalSignalSensor:
    def __init__(self):
        self.recent_candles = []

    def feed_candle(self, open_price, close_price, high, low):
        candle = {
            "open": open_price,
            "close": close_price,
            "high": high,
            "low": low,
            "body": abs(close_price - open_price),
            "range": high - low
        }
        self.recent_candles.append(candle)
        if len(self.recent_candles) > 20:
            self.recent_candles.pop(0)

    def detect_emotional_spike(self):
        if not self.recent_candles:
            return "no_data"
        last = self.recent_candles[-1]
        if last["range"] > 10 and last["body"] < 2:
            return "indecision_spike"
        elif last["body"] > 5:
            return "strong_sentiment"
        return "normal"
