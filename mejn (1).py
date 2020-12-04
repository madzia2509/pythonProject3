import numpy as np
import matplotlib.pyplot as plt
import scipy
import random
import math



user_decision = int(input("Wybierz\n 1 - by wylosować liczby\n 2 - by wprowadzic wlasne dane\n:"))
data = []
e = (1.6 * pow(10, -19))
uh2 = 3
if user_decision == 1:
    min = int(input("Podaj dolny zakres przedziału losowania liczb: "))
    max = int(input("Podaj górny zakres przedziału losowania liczb: "))
    for u in range(0, 1):
        uh1 = random.randint(min, max)
        u = random.randint(min, max)

elif user_decision == 2:
    try:
        uh1 = int(input("Wprowadz dana: "))
        u = int(input("wprowadzą kolejną daną: "))
    except ValueError:
        print(("Nieprawidłowe dane"))
else:
    print("niewłaściwy wybór, spróbuj ponownie")


# Wzór funkcji numer 1

ek = e * uh1

#wzór funkcji numer 2

I = uh2 * pow(u, 2)





























# def writ():
#     outfile = open('data.txt', 'w')
#     outfile.write(str(a)+ '\n')
#     outfile.write(str(b) + '\n')
#     outfile.write(str(c) + '\n')
#     outfile.close()
#
# writ()


