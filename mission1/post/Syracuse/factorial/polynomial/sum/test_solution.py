import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

def run(n_value: int):
    code = f"n={n_value}\n" + (HERE / "solution.py").read_text()
    p = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return p.stdout.strip()

def test_1():
    assert run(1) == "1"

def test_3():
    assert run(3) == "6"

def test_5():
    assert run(5) == "15"
