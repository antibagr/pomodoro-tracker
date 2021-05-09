import sys
from pathlib import Path

sys.path.append(Path(__file__).resolve().parent)

from app import run_tracker

run_tracker()
