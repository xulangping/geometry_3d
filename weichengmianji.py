from sympy import *
x, s, y  = symbols('x, s, y')
def chuli(tt):
    ans = []
    for t in tt:
        if 'y' in str(t[0]) + str(t[2]):
            a = t[0] - t[2]
            b = a.coeff(y)
            ans.append([y, '=', (y * b - a) / b])
        else:
            ans.append(t)
    return ans
def mianji(a, b):
    y1 = a
    y2 = b
    [x1, x2] = solve(y1 - y2)
    ineqs = [s, '=', abs(integrate(y1 - y2, (x, x1, x2)))]
    print(ineqs)
    return ineqs
def mianji2(a ,b, c, d):
    y1 = a
    y2 = b
    x1 = c
    x2 = d
    ineqs=[s, '=', abs(integrate(y1 - y2,(x,x1,x2)))]
    print(ineqs)
    return ineqs
def mianji1(a, b, c):
    y1 = a
    y2 = b
    x1 = c
    x2 = solve(a - b)
    ineqs=[s, '=', abs(integrate(y1 - y2,(x,x1,x2)))]
    print(ineqs)
    return ineqs
#mianji1(sqrt(x), x - 2, 0)
def mianji3(a, b, c):
    y1 = a
    y2 = b
    y3 = c
    x1 = [i for i in solve(y1 - y2) if i >= 0][0]
    x2 = [i for i in solve(y1 - y3) if i >= 0][0]
    x3 = [i for i in solve(y3 - y2) if i >= 0][0]
    s1 = abs(integrate(y1, (x, x1, x2)))
    s2 = abs(integrate(y2, (x, x1, x3)))
    s3 = abs(integrate(y3, (x, x2, x3)))
    if x1 < x2:
        if x1 < x3:
            if x2 < x3:
                ans = abs(s1 + s3 -s2)
            else:
                ans = abs(s2 + s3 -s1)
        else:
            ans = abs(s2 + s1 - s3)
    elif x3 < x2:
        ans = abs(s1 + s3 - s2)
    elif x3 < x1:
        ans = abs(s2 + s3 - s1)
    else:
        ans = abs(s2 + s1 - s3)
    ineqs = [s, '=', ans]
    print(ineqs)
    return ineqs
#mianji3(1 / x, x, 3)
def zhengli(t):
    if len(t) == 2:
        return mianji(t[0][2], t[1][2])
    if len(t) == 3:
        for i in range(3):
            if t[i][0] == x:
                return mianji1(t[(i+1) % 3][2], t[(i + 2) % 3][2] , t[i][2])
        return mianji3(t[0][2], t[1][2], t[2][2])
    if len(t) == 4:
        a = []
        b = []
        for i in range(4):
            if t[i][0] == x:
                b.append(t[i][2])
            else:
                a.append(t[i][2])
        return mianji2(a[0], a[1], b[0], b[1])
zhengli(chuli([[ x * y, '=',  1], [y, '=', 0], [x, '=', 2], [x, '=', Rational(1, 2)]]))