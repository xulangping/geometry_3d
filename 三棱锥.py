from sympy import *
a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4 = symbols('a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4')
A = [-a1/2, 0, 0]#[a1, b1, c1]
B = [a1/4, -sqrt(3)*sqrt(a1**2)/4, 0]#[a2, b2, c2]
C = [0, 0, b1]#[a3, b3, c3]
D = [-3*a1/8, sqrt(3)*sqrt(a1**2)/8, 3*b1/2]#[a4, b4, c4]
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
x1, y1, z1 = xiangliang(A, D)
x2, y2, z2 = xiangliang(B, D)
x3, y3, z3 = xiangliang(C, D)
M = Matrix([[x1, y1, z1],[x2, y2, z2],[x3, y3, z3]])
v = abs(det(M)) / simplify(6)
print(v)