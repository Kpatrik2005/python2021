#megszámolás de a több is egynek számít
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
