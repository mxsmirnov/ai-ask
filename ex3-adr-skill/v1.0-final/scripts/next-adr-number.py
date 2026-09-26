#!/usr/bin/env python3
"""Печатает следующий четырёхзначный номер ADR по файлам adr-NNNN-*.md."""

from pathlib import Path
import re
import sys

pattern = re.compile(r"^adr-(\d{4})-.*\.md$")
adr_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "adr")
adr_dir.mkdir(parents=True, exist_ok=True)

numbers = []
for path in adr_dir.iterdir():
    if path.is_file():
        match = pattern.match(path.name)
        if match:
            numbers.append(int(match.group(1)))

print(f"{max(numbers, default=0) + 1:04d}")
