import math
x = 6.251
y = 0.827
z = 25.001
s = y**math.sqrt(abs(x)) + math.cos(y)**3 * (abs(x - y) * (1 + math.sin(z)**2 / math.sqrt(x + y))) / (math.exp(abs(x - y)) + x/2)
print("s =", s)