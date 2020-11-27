import numpy as np
import matplotlib.pyplot as plt
import scipy
import random
import math



user_decision = int(input("Wybierz\n 1 - by wylosować liczby\n 2 - by wprowadzic wlasne dane\n:"))
data = []
if user_decision == 1:
    min = int(input("Podaj dolny zakres przedziału losowania liczb: "))
    max = int(input("Podaj górny zakres przedziału losowania liczb: "))
    for i in range(0, 3):
        i = random.randint(min, max)
        data.append(i)
    a = data[0]
    b = data[1]
    c = data[2]
    print("Twoje dane to: ", '\na =',a,'\nb =',b,'\nc =',c)

elif user_decision == 2:
    a = int(input("Wprowadz daną 'a' "))
    b = int(input("Wprowadz daną 'b' "))
    c = int(input("Wprowadz daną 'c' "))
else:
    print("niewłaściwy wybór, spróbuj ponownie")


def writ():
    outfile = open('data.txt', 'w')
    outfile.write(str(a)+ '\n')
    outfile.write(str(b) + '\n')
    outfile.write(str(c) + '\n')
    outfile.close()

writ()
