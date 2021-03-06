from sympy import *
import itertools
infinitesimal = 0.000001
x = symbols('x')


# (x1*y2*z3 - x1*y2*z5 - x1*y3*z2 + x1*y3*z5 + x1*y5*z2 - x1*y5*z3 - x2*y1*z3 + x2*y1*z5 + x2*y3*z1 - x2*y3*z5 - x2*y5*z1 + x2*y5*z3 + x3*y1*z2 - x3*y1*z5 - x3*y2*z1 + x3*y2*z5 + x3*y5*z1 - x3*y5*z2 - x5*y1*z2 + x5*y1*z3 + x5*y2*z1 - x5*y2*z3 - x5*y3*z1 + x5*y3*z2)/(x1*y2*z4 - x1*y2*z5 - x1*y3*z4 + x1*y3*z5 - x1*y4*z2 + x1*y4*z3 + x1*y5*z2 - x1*y5*z3 - x2*y1*z4 + x2*y1*z5 + x2*y3*z4 - x2*y3*z5 + x2*y4*z1 - x2*y4*z3 - x2*y5*z1 + x2*y5*z3 + x3*y1*z4 - x3*y1*z5 - x3*y2*z4 + x3*y2*z5 - x3*y4*z1 + x3*y4*z2 + x3*y5*z1 - x3*y5*z2 + x4*y1*z2 - x4*y1*z3 - x4*y2*z1 + x4*y2*z3 + x4*y3*z1 - x4*y3*z2 - x5*y1*z2 + x5*y1*z3 + x5*y2*z1 - x5*y2*z3 - x5*y3*z1 + x5*y3*z2)
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]


def area(s):
    x1, y1, z1 = xiangliang(s[0], s[1])
    x2, y2, z2 = xiangliang(s[0], s[2])
    a = sqrt((y1 * z2 - y2 * z1) ** 2 + (z1 * x2 - x1 * z2) ** 2 + (x1 * y2 - x2 * y1) ** 2) / simplify(2)
    return a


def three_pyramid_volume(s):
    x1, y1, z1 = xiangliang(s[0], s[3])
    x2, y2, z2 = xiangliang(s[1], s[3])
    x3, y3, z3 = xiangliang(s[2], s[3])
    M = Matrix([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    v = det(M) / simplify(6)
    return v


def point_in_plane(s, P):
    if abs(area([s[0], s[1], P]) + area([s[0], s[2], P]) + area([s[2], s[1], P]) - area(s)) < infinitesimal:
        return True
    else:
        return False


def if_line_intersection(s1, s2):
    Q = []
    [x1, y1, z1] = s1[0]
    [x2, y2, z2] = s1[1]
    [x3, y3, z3] = s1[2]
    [x4, y4, z4] = s2[0]
    [x5, y5, z5] = s2[1]
    if abs(x1 * y2 * z4 - x1 * y2 * z5 - x1 * y3 * z4 + x1 * y3 * z5 - x1 * y4 * z2 + x1 * y4 * z3 + x1 * y5 * z2 - x1 * y5 * z3 - x2 * y1 * z4 + x2 * y1 * z5 +
        x2 * y3 * z4 - x2 * y3 * z5 + x2 * y4 * z1 - x2 * y4 * z3 - x2 * y5 * z1 + x2 * y5 * z3 + x3 * y1 * z4 - x3 * y1 * z5 - x3 * y2 * z4 +
        x3 * y2 * z5 - x3 * y4 * z1 + x3 * y4 * z2 + x3 * y5 * z1 - x3 * y5 * z2 + x4 * y1 * z2 - x4 * y1 * z3 - x4 * y2 * z1 + x4 * y2 * z3 +
        x4 * y3 * z1 - x4 * y3 * z2 - x5 * y1 * z2 + x5 * y1 * z3 + x5 * y2 * z1 - x5 * y2 * z3 - x5 * y3 * z1 + x5 * y3 * z2) > infinitesimal:
        t = (
            x1 * y2 * z3 - x1 * y2 * z5 - x1 * y3 * z2 + x1 * y3 * z5 + x1 * y5 * z2 - x1 * y5 * z3 - x2 * y1 * z3 + x2 * y1 * z5 + x2 * y3 * z1 - x2 * y3 * z5 -
            x2 * y5 * z1 + x2 * y5 * z3 + x3 * y1 * z2 - x3 * y1 * z5 - x3 * y2 * z1 + x3 * y2 * z5 + x3 * y5 * z1 - x3 * y5 * z2 - x5 * y1 * z2 + x5 * y1 * z3 +
            x5 * y2 * z1 - x5 * y2 * z3 - x5 * y3 * z1 + x5 * y3 * z2) / (
            x1 * y2 * z4 - x1 * y2 * z5 - x1 * y3 * z4 + x1 * y3 * z5 - x1 * y4 * z2 + x1 * y4 * z3 +
            x1 * y5 * z2 - x1 * y5 * z3 - x2 * y1 * z4 + x2 * y1 * z5 + x2 * y3 * z4 - x2 * y3 * z5 +
            x2 * y4 * z1 - x2 * y4 * z3 - x2 * y5 * z1 + x2 * y5 * z3 + x3 * y1 * z4 - x3 * y1 * z5 -
            x3 * y2 * z4 + x3 * y2 * z5 - x3 * y4 * z1 + x3 * y4 * z2 + x3 * y5 * z1 - x3 * y5 * z2 +
            x4 * y1 * z2 - x4 * y1 * z3 - x4 * y2 * z1 + x4 * y2 * z3 + x4 * y3 * z1 - x4 * y3 * z2 -
            x5 * y1 * z2 + x5 * y1 * z3 + x5 * y2 * z1 - x5 * y2 * z3 - x5 * y3 * z1 + x5 * y3 * z2)
    else:
        return False
    if abs(t - 1) < infinitesimal or abs(t) < infinitesimal:
        return False
    for i in range(3):
        Q.append(t * (s2[0][i] - s2[1][i]) + s2[1][i])
    if (t >= 1) or (t <= 0) or (not point_in_plane(s1, Q)):
        return False
    return True


def find_dotted_line(s1, points, P):
    a = []
    s2 = []
    for i in points.values():
        s2.append(i)
    for i in s1:
        b = []
        for j in range(3):
            b.append((points[i[0]][j] + points[i[1]][j]) / simplify(2))
        for j in list(itertools.combinations(s2, 3)):
            j = list(j)
            if abs(area(j)) > infinitesimal:
                if if_line_intersection(j, [P, b]):
                    a.append(i)
                    break
    for i in s1:
        if i in a:
            i.append('dotted')
        else:
            i.append('solid')
    return s1


points = {'A': [0, 0, 0], 'B': [1, 0, 0], 'C': [0, 1, 0], 'D': [0, 0, 1], 'E': [0, 1, 1], 'F': [1, 0, 1],
          'G': [1, 1, 0], 'H': [1, 1, 1]}
print(find_dotted_line([['A', 'B'], ['A', 'C'], ['A', 'D'], ['G', 'H']], points, [4, 4, 4]))
