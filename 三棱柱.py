from sympy import*
import itertools
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
def sanlengzhui(s):
    x1, y1, z1 = xiangliang(s[0], s[3])
    x2, y2, z2 = xiangliang(s[1], s[3])
    x3, y3, z3 = xiangliang(s[2], s[3])
    M = Matrix([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    v = abs(det(M)) / 6
    return v
A = [0, 2, 0]#[a1, b1, c1]
B = [0, 1, sqrt(3)]#[a2, b2, c2]
C = [1, 2, 0]#[a3, b3, c3]
D = [0, 1 / 2, sqrt(3) / 2]#[a4, b4, c4]
E = [1, 0, 1]#[a5, b5, c5]
F = [0, 1, 1]#[a6, b6, c6]
s= [A, B, C, D, E, F]
for i in list(itertools.combinations(s,4)):
    v = 3 * sanlengzhui(i)
    if v > 0:
        break
print(v)