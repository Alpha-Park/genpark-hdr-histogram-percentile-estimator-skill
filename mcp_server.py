import sys
import json
from client import HdrHistogram

def main():
    hdr = HdrHistogram()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "record":
            for v in params.get("values", []):
                hdr.record_value(v)
            res = {"status": "ok", "total": hdr.total_count}
        elif method == "percentile":
            p = hdr.get_value_at_percentile(params.get("percentile", 50.0))
            res = {"percentile_value": p}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
