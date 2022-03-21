<<<<<<< HEAD
def ertek(darab):
    if darab == 1:
        return 500
    else:
        return darab * 400 + 150

=======
#megszámolás de a több is egynek számít
def ertek(darab):
    if darab == 1:
        return 500
        
>>>>>>> fb895628f84ab74e210a9053f0b7e1eab6f6582f
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





<<<<<<< HEAD
=======
aruindex = kosar.index(arnev)
darablista = kosar[:aruindex]
print(darablista)
vasarlasDb = darablista.count("F") + 1
print(vasarlasDb)

print("5.feladat")
print("Az első vásárlás sorszáma: " + str(vasarlasDb))

for i in range(0, len(kosar)):
    if kosar[i*-1-1]==arnev:
        utolsoindex=len(kosar)-i
        break
darablista=kosar[:utolsoindex]
vasarlasDb=darablista.count("F") + 1
print("Az utolsó vásárlás sorszáma: " + str(vasarlasDb))


voltF=False
szam = 0
for e in kosar:
    if e == arnev:
        if not voltF:
            szam=szam+1
            voltF=True
        if e == "F":
            voltF=False
print(str(szam) + "vásárlás során vettek belöle.")
            
        
print(str(vasarlasDb)) + "darab vételkor fizetendő: " + str(ertek(ertek(vasarlasDb)))

darabF=0
elozoindex=0
keresettindex=0
for i in range(0,len(kosar)):
    if kosar[i]=="F":
        darabF+=1
    if darabF==sorszam:
        elozoindex=keresetindex
        keresetindex=1
        break
print(kosar[elozoindex:keresettindex])
darabKosar=kosar[elozoindex:keresettindex]
stat={}
for e in darabKosar:
    if e in stat.keys():
        stat[e]+=1
    else:
        stat[e]=1
print(stat)














