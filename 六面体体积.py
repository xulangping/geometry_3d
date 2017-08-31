from sympy import*
import itertools
from silengzhui import *
from mianji import *
C = [2, 2, 0]#[a3, b3, c3]
D = [0, 0, 0]
P = [2, 0, 2*sqrt(3)]
A = [4, 0, 0]
B = [4, 2, 0]
s = [P, A, B, C, D]
v = 0
for i in list(itertools.combinations(s,4)):
    v +=  sanlengzhui(i) / simplify(2)
print(v)
