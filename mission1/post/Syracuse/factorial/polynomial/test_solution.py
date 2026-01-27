import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

def run(a, b, c, x):
    code = (
        f"a={a}\n"
        f"b={b}\n"
        f"c={c}\n"
        f"x={x}\n"
        + (HERE / "solution.py").read_text()
    )
    p = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return p.stdout.strip()

def test_simple():
    assert run(1, 1, 1, 1) == "3"

def test_mixed():
    assert run(2, 0, 1, 2) == str(2*(2**6) + 1)

def test_constant():
    assert run(0, 0, 5, 10) == "5"

