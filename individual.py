from math import sqrt

x1, y1 = list(map(int, input("Enter x1, y1: ").split()))
x2, y2 = list(map(int, input("Enter x2, y2: ").split()))

print(sqrt((x2 - x1)**2 + (y2 - y1)**2))
