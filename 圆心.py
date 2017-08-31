from sympy import *
x, y, z = symbols('x, y, z')
A = [0, 0, 1]
B = [1, 0, 0]
C = [0, 1, 0]
D = [x, y, z]
s = [D, A, B, C]
M = []
l = [0, 0, 0]
for i in range(3):
    M.append([s[0][0] - s[i + 1][0], s[0][1] - s[i + 1][1], s[0][2] - s[i + 1][2]])
    l[i] = (x - s[i+1][0]) ** 2 + (y - s[i+1][1]) ** 2 + (z - s[i+1][2]) ** 2
X = solve([det(Matrix(M)), l[0] - l[1], l[0] - l[2]], [x, y, z])
print(X)