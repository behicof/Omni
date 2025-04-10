
import matplotlib.pyplot as plt
import numpy as np

class VisualMarket:
    def __init__(self):
        pass

    def generate_pattern(self, market_state, save_path="market_visual.png"):
        x = np.linspace(0, 10, 500)
        if market_state == "bullish":
            y = np.sin(x) * np.exp(0.05 * x)
            color = "green"
        elif market_state == "bearish":
            y = -np.sin(x) * np.exp(0.05 * x)
            color = "red"
        else:
            y = np.sin(x)
            color = "gray"

        plt.figure(figsize=(8, 4))
        plt.plot(x, y, color=color, linewidth=2)
        plt.title(f"Market Mood: {market_state}", fontsize=14)
        plt.axis("off")
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        return save_path
