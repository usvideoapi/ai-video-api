import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from engine import optimize_brief  # noqa: E402


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 -m cli.main <brief.json>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    payload = json.loads(path.read_text())
    result = optimize_brief(payload)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
