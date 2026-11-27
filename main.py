import jocs

while True:
    print("--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir")

    opcio = input("Opció: ")

    if opcio == "1":
        jocs.janken()
    elif opcio == "2":
        jocs.nana()
    elif opcio == "S":
        print("Adeu!")
        break
    else:
        print("Opció incorrecta")
