szam = 100
if szam > 20:
    print("nagyobb")
    print("mint 20")
if szam % 2 :
    print("p�ros")
else:print("p�ratlan")
#user bek�r�s
be = input("szam")
print(be)
if be % 2 == 0:
    print("p�ros")
else:print("p�ratlan")
szam = input("m�gegyszam")
if szam > 10 :
    if szam % 12 == 0:
        print(str(szam))
ora = input("H�ny �ra van?")
if ora <= 8:
    print("j� reggelt!!")
elif ora <= 17:
    print("J� napot")
elif ora <= 21:
    print("J� est�t!")
else :
    print("J� �szak�t!")

