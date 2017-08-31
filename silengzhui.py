from sympy import*
a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4, a5, b5, c5 = symbols('a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4, a5, b5, c5')
A = [1, 0, 0]#[a1, b1, c1]
B = [0, 1, 0]#[a2, b2, c2]
C = [0, 0, 1]#[a3, b3, c3]
D = [0, 0, 0]#[a4, b4, c4]
E = [1.5, 1.5, -2]#[a5, b5, c5]
s = [A, B, C, D, E]
def xiangliang(m, n):
    return m[0] - n[0], m[1] - n[1], m[2] - n[2]
def sanlengzhui(s):
    x1, y1, z1 = xiangliang(s[0], s[3])
    x2, y2, z2 = xiangliang(s[1], s[3])
    x3, y3, z3 = xiangliang(s[2], s[3])
    M = Matrix([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    v = abs(det(M)) / simplify(6)
    return v
def gongmian(s):
    M = []
    for i in range(3):
        M.append([s[0][0] - s[i + 1][0], s[0][1] - s[i + 1][1], s[0][2] - s[i + 1][2]])
    if det(Matrix(M)) == 0:
        return True
    else:
        return False
def slz(s):
    for i in range(5):
        t = [j for j in s]
        del t[i]
        if gongmian(t):
            v1 = sanlengzhui([s[i], t[0], t[1], t[2]])
            v2 = sanlengzhui([s[i], t[0], t[1], t[3]])
            v3 = sanlengzhui([s[i], t[0], t[2], t[3]])
            v4 = sanlengzhui([s[i], t[2], t[1], t[3]])
            v = (v1 + v2 + v3 + v4) / simplify(2)
            #print(v)
            return v
    return None
    print('Error!')

