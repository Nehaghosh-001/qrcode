#!/usr/bin/env python
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR / "upiqr"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "upiqr.settings")

from django.core.management import execute_from_command_line


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
