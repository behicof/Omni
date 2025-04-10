
class PerformanceAlignmentEngine:
    def __init__(self):
        self.records = []

    def align(self, experience, motive, result):
        alignment_score = 1.0 if experience > 0 and motive in ["growth", "clarity"] else 0.5
        self.records.append({
            "experience": experience,
            "motive": motive,
            "profit": result,
            "alignment_score": round(alignment_score, 2)
        })

    def get_summary(self):
        return {
            "total_aligned": len(self.records),
            "average_alignment": round(
                sum(r["alignment_score"] for r in self.records) / len(self.records), 2
            ) if self.records else 0
        }
