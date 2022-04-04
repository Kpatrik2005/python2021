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
        honap=int(e[2:4])
        nap==int(e[5:])
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
igazolt = sum([e[3].count("X") for e in naplo])

def hetnapja(honap,nap):
    napnev= ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335) 
    napsorszam = (napszam[honap-1]+nap) % 7 
    return napnev[napsorszam] 

print("5.feladat")
honap=int(input("A honap sorszáma"))
nap=int(input("A nap sorszáma"))
print("Azon a napon " + hetnapja(honap,nap) + " volt.")

print("6.feladat")
napnev=input("A nap neve=")
ora=int(input("A nap sorszáma"))
db=0
for e in naplo:
    if hetnapja(e[0],e[1])==napnev:
        if e[3][ora-1]=="X" or e[3][ora-1]=="I":
            db+=1
print("Ekkor összesen " + str(db) + "hiányzás történt.")
db = [e[3][ora-1] for e in naplo if hetnapja(e[0],e[1])==napnev]

stat={}
for e in naplo:
    if e[2] in stat.keys():
        stat[e[2]]+=e[3].count("X")+e[3].count("I")
    else:
        stat[e[2]]+=e[3].count("X")+e[3].count("I")
print(stat)


maximum=0lgép,l
        







