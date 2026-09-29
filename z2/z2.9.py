import math
x = 1.825e2
y = 18.225
z = -3.298e-2
s = abs(x**z - (y/x)**(1/3)) + (y - x) * (math.cos(y) - z/(y - x)) / (1 + (y - x)**2)
print("s =", s)