from sympy import *
import itertools
x = symbols('x')
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
def area(s):
    x1, y1, z1 = xiangliang(s[0], s[1])
    x2, y2, z2 = xiangliang(s[0], s[2])
    a = sqrt((y1 * z2 - y2 * z1) ** 2+(z1 * x2 - x1 * z2) ** 2 + (x1 * y2 - x2 * y1) ** 2) / simplify(2)
    return a
def three_pyramid_volume(s):
    x1, y1, z1 = xiangliang(s[0], s[3])
    x2, y2, z2 = xiangliang(s[1], s[3])
    x3, y3, z3 = xiangliang(s[2], s[3])
    M = Matrix([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    v = abs(det(M)) / simplify(6)
    return v
def point_in_plane(s, P):
    if area([s[0], s[1], P]) + area([s[0], s[2], P]) + area([s[2], s[1], P]) == area(s):
        return True
    else:
        return False
def if_line_intersection(s1, s2):
    P = []
    Q = []
    for i in range(3):
        P.append(x * (s2[1][i] - s2[0][i]) + s2[0][i])
    s1.append(P)
    t = solve(three_pyramid_volume(s1))
    for i in range(3):
        Q.append(t * (s2[1][i] - s2[0][i]) + s2[0][i])
    if (t >= 1) or (t <= 0) or (not point_in_plane(s1, Q)):
        return False
    return True
def find_dotted_line(s1, s2, P):
    a = []
    for i in s1:
        b = []
        for j in range(3):
            b.append((i[0][j] - i[1][j]) / simplify(2))
        for j in list(itertools.combinations(s2,3)):
            if area(j) > 0:
                if if_line_intersection(j, [P, b]):
                    a.append(i)
                    break
    return a