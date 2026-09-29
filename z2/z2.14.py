import math
x = 12.3e-1
y = 15.4
z = 0.252e3
s = y**(x + 1) / (abs(y - 2)**(1/3) + 3) + (x + y/2) / (2 * abs(x + y)) * (x + 1)**(-1/math.sin(z))
print("s =", s)