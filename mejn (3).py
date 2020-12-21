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
try:
    ek = e * uh1

except NameError:
    print("Źle zdefiniowana dana")

# x = e * uh1 - zbiór argumentow funkcji

#wzór funkcji numer 2
try:
    I = uh2 * pow(u, 2)
except NameError:
    print("Źle zdefiniowana dana")


#  x1 = uh2 * pow(u, 2) - zbiór argumentów funkcji




x = [3, 6, 8]
y = [2, 4, 7]
plt.plot(x, y, '-r', label='y=2x+1')
plt.title('tytul')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()



