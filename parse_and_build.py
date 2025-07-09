# parse_and_build.py
import json
import subprocess
import os
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python parse_and_build.py compile_commands.json")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    if not json_path.is_file():
        print(f"Error: {json_path} not found.")
        sys.exit(1)

    try:
        data = json.loads(json_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        sys.exit(1)

    failures = 0
    for entry in data:
        directory = entry.get("directory")
        command   = entry.get("command") or " ".join(entry.get("arguments", []))
        if not directory or not command:
            print("Skipping invalid entry:", entry)
            continue

        print(f"\n[Building] {entry.get('file')} in {directory}")
        proc = subprocess.run(command, cwd=directory, shell=True)
        if proc.returncode != 0:
            print(f"[Error] Command failed: {command}")
            failures += 1

    if failures:
        print(f"\nBuild finished with {failures} errors.")
        sys.exit(1)
    else:
        print("\nAll commands succeeded.")
        sys.exit(0)

if __name__ == "__main__":
    main()
