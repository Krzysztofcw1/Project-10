tablica = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

pozycje = []

a = tablica[0]
b = tablica[1]
c = tablica[2]

def spr_X():
    #pion
    if a[0] == "X" and b[0] == "X" and c[0] == "X":
        print("X wygrały!")
        return False
    elif a[1] == "X" and b[1] == "X" and c[1] == "X":
        print("X wygrały!")
        return False
    elif a[2] == "X" and b[2] == "X" and c[2] == "X":
        print("X wygrały!")
        return False
    #poziom
    elif a[0] == "X" and a[1] == "X" and a[2] == "X":
        print("X wygrały!")
        return False
    elif b[0] == "X" and b[1] == "X" and b[2] == "X":
        print("X wygrały!")
        return False
    elif c[0] == "X" and c[1] == "X" and c[2] == "X":
        print("X wygrały!")
        return False
    #skos
    elif a[0] == "X" and b[1] == "X" and c[2] == "X":
        print("X wygrały")
        return False
    elif a[2] == "X" and b[1] == "X" and c[0] == "X":
        print("X wygrały")
        return False

def spr_O():
    #pion
    if a[0] == "O" and b[0] == "O" and c[0] == "O":
        print("O wygrały!")
        return False
    elif a[1] == "O" and b[1] == "O" and c[1] == "O":
        print("O wygrały!")
        return False
    elif a[2] == "O" and b[2] == "O" and c[2] == "O":
        print("O wygrały!")
        return False
    # poziom
    elif a[0] == "O" and a[1] == "O" and a[2] == "O":
        print("O wygrały!")
        return False
    elif b[0] == "O" and b[1] == "O" and b[2] == "O":
        print("O wygrały!")
        return False
    elif c[0] == "O" and c[1] == "O" and c[2] == "O":
        print("O wygrały!")
        return False
    # skos
    elif a[0] == "O" and b[1] == "O" and c[2] == "O":
        print("O wygrały")
        return False
    elif a[2] == "O" and b[1] == "O" and c[0] == "0":
        print("O wygrały")
        return False


def dodaj_X():
    print()
    pole = int(input("\tPodaj pole (X): "))

    while 9 < pole or pole < 1 or pole in pozycje:
        pole = int(input("\tPodaj poprawne pole (X): "))
    pozycje.append(pole)

    if pole <= 3:
        a[pole-1] += "X"
    elif 3 < pole <= 6:
        b[pole-4] += "X"
    elif 6 < pole <= 9:
        c[pole-7] += "X"


def dodaj_O():
    print()
    pole = int(input("\tPodaj pole (O): "))

    while 9 < pole or pole < 1 or pole in pozycje:
        pole = int(input("\tPodaj poprawne pole (O): "))
    pozycje.append(pole)

    if pole <= 3:
        a[pole-1] += "O"
    elif 3 < pole <= 6:
        b[pole-4] += "O"
    elif 6 < pole <= 9:
        c[pole-7] += "O"


def wyswietl_tablice():
    print()
    for i in tablica:
        print(i)

wyswietl_tablice()
num = 0
while True:
    dodaj_X()
    num += 1
    wyswietl_tablice()
    x = spr_X()
    o = spr_O()
    if x == False:
        break
    elif o == False:
        break
    if num == 9:
        print("Remis")
        break

    dodaj_O()
    num += 1
    wyswietl_tablice()
    x = spr_X()
    o = spr_O()
    if x == False:
        break
    elif o == False:
        break
    if num == 9:
        print("Remis")
        break
