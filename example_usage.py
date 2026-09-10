from client import HdrHistogram

def main():
    print("=== Testing HdrHistogram Percentile Estimator ===")
    hdr = HdrHistogram(highest_trackable_value=1000)
    for i in range(1, 101):
        hdr.record_value(i)

    p50 = hdr.get_value_at_percentile(50.0)
    p99 = hdr.get_value_at_percentile(99.0)
    print(f"P50: {p50}, P99: {p99}")
    assert p50 == 50 and p99 == 99
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
