f1="Ide jön a szám{}"

print(f1.format("Kettő"))
print(f1.format(2))
szam=input("Kérek egy számot")
print(f1.format(szam))

f2="Ide jön valami{1}, ide meg más{0}"
print(f2.format(123,321))
      
f3=my name is {surname}. {firstname}. surname"
