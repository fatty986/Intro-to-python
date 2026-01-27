# Mission 1 – Main Exercise
# Find solutions to: a * x + b * y = c

a = 2
b = 3
c = 13
max_value = 10

solutions = 0

for x in range(1, max_value + 1):
    for y in range(1, max_value + 1):
        if a * x + b * y == c:
            print("x =", x, ", y =", y)
            solutions += 1

if solutions == 0:
    print("No solution found")
else:
    print(solutions, "solutions found")
