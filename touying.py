from sympy import *# A在平面BCD上的投影
def diancheng(m, n):
    return m[0] * n[0] + m[1] * n[1] + m[2] * n[2]
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
x, y, z = symbols('x, y, z')
A = [0, 0, 0]#[a1, b1, c1]
B = [1, 0, 0]#[a2, b2, c2]
C = [0, 1, 0]#[a3, b3, c3]
D = [0, 0, 1]#[a4, b4, c4]
P = [x, y, z]
a = xiangliang(A, P)
b = xiangliang(B, C)
c = xiangliang(B, D)
s = [A, B, C, D]
M = []
for i in range(3):
    M.append([x - s[i + 1][0], y - s[i + 1][1], z - s[i + 1][2]])
X = solve([det(Matrix(M)), diancheng(a, b), diancheng(a, c)], [x, y, z])
print(X)
