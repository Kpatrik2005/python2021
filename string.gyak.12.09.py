"""be = input("kérek egy kisbetüt")
print(be.upper())

be = input("kérek egy nagybetöt")
print(be.lower())

for i in range(70):
    print(be,end="")

print()
print(be.ljust(70,be))

be = input("kérek egy szöveget")
if len(be)>= 12:
    if be[11] == "k":
        print("igaz")
    else:
        print("nem igaz")
              
print(be[:3])
print(be[-3:])
szo = be[:3].upper()+be[3:-3].lower()+be[-3:].upper()
print(szo)
#kérj be egy mondatot és a mondat szavait forditva ird ke pl:géza egy láda helyet éáda egy géza
be = input("kérek egy mondatot ")
#szavakra bontás
fordit=be.split(" ")
print(fordit)

#megforditás
fordit.reverse()
print(fordit)

#egyesités
print(" ".join(fordit).capitalize())"""
be = "nem és, tudok mondatot írni és nem nagyon zavar"
darab = be.replace(",","").split(" ")

db = 0
for szo in darab:
    if szo=="és":
        db +=1
if db==0:
    print("nem volt")
else:
    print(str(db)+" darab volt benne")
print((be.replace(",","")+" ").count(" és ")
