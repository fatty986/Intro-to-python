import solution

def run(a, b, c):
    solution.a = a
    solution.b = b
    solution.c = c
    exec(open("solution.py").read(), solution.__dict__)
    return solution.median

def test_1():
    assert run(1, 2, 3) == 2

def test_2():
    assert run(3, 1, 2) == 2

def test_3():
    assert run(2, 2, 3) == 2

def test_4():
    assert run(5, 5, 5) == 5
