f=open("autok.txt")
teljes=f.read()


f.close()
#print(teljes)
teljes=teljes[0:-1]
darabok=teljes.split("\n")
print(darabok)

for egysor in darabok:
    vag=egysor.split(" ")
    print(vag[2])
