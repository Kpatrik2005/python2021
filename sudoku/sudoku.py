print("1.feladat")
filenev = "nehez.txt" #input("adja meg a file nevet")
sor = 1 #int(input("Adja meg a sorszámot"))
oszlop= 1 #int(input("adja meg az oszlop számát"))

f = open(filenev)
sorok=f.read().split("\n")[:-1]
f.close()

adatok=[]
for sor in sorok:
    adatok.append(sor.split(" "))

adatok2 = []
for sor in adatok:
    temp=[]
    for elem in sor:
        temp.append(int(elem))
tabla=adatok[:9]
lepesek=adatok[9:]
print(tabla)
print(lepesek)

