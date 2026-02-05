import json, statistics, hashlib
from datetime import datetime

with open("input.json") as f:
    data = json.load(f)

ts = sorted(
    datetime.fromisoformat(x["timestamp"].replace("Z",""))
    for x in data["replies"]
)

if len(ts) < 2:
    print(json.dumps({"error": "INSUFFICIENT_DATA"}, indent=2))
    exit(0)

deltas = [(ts[i]-ts[i-1]).total_seconds() for i in range(1,len(ts))]

mean = round(statistics.mean(deltas), 2)
std  = round(statistics.stdev(deltas), 2) if len(deltas) > 1 else 0
lt10 = sum(1 for d in deltas if d < 10)

snapshot = hashlib.sha256(
    "\n".join(t.isoformat()+"Z" for t in ts).encode()
).hexdigest()

classification = "INDICATIVE_SUSPICIOUS" if (len(ts)>=30 and std<5) else "INDICATIVE_ORGANIC"

result = {
    "engine": "Veritas",
    "replies_analyzed": len(ts),
    "mean_interval_sec": mean,
    "std_interval_sec": std,
    "intervals_lt_10s": lt10,
    "snapshot_hash": snapshot,
    "classification": classification
}

print(json.dumps(result, indent=2))
