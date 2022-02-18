f = open("demofile.txt", "r")
for x in f:
    print(x)
    print("-", x, end="")
f.close()
