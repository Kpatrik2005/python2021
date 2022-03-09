#megszámolás de a több is egynek számít
def ertek(darab):
    if darab == 1:
        return 500
        
f = open("penztar.txt")
kosar = []
#szoveg=f.read()
#print(szoveg)
#print(f.readline())
for sor in f:
    kosar.append(sor.strip())
f.close()

print("2.feladat")
print("A fizetések száma: " + str(kosar.count("F")))

print("Az első vásárló "+str(kosar.index("F"))+" darab árucikek vásárlása")

sorszam = int(input("Vásárlás sorszéma "))
arnev = input("Árucik neve ")
darab = int(input("Darabszám "))

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













