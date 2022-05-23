import math
def oszlopban_van_e(oszlop, ertek):
    for o in tabla:
        if o(oszlop) == ertek:
            return True
    return False

print("1. feladat:")
#filenev = input("Adja meg a bemeneti fájl nevét! ")
#sor = int(input("Adja meg egy sor számát! "))
#oszlop = int(input("Adja meg egy oszlop számát! "))
filenev = "nehez.txt"
sor = 7
oszlop = 7

f = open(filenev)
sorok = f.read().split("\n")[:-1]
f.close()

adatok = []
for _sor in sorok:
    adatok.append(_sor.split(" "))

adatok2 = []
for _sor in adatok:
    temp = []
    for elem in _sor:
        temp.append(int(elem))
        
    adatok2.append(temp)
    
#print(adatok)
#print(adatok2)

tabla = adatok[:9]
lepesek = adatok[9:]
#print(tabla)
#print(lepesek)

print("3. feladat:")
if tabla[sor-1][oszlop-1] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print("Az adott helyen szereplő szám: " + str(tabla[sor-1][oszlop-1]))

s = math.ceil(sor / 3) - 1
o = math.ceil(oszlop / 3)

print("A hely a(z) {} résztáblázathoz tartozik.".format(s * 3 + o))

db = 0
for s in tabla:
    print(s)
    db += s.count("0")

print("4. feladat:")
print("Az üres helyek aránya: {:.0%}".format(db / 81))

for lepes in lepesek:
    t_s = int(lepes[1])-1 #temp sor
    t_o = int(lepes[2])-1 #temp oszlop
    
    print(lepes)
    print(tabla[int(lepes[1])-1][int(lepes[2])-1])

    print(lepes[0] in [int(lepes[1])-1])
    if (tabla[int(lepes[1])-1][int(lepes[2])-1]) != "0":
        print("A helyet már kitöltötték")
    elif lepes[0] in tabla[t_s]:
        print("Az adott sorban már szerepel a szám")
    elif oszlopban_van_e(t_o, lepes[0]):
        print("Az adott oszlopban már szerepel a szám")
