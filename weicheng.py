class eqs_wei_area(objects):
    def chuli(self, tt):
        ans = []
        for t in tt:
            if 'y' in str(t[0]) + str(t[2]):
                a = t[0] - t[2]
                b = a.coeff(y)
                ans.append([y, '=', (y * b - a) / b])
            else:
                ans.append(t)
        return ans

    def mianji(self, a, b):
        y1 = a
        y2 = b
        [x1, x2] = solve(y1 - y2)
        ineqs = [Symbol("s"), '=', abs(integrate(y1 - y2, (x, x1, x2)))]
        return ineqs

    def mianji2(self,a ,b, c, d):
        y1 = a
        y2 = b
        x1 = c
        x2 = d
        ineqs=[Symbol("s"), '=', abs(integrate(y1 - y2,(x,x1,x2)))]
        return ineqs

    def mianji1(self,a, b, c):
        y1 = a
        y2 = b
        x1 = c
        x2 = solve(a - b)
        ineqs=[Symbol("s"), '=', abs(integrate(y1 - y2,(x,x1,x2)))]
        return ineqs

    def mianji3(self,a, b, c):
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
        ineqs = [Symbol("s"), '=', ans]
        return ineqs

    def zhengli(self,t):
        if len(t) == 2:
            return self.mianji(t[0][2], t[1][2])
        if len(t) == 3:
            for i in range(3):
                if t[i][0] == x:
                    return self.mianji1(t[(i+1) % 3][2], t[(i + 2) % 3][2] , t[i][2])
            return self.mianji3(t[0][2], t[1][2], t[2][2])

        if len(t) == 4:
            a = []
            b = []
            for i in range(4):
                if t[i][0] == x:
                    b.append(t[i][2])
                else:
                    a.append(t[i][2])
            return self.mianji2(a[0], a[1], b[0], b[1])

    def solver(self, *args):
        eqs = args[0].toSympy()
        value = self.chuli(eqs)
        print self.zhengli(value)
        return self