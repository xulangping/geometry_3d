import copy
import itertools
from sympy import *
shuru = [
    {
        'id': 11103,
        'front_view': [[0, 0], [sqrt(3), 0], [2 * sqrt(3), 0], [sqrt(3), 1]],
        'side_view': [[0, 0], [0, 1], [1, 0]],
        'vertical_view': [[0, 0], [sqrt(3), 0], [2 * sqrt(3), 0], [sqrt(3), 1]]
    },
    {
        'id':11356,
        'front_view': [[0, 0], [1, 0], [2, 0], [1, 1]],
        'side_view': [[0, 0], [0, 1], [1, 0]],
        'vertical_view': [[0, 0], [1, 0], [2, 0], [1, 1]]
     },
    {
        'id': 11714,
        'front_view': [[0, 0], [1, 0], [2, 0], [0, 2], [1, 2], [2, 2]],
        'side_view': [[0, 0], [0, 1], [2, 1], [2, 0]],
        'vertical_view': [[0, 0], [0, 1], [2, 0], [1, 1]]
    },
    {
        'id': 11921,
        'front_view': [[0, 0], [4, 0], [4, 2], [0, 5]],
        'side_view': [[0,0], [0, 3], [5, 0], [2, 3], [5, 3]],
        'vertical_view': [[0, 0], [0, 3], [4, 3]]
    },
    {
        'id': 12730,
        'front_view': [[0, 0], [10, 0], [0, 4], [10, 4]],
        'side_view': [[0, 0], [0, 8], [4, 3], [4, 5]],
        'vertical_view': [[0, 0], [10, 0], [10, 3], [0, 3], [10, 5], [0, 5], [0, 8], [10, 8]]
    },
    {
        'id': 12760,
        'front_view': [[0, 0], [1, 0], [0, 2]],
        'side_view': [[0, 0], [0, 1], [2, 1]],
        'vertical_view':[[0, 1], [1, 0], [1, 1]]
    },
    {
        'id': 12781,
        'front_view': [[0, 0], [2, 0], [0, 2], [1, 2]],
        'side_view': [[0, 0], [2, 0], [0, 2], [2, 1]],
        'vertical_view':[[0, 0], [0, 1], [1, 0], [1, 1], [0, 2], [2, 0], [2, 2]]
    },
    {
        'id': 13524,
        'front_view': [[0, 0], [2, 0], [5, 0], [0, 4], [2, 4], [5, 4]],
        'side_view': [[0, 0], [4, 0], [0, 4], [4, 4]],
        'vertical_view': [[0, 0], [5, 0], [0, 4], [2, 4]]
    },
    {
        'id': 13708,
        'front_view': [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1]],
        'side_view': [[0, 0], [0, 1], [1, 0], [1, 1], [0, 2], [1, 2]],
        'vertical_view':[[0, 1], [1, 0], [2, 0], [3, 1], [1, 2], [2, 2]]
    },
    {
        'id': 14240,
        'front_view': [[0, 0], [0, 4], [4, 0], [4, 4]],
        'side_view': [[0, 0], [0, 4], [4, 1], [4, 3]],
        'vertical_view':[[0, 0], [0, 4], [4, 0], [4, 4], [0, 1], [0, 3], [4, 1], [4, 3]]
    },
    {
        'id': 14304,
        'front_view': [[0, 0], [sqrt(3), 0], [2 * sqrt(3), 0], [sqrt(3), 3]],
        'side_view': [[0, 0], [0, 1], [0, 2], [3, 1]],
        'vertical_view':[[sqrt(3), 0], [0, 1], [sqrt(3), 1], [2 * sqrt(3), 1], [sqrt(3), 2]]
    },
    {
        'id':14325,
        'front_view': [[0, 0], [1, sqrt(3)], [4, sqrt(3)], [3, 0]],
        'side_view': [[0, 0], [0, 3], [sqrt(3), 0], [sqrt(3), 3]],
        'vertical_view': [[0, 0], [1, 0], [3, 0], [4, 0], [0, 3], [1, 3], [3, 3], [4, 3]]
    },
    {
        'id': 14847,
        'front_view': [[0, 0], [8, 0], [0, 2], [1, 2], [7, 2], [8, 2], [1, 10], [7, 10]],
        'side_view': [[0, 0], [0, 10], [2, 0], [2, 6], [2, 8], [2, 10], [10, 6], [10, 8]],
        'vertical_view': [[0, 0], [8, 0], [1, 6], [7, 6], [1, 8], [7, 8], [0, 10], [8, 10]]
    },
    {
        'id': 14965,
        'front_view': [[0, 0], [2, 0], [2, 2]],
        'side_view': [[0, 0], [0, 2], [2, 0]],
        'vertical_view': [[0, 2], [2, 0], [2, 2]]
    },
    {
        'id': 25097,
        'front_view': [[0, 0], [2, 0], [4, 0], [3, 2]],
        'side_view': [[0, 0], [2, 0], [0, 3]],
        'vertical_view': [[0, 0], [3, 0], [4, 0], [2, 3]]
    },
    {
        'id': 25115,
        'front_view': [[0, 0], [6, 0], [3, 4]],
        'side_view': [[0, 0], [0, 6], [4, 3]],
        'vertical_view':[[0, 0], [3, 3], [6, 6], [0, 6]]
    },
    {
        'id': 25186,
        'front_view': [[0, 0], [20, 0], [20, 20]],
        'side_view': [[0, 0], [0, 20], [20, 10]],
        'vertical_view': [[0, 0], [0, 20], [20, 0], [20, 20], [20, 10]]
    },
    {
        'id': 89129,
        'front_view': [[0, 0], [3, 0], [6, 0], [3, 3]],
        'side_view': [[0, 0], [3, 3], [0, 3]],
        'vertical_view': [[0, 0], [6, 0], [3, 3]]
    },
    {
        'id': 89359,
        'front_view': [[0, 4], [4, 0], [4, 2], [4, 4]],
        'side_view': [[0, 0], [4, 0], [2, 4]],
        'vertical_view': [[0, 0], [4, 0], [4, 4]]
    },
    {
        'id': 89376,
        'front_view': [[0, 0], [6, 0], [0, 6]],
        'side_view': [[0, 0], [0, 4], [6, 4], [6, 0]],
        'vertical_view': [[0, 0], [6, 0], [0, 4], [6, 4]]
    },
    {
        'id': 89482,
        'front_view': [[0, 0], [3, 0], [3, 6], [6, 6]],
        'side_view': [[0, 0], [6, 0], [0, 3], [6, 3]],
        'vertical_view': [[0, 0], [3, 0], [6, 0], [0, 3], [3, 3], [6, 3]]
    },
    {
        'id': 21198,
        'front_view': [[0, 0], [2, 0], [4, 0], [6, 0], [2, 6], [4, 6]],
        'side_view': [[0, 0], [6, 0], [0, 5]],
        'vertical_view': [[2, 0], [4, 0], [0, 5], [6, 5]]
    },
    {
        'id':21684,
        'front_view': [[0, 0], [1, 0], [2, 0], [0, 2], [1, 2], [2, 2]],
        'side_view': [[0, 0], [2, 0], [0, 2], [2, 1], [2, 2]],
        'vertical_view': [[0, 0], [2, 0], [0, 1], [0, 2], [1, 2]]
    }
]
x = symbols('x')
for shuru_view in shuru:
    view = [[], [], []]
    for i in shuru_view['front_view']:
        view[2].append([i[0], i[1], x])
    print(shuru_view['id'])
    for i in shuru_view['side_view']:
        view[0].append([x, i[0], i[1]])
    s = view[0]
    inital_view0 = copy.deepcopy(view[0])
    for i in shuru_view['vertical_view']:
        view[1].append([i[0], x, i[1]])
    points = min(len(view[2]), len(view[1]), len(view[0])) * 2
    a = []
    for i in range(points):
        a.append([100, 100, 100])
    def panduan(a):
        for i in range(len(a)):
            for j in a[i]:
                if type(j) == list:
                    return True
            for j in range(i + 1, len(a)):
                if a[j] == a[i]:
                    return True
        return False
    while panduan(a):
        a = []
        for i in range(points):
            a.append([100, 100, 100])
        for i in list(itertools.combinations(s, points - len(s))):
            view[0] = copy.deepcopy(inital_view0)
            for j in i:
                view[0].append(j)
            for j in range(points):
                a[j][1], a[j][2] = view[0][j][1], view[0][j][2]
            for j in range(points):
                list3 = []
                list1 = []
                list2 = []
                for k in view[2]:
                    if a[j][1] == k[1]:
                        list1.append(k[0])
                for k in view[1]:
                    if a[j][2] == k[2]:
                        list2.append(k[0])
                list3 = list(set(list1) & set(list2))
                if len(list3) == 1:
                    a[j][0] = list3[0]
                else:
                    a[j][0] = [min(list3), max(list3)]
            for j in range(points):
                if (type(a[j][0]) == list):
                    for k in range(points):
                        if (k != j) & (a[k][1] == a[j][1]) & (a[k][2] == a[j][2]) & (type(a[k][0]) != list):
                            a[j][0] = list(set(a[j][0]) - set([a[k][0]]))[0]
                            break
                        elif (k != j) & (a[k][1] == a[j][1]) & (a[k][2] == a[j][2])& (type(a[k][0]) == list):
                            a[j][0], a[k][0] = a[j][0][0], a[j][0][1]
                            break
            if not panduan(a):
                break
        points -= 1
    print(a)
