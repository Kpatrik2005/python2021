menu_options = {
    1: "Autók adatai",
    2: "Bérlési árak",
    3: "Bérlések időpontja",
    4: "Sofőrök adatai",
    5: "Kilépés",
}

def menu1():
    print(menu_options[1])

def menu2():
    print(menu_options[2])

def menu3():
    print(menu_options[3])

def menu4():
    print(menu_options[4])

def print_menu():
    #print(menu_options)
    for menupontIndex in menu_options:
        minta = "{} --- {}"
        print(minta.format(menupontIndex, menu_options[menupontIndex]))
        #print(menu_options[menupontIndex])
    print("============================================")
    pass

print("================ Menüpontok ================")

while (True):
    print_menu()
    try:
        option = int(input("Válassz: "))
    except:
        option = "nincsilyen"
        pass

    if option == 1:
        menu1()
    elif option == 2:
        menu2()
    elif option == 3:
        menu3()
    elif option == 4:
        menu4()
    elif option == 5:
        break
    else:
        print("Nincs ilyen menüpont!")
