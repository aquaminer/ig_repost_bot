from json import loads
from pathlib import Path

print("Loading ig_repost_bot by @es3n1n, please wait...")
print("Parsing the config variables")

with open(Path(__file__).parent.parent / "config.json", "r") as f:
    config = loads(f.read())
