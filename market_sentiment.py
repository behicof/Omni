
from textblob import TextBlob

class MarketSentimentAnalyzer:
    def __init__(self):
        self.history = []

    def analyze(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        label = self.label_sentiment(polarity)
        self.history.append({"text": text, "polarity": polarity, "label": label})
        return {"label": label, "score": polarity}

    def label_sentiment(self, score):
        if score > 0.2:
            return "Bullish"
        elif score < -0.2:
            return "Bearish"
        return "Neutral"

    def get_history(self):
        return self.history
