<<<<<<< HEAD
class kutya:
    def__init__(self,nev)
    self.nev = nev
egykutya = kutya()
print(egykutya.nev)
=======
#osztály definicio
class Kutya:
    #construktor
    def __init__(self,nev):
        self.nev=nev
    #osztály fügvény
    def ugat(self):
        print("vauvau")
#példányositás
k=Kutya("armagedon")
k.ugat()
print(k.nev)
#osztályváltozó értékadása
k.nev="Brunó"
print(k.nev)
#öröklés, leszármaztatás
class NemethJuhasz(Kutya):
    #uj f
    def pitiz(self):
        print(self.nev + " nein!")
    #f felülirás
    def ugat(self):
        print("WauWau")
n =NemethJuhasz("Rex")
n.ugat()
n.pitiz()

n2=NemethJuhasz("Kondér")
n2.pitiz()
>>>>>>> 1398f79fa14b3f01fda65c6400094109faf8f211
