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
