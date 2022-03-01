import random

#1. feladat
f = open("ajto.txt", "r")

kodok = []
for egySor in f:
    kodok.append(egySor[:-1])
    #kodok.append(egySor.strip())

f.close()

print(kodok)

#239451
#2. feladat
be = input("Adja meg, mi nyitja a zárat! ")

#3. feladat
sorszam = 1
talalat = []
for kod in kodok:
    if kod == be:
        talalat.append(sorszam)    
    sorszam += 1
    
#Számlista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

#A nyitó kódszámok sorai: 1 4 5 8 10…

#Kicsit más megoldás
talalat = []
for index,kod in enumerate(kodok, 1):
    if kod == be:
        talalat.append(index)
    
#Számlista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

#4. feladat
dupla = []
for index,kod in enumerate(kodok, 1):
    for karakter in kod:
        if kod.count(karakter) > 1:
            dupla.append(index)

if len(dupla) > 0:
    print(dupla[0])
else:
    print("Nem volt ismétlődő számjegy")

#5. feladat
ujkod = ""
valaszthato = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while len(ujkod) < len(be):
    szam = random.randint(0,len(valaszthato)-1)
    ujkod += valaszthato[szam]
    print(ujkod)
    valaszthato.pop(szam)

#5. feladat 2.0
print("Egy " + str(len(ujkod)) + " hosszú kódszám: " + ujkod)

Függvény nyit(jo, proba:karaktersorozat): logikai érték 
 egyezik:=(hossz(jo)=hossz(proba)) 
 Ha egyezik akkor 
 elteres=ascii(jo[1])-ascii(proba[1]) 
 Ciklus i:=2-től hossz(jo) 
 Ha ( elteres - (ascii(jo[i])-ascii(proba[i])) ) mod 10 <> 0 
 akkor egyezik:=hamis 
 Ciklus vége 
 Elágazás vége 
 nyit:=egyezik 
 Függvény vége 

#6. feladat
def nyit(jo, proba):
    egyezik = len(jo) == len(proba)
    if egyezik:
        elteres = ord(jo[0]) - ord(proba[0])
        for i in range(1, len(jo)):
            if (elteres - (ord(jo[i]) - ord(proba[i]))) % 10 != 0:
                egyezik = False
    return egyezik


































