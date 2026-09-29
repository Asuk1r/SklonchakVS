import math
x = 17.421
y = 10.365e-3
z = 0.828e5
s = (y**(1/3) + (x - 1)**(1/3)) / (abs(x - y) * (math.sin(z)**2 + math.tan(z)))
print("s =", s)