from sympy import*
C = [0, 1, 0]#[a3, b3, c3]
D = [1, 0, 0]
P = [0, 0, 1]
s = [P, C, D]
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
def mianji3(s):
    x1, y1, z1 = xiangliang(s[0], s[1])
    x2, y2, z2 = xiangliang(s[0], s[2])
    s = sqrt((y1 * z2 - y2 * z1) ** 2+(z1 * x2 - x1 * z2) ** 2 + (x1 * y2 - x2 * y1) ** 2) / simplify(2)
    return s
def mianji4(s):
    s1 = mianji3([s[0], s[1], s[2]])
    s2 = mianji3([s[0], s[1], s[3]])
    s3 = mianji3([s[0], s[2], s[3]])
    s4 = mianji3([s[3], s[1], s[2]])
    s = (s1 + s2 + s3 + s4) / simplify(2)
    return(s)
print(mianji3(s))
