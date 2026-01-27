import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

def run_with_n(n_value: int):
    code = f"n={n_value}\n" + (HERE / "solution.py").read_text()
    p = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return p.stdout.strip()

def test_0():
    assert run_with_n(0) == "1"

def test_5():
    assert run_with_n(5) == "120"

def test_7():
    assert run_with_n(7) == "5040"
