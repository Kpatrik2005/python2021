# -*- coding: cp1250 -*-
"""import random
import math
print(random.random())
paros = random.random()*450
print(math.floor(paros))
import random
import math
ho = random.random()
print(math.floor(ho)*12)+1
i = range(0, 20)
print(i, ho)
import random
import math
darab = int(input("kérek egy számot"))
szam = []
for i in range(0, darab):
    szam.append(math.floor(random.random()*900)+100)
print(szam)
print(max(szam))
szam.sort()
print(szam)
print(szam[len(szam)-2])
szam.reverse()
print(szam[1])"""
#loto
import random
import math
golyo = []
for i in range(1, 91):
    golyo.append(i)
print(golyo)
random.random()
random.shuffle(golyo)
print(golyo)
print(golyo[0:5])
print(golyo[5:10])
