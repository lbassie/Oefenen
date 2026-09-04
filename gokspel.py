"""Simpel getallen-gokspel: raad het geheime getal tussen 1 en 100."""

import random


def speel():
    geheim_getal = random.randint(1, 100)
    pogingen = 0

    print("Ik denk aan een getal tussen 1 en 100. Kun jij het raden?")

    while True:
        gok = input("Jouw gok: ")

        if not gok.isdigit():
            print("Voer alsjeblieft een getal in.")
            continue

        gok = int(gok)
        pogingen += 1

        if gok < geheim_getal:
            print("Hoger!")
        elif gok > geheim_getal:
            print("Lager!")
        else:
            print(f"Goed geraden! Het was {geheim_getal}, in {pogingen} pogingen.")
            break


if __name__ == "__main__":
    speel()
