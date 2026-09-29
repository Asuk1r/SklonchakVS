import math
x = 3.981e-2
y = -1.625e3
z = 0.512
s = 2**(-x) * math.sqrt(x + abs(y)**(1/3)) * math.exp((x - 1/math.sin(z))/3)
print("s =", s)