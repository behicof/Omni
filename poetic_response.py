
import random

class PoeticResponse:
    def __init__(self):
        self.templates = {
            "bullish": [
                "در طلیعه طلوع طلا، امید با نغمه صعود می‌رقصد.",
                "بازار به آغوش گرمای اعتماد بازگشته است.",
                "نسیم صعود در شاخه‌های قیمت جاری‌ست."
            ],
            "bearish": [
                "ابرهای شک، آسمان بازار را تیره کرده‌اند.",
                "باد سرد فروش، برگ‌های سود را می‌رباید.",
                "سکوتی سنگین، دره‌ی ضرر را در آغوش گرفته است."
            ],
            "neutral": [
                "بازار در خواب آرام، منتظر بیداری‌ست.",
                "نبض قیمت بی‌صدا می‌تپد، بی‌آنکه فریادی باشد.",
                "هاله‌ای از تردید، سکوتی از انتظار."
            ]
        }

    def generate(self, sentiment):
        return random.choice(self.templates.get(sentiment, self.templates["neutral"]))
