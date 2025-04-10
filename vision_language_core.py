
from textblob import TextBlob

class VisionLanguageCore:
    def __init__(self):
        self.context_memory = []

    def interpret_text(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        return {"text": text, "sentiment": sentiment}

    def interpret_chart(self, candle_data):
        # ساده‌سازی: تشخیص روند ساده
        closes = [c["close"] for c in candle_data[-5:]]
        if closes[-1] > closes[0]:
            trend = "uptrend"
        elif closes[-1] < closes[0]:
            trend = "downtrend"
        else:
            trend = "sideways"
        return {"trend": trend, "closes": closes}

    def combine_insights(self, text, candle_data):
        t_analysis = self.interpret_text(text)
        c_analysis = self.interpret_chart(candle_data)
        self.context_memory.append((t_analysis, c_analysis))
        return {
            "text_sentiment": t_analysis["sentiment"],
            "chart_trend": c_analysis["trend"],
            "conclusion": self.summarize(t_analysis["sentiment"], c_analysis["trend"])
        }

    def summarize(self, sentiment, trend):
        if sentiment > 0.2 and trend == "uptrend":
            return "Bullish Alignment"
        elif sentiment < -0.2 and trend == "downtrend":
            return "Bearish Confirmation"
        return "Mixed or Unclear"
