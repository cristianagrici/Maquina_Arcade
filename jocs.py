import random


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
