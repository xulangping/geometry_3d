from sympy import *
x, y, z = symbols('x, y, z')
A = [-sqrt(3), 0, 0]
B = [0, -1, 0]
C = [0, 3, 0]
D = [0, 0, 0]
B1 = [x, y, z]
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
def diancheng(m, n):
    return m[0] * n[0] + m[1] * n[1] + m[2] * n[2]
def juli(m, n):
    return sqrt((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2 + (m[2] - n[2]) ** 2)
ineqs = [juli(B1, D) - juli(B, D), juli(B1, A) - juli(B, A), diancheng(xiangliang(B1, D), xiangliang(C, D))]
X = solve([juli(B1, D) - juli(B, D), juli(B1, A) - juli(B, A), diancheng(xiangliang(B1, D), xiangliang(C, D))],[x, y, z])
print(X)