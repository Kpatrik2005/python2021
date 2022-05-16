#nekem roszzul van kodolva a file azt is csatoltam
f = open("tancrend.txt")
adatok=f.read().split("\n")
f.close()
tancok=[]
#adatok2=[]
for i in range(0,len(adatok),3):
    tancok.append(adatok[i:i+3])
    
#print(tancok)
#adatok2.append(adatok)
#print("2.feladat \nAz elso tanc: "+ adatok2[0] + "\nAz utolso tanc: " + adatok2[-3])

print("2.feladat\nAz elso tanc: " + str(tancok[0][0]) + "\nAz utolso tanc: " + str(tancok[-1][0]))
#print("3.feladat\n" + str(len(tancok)) + " tanc volt bemutatva")

print("3.feladat\n" + str(adatok.count("samba"))+ " par táncolta el a sambat")
print("4.feladat\nVilma ezekben a tancokban szerepel:")
for e in tancok:
    if e[1] == "Vilma":
        print(e[0])
temp= []
be = input("Kérek egy táncot.")
for e in tancok:
    if e[0]==be:
        if e[1] == "Vilma":
            temp.append(e[2])
            print("Vilma " + str(temp) + "-al táncolt " + be + "-t")
            break
        else:
            print("Vilma nem táncolt " + be)
            break
#print("Vilma " + str(temp) + be + "-t")
