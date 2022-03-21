def ertek(darab):
    if darab == 1:
        return 500
    else:
        return darab * 400 + 150

f = open("penztar.txt")

kosar = []
#szoveg = f.read()
#print(szoveg)
for sor in f:
    kosar.append(sor.strip())

f.close()

print("A fizetések száma: " + str(kosar.count("F")))

print("Az első vásárló " + str(kosar.append("F")) + " darab árucikket vásárolt.")

print("A fizetések száma: " + str(kosar.count("F")))

print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")

sorszam = int(input("Vásárlás sorszáma: "))
arunev = input("Árucikk neve: ")
darab = int(input("Darabszám: "))

#A termék első indexe
aruIndex = kosar.index(arunev)
darabLista = kosar[:aruIndex]
#print(darabLista)
vasarlasDb = darabLista.count("F") + 1
#print(vasarlasDb)

print("Az első vásárlás sorszáma: " + str(vasarlasDb))

#A termék utolsó indexe
utolsoIndex = 0
for i in range(0, len(kosar)):
    if kosar[i * -1 - 1] == arunev:
        utolsoIndex = len(kosar)-i
        break
darabLista = kosar[:utolsoIndex]
vasarlasDb = darabLista.count("F") + 1
print("Az utolsó vásárlás sorszáma: " + str(vasarlasDb))

voltF = False
szam = 0
for e in kosar:
    if e == arunev:
        if not voltF:
            szam = szam + 1
            voltF = True
    if e == "F":
        voltF = False
print(str(szam) + " vásárlás során vettek belőle.")

print(str(vasarlasDb) + " darab vételekor fizetendő: " + str(ertek(vasarlasDb)))

darabF = 0
elozoIndex = 0
keresettIndex = 0
for i in range(0, len(kosar)):
    if kosar[i] == "F":
        darabF += 1
    if darabF == sorszam:
        elozoIndex = keresettIndex
        keresettIndex = i
        break

print(kosar[elozoIndex+1:keresettIndex])

if sorszam > 1:
    darabKosar = kosar[elozoIndex+1:keresettIndex]
else:
    darabKosar = kosar[elozoIndex:keresettIndex]

stat = {}
for e in darabKosar:
    if e in stat.keys():
        stat[e] += 1
    else:
        stat[e] = 1

print(stat)





