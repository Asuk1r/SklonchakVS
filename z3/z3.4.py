def lace_length(a, b, l, N):
    return N * a + (N - 1) * b + 2 * l

a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(lace_length(a, b, l, N))