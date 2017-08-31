from sympy import *
x, y, z = symbols('x, y, z')
A = [0, 0, 1]
B = [1, 0, 0]
C = [0, 1, 0]
D = [0, 0, 0]
O = [x, y, z]
s = [D, A, B, C]
l = s
ineqs=[]
for i in range(len(s)):
    l[i] = (x - s[i][0]) ** 2 + (y - s[i][1]) ** 2 + (z - s[i][2]) ** 2
    ineqs.append(l[0] - l[i])
X = solve(ineqs,[x, y, z])
print(X)