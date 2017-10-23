import math

def f(x):
    return math.sin(x)/x

values = [0.1, 0.01, 0.001, 0.0001]

for val in values:
    print(f(val))