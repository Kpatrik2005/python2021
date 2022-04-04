#2.verziookoi

#1. feladat:
f = open("naplo.txt")
adatok = f.read().split("\n")
f.close()

naplo = []
honap = 0
nap = 0

for e in adatok:
    if e[0] == "#":
        honap=e[2:4]
        nap==e[5:]
        print(honap)
    else:
        temp=[]
        temp.append(honap)
        temp.append(nap)
        vag= e.split(" ")
        temp.append(" ".join(vag[0:2]))
        temp.append(vag[2])
        naplo.append(temp)

print("2.feladatm \nA naploban " + str(len(naplo)) + " hiányzás van.")

igazolt = 0
for e in naplo:
    igazolt+=e[3].count("X")


igazolatlan = 0
for e in naplo:
    igazolatlan+=e[3].count("I")
print("3.feladat\nAz igazolt hiányzások száma " + str(igazolt) + ", az igazolatlan hiányzások száma " + str(igazolatlan))














