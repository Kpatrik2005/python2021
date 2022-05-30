import smsmodul
f=open("sms.txt")
sorok=f.read().split("\n")[1:-1]
f.close()
#print(sorok)
smsek=[]
for i in range(0,len(sorok)//2):
    smsek.append(smsmodul.adatok(sorok[i*2],sorok[i*2+1]))

print("2.feladat")
print(f"{smsek[-1].uzenet}")
print("{}".format(smsek[-1].uzenet))

print("3.feladat")

minindex=0
maxindex=0
for i in range(0,len(smsek)):
    if len(smsek[i].uzenet)>len(smsek[maxindex].uzenet):
        maxindex=1
    if len(smsek[i].uzenet)>len(smsek[minindex].uzenet):
        minindex=1
print("ora:{} perc:{} telefonszam:{} uzenet:{}".format(smsek[maxindex].ora,[maxindex].perc,[maxindex].telefonszam,[maxindex].uzenet))
print("ora:{} perc:{} telefonszam:{} uzenet:{}".format(smsek[minindex].ora, [minindex].perc, [minindex].telefonszam, [minindex].uzenet))
