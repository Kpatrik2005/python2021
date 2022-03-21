f = open("titanic.txt")
adatok = f.read().split("\n")

f.close()
print(adatok)

print("2.feladat: "+ str(len(adatok)) + " db")

print([ int(e.split(";")[1]) + int(e.split(";")[2]) for e in adatok] + " fő")
