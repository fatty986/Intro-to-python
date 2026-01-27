import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

def run_with_n(n_value: int):
    code = f"n={n_value}\n" + (HERE / "solution.py").read_text()
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=5)
    out = p.stdout.strip().splitlines()
    return out

def test_n_1():
    assert run_with_n(1) == ["1"]

def test_n_6():
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert run_with_n(6) == ["6", "3", "10", "5", "16", "8", "4", "2", "1"]
