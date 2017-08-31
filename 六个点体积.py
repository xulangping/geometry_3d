from sympy import*
import itertools
from silengzhui import *
from mianji import *
from touying import *
A = [-sqrt(3) / 2, -Rational(1, 2), 2]
B = [0, -1, 2]#[a2, b2, c2]
C = [sqrt(3) / 2, -Rational(1, 2), 2]#[a3, b3, c3]
D = [-sqrt(3), 0, 0]#[a1, b1, c1]#[a4, b4, c4]
P = [0, -1, 0]
Q = [sqrt(3), 0, 0]#[a1, b1, c1]
s = [Q, A, P, B, D, C]
def chacheng(m, n):
    return [m[1] * n[2] - m[2] * n[1], m[2] * n[0] - m[0] * n[2], m[0] * n[1] - m[1] * n[0]]
for i in list(itertools.combinations(s,4)):
    if gongmian(i):
        t = [j for j in s if j not in i]
        v1 = slz([t[0], i[0], i[1], i[2], i[3]])
        v2 = slz([t[1], i[0], i[1], i[2], i[3]])
        a = xiangliang(i[0], i[1])
        b = xiangliang(i[0], i[2])
        c = xiangliang(i[0], i[3])
        if diancheng(chacheng(a, b), chacheng(a, c)) < 0:
            v9 = sanlengzhui([t[0], t[1], i[0], i[1]])
            v10 = sanlengzhui([t[0], t[1], i[2], i[3]])
        elif diancheng(chacheng(b, a), chacheng(b, c)) < 0:
            v9 = sanlengzhui([t[0], t[1], i[0], i[2]])
            v10 = sanlengzhui([t[0], t[1], i[1], i[3]])
        else:
            v9 = sanlengzhui([t[0], t[1], i[0], i[3]])
            v10 = sanlengzhui([t[0], t[1], i[2], i[1]])
        v3 = sanlengzhui([t[0], t[1], i[0], i[1]])
        v4 = sanlengzhui([t[0], t[1], i[2], i[1]])
        v5 = sanlengzhui([t[0], t[1], i[2], i[3]])
        v6 = sanlengzhui([t[0], t[1], i[0], i[3]])
        v7 = sanlengzhui([t[0], t[1], i[0], i[2]])
        v8 = sanlengzhui([t[0], t[1], i[1], i[3]])
        v = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 - v9 - v10) / simplify(2)
        print(i, v)
        break

