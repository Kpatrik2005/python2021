import random
f = open("ajto.txt")
kodok=[]
for egysor in f:
    kodok.append(egysor[:-1])
    
f.close()

print(kodok)

#239451
print("2.feladat")
be=input("Adja meg,mi nyitja a zárt")

print("3.feladat")

sorszam = 1
talalat = []
for kod in kodok:
    if kod == be:
        talalat.append(sorszam)
    sorszam+=1
print("A nyitó kodszámok sorai"+" ".join(str(e) for e in talalat))

talalat = []
for index,kod in enumerate(kodok,1):
    if kod == be:
        talalat.append(index)
    
print("A nyitó kodszámok sorai"+" ".join(str(e) for e in talalat))

print("4.feladat")

dupla = []
for index,kod in enumerate(kodok, 1):
    for karakter in kod:
        if kod.count(karakter) > 1:
            dupla.append(index)

if len(dupla) > 0:
    print(dupla[0])
else:
    print("Nem volt")

print("5.feladat")

ujkod = ""
valaszthato = ["0","1","2","3","4","5","6","7","8","9"]
while len(ujkod)<len(be):
    szam=random.randint(0, len(valaszthato)-1)
    ujkod+=valaszthato[szam]
    valaszthato.pop(szam)
print("Egy "+str(len(ujkod))+" hooszu kodszam "+ujkod)
