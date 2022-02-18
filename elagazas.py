szam = 100
if szam > 20:
    print("nagyobb")
    print("mint 20")
if szam % 2 :
    print("páros")
else:print("páratlan")
#user bekérés
be = input("szam")
print(be)
if be % 2 == 0:
    print("páros")
else:print("páratlan")
szam = input("mégegyszam")
if szam > 10 :
    if szam % 12 == 0:
        print(str(szam))
ora = input("Hány óra van?")
if ora <= 8:
    print("jó reggelt!!")
elif ora <= 17:
    print("Jó napot")
elif ora <= 21:
    print("Jó estét!")
else :
    print("Jó északát!")

