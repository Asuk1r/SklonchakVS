import math
x = 3.74e-2
y = -0.825
z = 0.16e2
s = ((9 + (x - y)**2)**(1/3)) / (x**2 + y**2 + 2) - math.exp(abs(x - y)) * math.tan(z)**3
print("s =", s)