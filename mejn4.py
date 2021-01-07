import numpy as np
import matplotlib.pyplot as plt
import decimal
import webbrowser
import time
import os



decision = input("Czy wiesz co to jest zjawisko fotolelektryczne zewnętrzne? \n")

if decision == "nie":
    webbrowser.open('http://ilf.fizyka.pw.edu.pl/instrukcje/fotokomorka/')
    print("Za pół minuty Ci się wykres zależnosci napięcia hamowania od częstotliwości\n")
    time.sleep(30)


else:
    print("Za chwilę wyświetli Ci się wykres zależnosci napięcia hamowania od częstotliwości\n")
    time.sleep(5)


e = 1.6 * pow(10, -19)#c
h = 6.62 * pow(10, -34)# J * s

w_values = []
uh_vals2 = []
v_values = []



def uhv_values(start, stop, step):
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)

uh_vals = (list(uhv_values(0, 5, '0.5')))

list2 = open("dane.txt").readlines()

for a in list2:
    v_values.append(float(a))


for (a, b) in zip(uh_vals, v_values):
    w = h * b - e * a
    w_values.append(w)



for (c, d) in zip(v_values, w_values):
    uh = (h * c - d) / e
    uh_vals2.append(uh)


plt.plot(v_values, uh_vals2, label='uh = (hv - w) / e')
plt.title('Zależność napięcia hamowania od częstotliwości')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.xlabel('Częstotliwość [10^15  s^-1]')
plt.ylabel('Napięcie hamowania [V]')
plt.grid()
plt.savefig('wykres.png')
plt.show()
print("Wykres został zapisany w folderze projektu. W każdej chwili możesz do niego wrócić\n")



decision2 = input("Czy potrafisz wyznaczyć kąt nachylenia wykresu do osi X?\n")




if decision2 == "nie":
    print("Wzór potrzebny do wyznaczenia kąta to: tgα = (e * ΔUh) / ΔV \n")


    deltauh = float(input("Odczytaj wartość napięcia hamowania z wykresu i wpisz: "))

    try:
        deltav = float(input("Odczytaj  wartość częstotliwości z wykresu i wpisz: "))
        tga = (e * deltauh) / deltav
        print("Tanges alfa wynosi", tga, "\n")

    except ZeroDivisionError:
        print("Wybierz wartość różną od zera")




print("Jeżeli chcesz dowiedzieć się więcej o tym zjawisku odwiedź ten link, w którym zostały umieszczone materiału naukowe. \n")
print("https://docs.google.com/document/d/1ObinEOG7GrAc7EU3pT4tKuPlEdaiQ72IcB_CHeHHKsU/edit?fbclid=IwAR3JY29AmrnY9Jl3TDJrjw9up-lf9DFFD6mATM1qG5zxXhviUxuxIJGBWm4")

print("W poniższym dokumencie znajdują się zródła z korzystałam do stworzenia projektu")
time.sleep(10)
os.system('Bibliografia.pdf')