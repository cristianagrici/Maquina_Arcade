import random
import robot


def janken():
    print("1. El primer que arribi a 3 victòries")
    print("2. Al millor de 5 rondes")
    modalitat = input("Quina modalitat vols? ")

    maquina = robot.robot()
    punts_jugador = 0
    punts_robot = 0
    ronda = 0

    while True:
        if modalitat == "1":
            if punts_jugador == 3 or punts_robot == 3:
                break
        else:
            if ronda == 5:
                break

        ronda = ronda + 1
        jugada = input("Pedra, paper o tisora? ")
        jugada_robot = maquina.playing()
        print("El robot treu", jugada_robot)

        if jugada == jugada_robot:
            print("Empat")
        elif jugada == "pedra" and jugada_robot == "tisora":
            print("Guanyes la ronda")
            punts_jugador = punts_jugador + 1
        elif jugada == "paper" and jugada_robot == "pedra":
            print("Guanyes la ronda")
            punts_jugador = punts_jugador + 1
        elif jugada == "tisora" and jugada_robot == "paper":
            print("Guanyes la ronda")
            punts_jugador = punts_jugador + 1
        else:
            print("Guanya el robot")
            punts_robot = punts_robot + 1

    print("Tu:", punts_jugador, "Robot:", punts_robot)
    if punts_jugador > punts_robot:
        print("Has guanyat la partida!")
    elif punts_robot > punts_jugador:
        print("El robot guanya la partida...")
    else:
        print("Empat")


def nana():
    secret = random.randint(1, 100)
    intents = 0
    print("Endevina el número entre 1 i 100")

    while True:
        text = input("Número: ")
        if not text.isdigit():
            print("Això no és un número")
            continue

        numero = int(text)
        intents = intents + 1

        if numero > secret:
            print("Massa alt")
        elif numero < secret:
            print("Massa baix")
        else:
            print("Molt bé! Ho has encertat en", intents, "intents")
            break
