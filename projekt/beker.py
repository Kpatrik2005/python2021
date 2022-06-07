# adatbekérő class
# rendszám, sofőr, indulás, megállás, tankolás

class beker:
    def __init__(self):
        pass

    def form(self):
        self.rendszam = input("Rendszám: ")
        self.sofor = input("Sofőr: ")
        self.indulkm = int(input("Indul (km): "))
        self.megallkm = int(input("Megáll (km): "))
        self.tankol = int(input("Tankolt liter (0, ha nem): "))

if __name__ == "__main__":
    adat = beker()
    adat.form()
    print("Megtett km: " + str(adat.megallkm-adat.indulkm))
    
else:
    print("Ez egy modul.")
