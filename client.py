import math

class HdrHistogram:
    """
    HdrHistogram Percentile Estimator.
    Maintains count distributions across integer value domains.
    """
    def __init__(self, highest_trackable_value=10000, precision=2):
        self.max_val = highest_trackable_value
        self.counts = [0] * (highest_trackable_value + 1)
        self.total_count = 0

    def record_value(self, value):
        v = min(self.max_val, max(0, int(value)))
        self.counts[v] += 1
        self.total_count += 1

    def get_value_at_percentile(self, percentile):
        if self.total_count == 0:
            return 0
        threshold = math.ceil((percentile / 100.0) * self.total_count)
        accum = 0
        for val, cnt in enumerate(self.counts):
            accum += cnt
            if accum >= threshold:
                return val
        return self.max_val
