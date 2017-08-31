from sympy import *
view = [1, 2, 3]
t = symbols('t')
view[2] = [[0, 0, t], [6, 0, t], [3, 4, t]]
view[0] = [[t, 0, 0], [t, 0, 6], [t, 4, 3]]
view[1] = [[0, t, 0], [0, t, 6],  [3, t, 3], [6, t, 6]]
print(view)
x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = symbols('x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4')
a = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
for i in range(3):
    if len(view[i]) == 4:
        for j in range(4):
            a[j][(i + 1) % 3], a[j][(i + 2) % 3] = view[i][j][(i + 1) % 3], view[i][j][(i + 2) % 3]
        for j in range(4):
            list3 = []
            list1 = []
            list2 = []
            for k in view[(i + 2) % 3]:
                if a[j][(i + 1) % 3] == k[(i + 1) % 3]:
                    list1.append(k[i])
            for k in view[(i + 1) % 3]:
                if a[j][(i + 2) % 3] == k[(i + 2) % 3]:
                    list2.append(k[i])
            list3 = list(set(list1) & set(list2))
            if len(list3) == 1:
                a[j][i] = list3[0]
            else:
                a[j][i] = list3
        print(a)
        for j in range(4):
            if (type(a[j][i]) == list):
                for k in range(4):
                    if (k != j) & (a[k][(i + 1) % 3] == a[j][(i + 1) % 3]) & (type(a[k][i]) != list):
                        print(set(a[j][i]) - set([a[k][i]]))
                        a[j][i] = list(set(a[j][i]) - set([a[k][i]]))[0]
                        break
                    elif (k != j) & (a[k][(i + 1) % 3] == a[j][(i + 1) % 3]) & (type(a[k][i]) == list):
                        a[j][i], a[k][i] = a[j][i][0], a[j][i][1]
                        break
        break
print(a)