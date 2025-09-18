from collections import defaultdict

class Stats:
    def __init__(self):
        self.total_requests = 0
        self.class_distribution = defaultdict(int)
        self.feedback_counts = {"positive": 0, "negative": 0}
        self.latencies = []

    def record_request(self, cls: str, latency: int):
        self.total_requests += 1
        self.class_distribution[cls] += 1
        self.latencies.append(latency)

    def record_feedback(self, positive: bool):
        if positive:
            self.feedback_counts["positive"] += 1
        else:
            self.feedback_counts["negative"] += 1

    def get_metrics(self):
        if self.latencies:
            avg = sum(self.latencies) / len(self.latencies)
            p95 = sorted(self.latencies)[int(0.95 * len(self.latencies)) - 1]
        else:
            avg, p95 = 0, 0
        return {
            "total_requests": self.total_requests,
            "class_distribution": dict(self.class_distribution),
            "feedback_counts": self.feedback_counts,
            "latency": {"avg_ms": avg, "p95_ms": p95}
        }

# 👇 Important: define global instance here
stats = Stats()
