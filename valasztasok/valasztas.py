f=open("szavazatok.txt")
szavazat=f.read().split("\n")[:-1]
f.close()
adatok=[]
for i in szavazat:
    i.split(" ")
    adatok.append(i)
print(adatok)
#adatok=szavazat[1].split(" ")
#print(szavazat)
kepviselo= len(szavazat)
print("2.feladat")
print("A helyhatósági választáson "+str(kepviselo)+ " képviselőjelölt indult.")

be= input("Kérem a vezeték nevet")
be2= input("Kérem a lereszt nevet")

temp=0
for i in adatok:
    print(i[2])
    if be==i[2]:
        if be2==i[3]:
            print(i[2])

