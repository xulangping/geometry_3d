from sympy import *
x, y, z = symbols('x, y, z')
A = [0, 0, 0]
B = [1, 0, 0]
C = [0, 0, 2]
D = [0, 2, 2]
a = [0, 0, 0]
b = [0, 0, 0]
c = [0, 0, 0]
for i in range(3):
    a[i] = A[i] - B[i]
    b[i] = C[i] - D[i]
    c[i] = A[i] - C[i]
X = solve([a[0] * x + a[1] * y + a[2], b[0] * x + b[1] * y + b[2]])
if X == []:
    X = solve([a[0] * x + a[1] + a[2] * z, b[0] * x + b[1] + b[2] * z])
    if X == []:
        X = solve([a[0] + a[1] * y+ a[2] * z, b[0] + b[1] * y + b[2] * z])
        X[x] = 1
    else:
        X[y] = 1
else:
    X[z] = 1
n = [X[x], X[y], X[z]]
l = abs(c[0] * n[0] + c[1] * n[1] + c[2] * n[2]) / sqrt(sum([i ** 2 for i in n]))
print(l)