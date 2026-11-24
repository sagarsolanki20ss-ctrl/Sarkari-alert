import json
from datetime import datetime, timezone
from pathlib import Path

jobs_file = Path("jobs.json")

if jobs_file.exists():
    data = json.loads(jobs_file.read_text(encoding="utf-8"))
else:
    data = {"jobs": []}

data["lastUpdated"] = datetime.now(timezone.utc).isoformat()
data["source"] = "Official Government Recruitment Websites"

jobs_file.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print("Sarkari Alert data file updated successfully.")
