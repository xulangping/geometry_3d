from sympy import *
x1, y1, z1, x2, y2, z2, x3, y3, z3, x, y, z = symbols('x1, y1, z1, x2, y2, z2, x3, y3, z3, x, y, z')
s = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]#[[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]]
P = [x, y, z]
def zhongxin(s):
    ineqs = []
    for j in range(3):
        ineqs.append(P[j] - sum([s[i][j] for i in range(3)]) / simplify(3))
    return ineqs
print(zhongxin(s))
def xiangliang(m, n):
    return [m[0] - n[0], m[1] - n[1], m[2] - n[2]]
def mianji3(s):
    x1, y1, z1 = xiangliang(s[0], s[1])
    x2, y2, z2 = xiangliang(s[0], s[2])
    s = sqrt((y1 * z2 - y2 * z1) ** 2+(z1 * x2 - x1 * z2) ** 2 + (x1 * y2 - x2 * y1) ** 2) / simplify(2)
    return s
def liangdianjuli(m, n):
    return sqrt((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2 + (m[2] - n[2]) ** 2)
def diancheng(m, n):
    return m[0] * n[0] + m[1] * n[1] + m[2] * n[2]
def neixin(s):
    l1 = mianji3([P, s[1], s[2]]) / liangdianjuli(s[1], s[2])
    l2 = mianji3([P, s[0], s[2]]) / liangdianjuli(s[0], s[2])
    l3 = mianji3([P, s[1], s[0]]) / liangdianjuli(s[1], s[0])
    M = []
    for i in range(3):
        M.append([x - s[i][0], y - s[i][1], z - s[i][2]])
    ineqs = [l1 - l2, l1 -l3, det(Matrix(M)), mianji3([P, s[1], s[2]]) + mianji3([P, s[0], s[2]]) + mianji3([P, s[1], s[0]]) -
             mianji3([s[2], s[1], s[0]])]
    return ineqs
print(solve(neixin(s), P))
def chuixin(s):
    M = []
    ineqs = []
    for i in range(3):
        M.append([x - s[i][0], y - s[i][1], z - s[i][2]])
        ineqs.append(diancheng(xiangliang(P, s[i]), xiangliang(s[(i + 1) % 3], s[(i + 2) % 3])))
    ineqs.append(det(Matrix(M)))
    return ineqs
print(solve(chuixin(s), P))