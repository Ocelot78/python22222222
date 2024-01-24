#use temp.txt
with open("temp.txt", "r") as plik:
  temp = plik.read().split()
#zad 1. ile jest temperatur poniżej 0, wyświetl wynik dla każdego zadania
# licznik = 0
# for i in temp:
#   if int(i) < 0:
#     licznik += 1
# print(licznik)
#zad 2. jaka jest najniższa temperatura - bez używania funkcji wbudowanej
# min = temp[0]
# for i in temp:
#   if int(i) < int(min):
#     min = i
# print(min)
#zad 3. jaka jest średnia temperatura - zaokrąglij do 2 miejsc po przecinku
# licz = 0
# suma = 0
# for i in temp:
#   licz += 1
#   suma += int(i)
# srednia = suma/licz
# print(round(srednia,2))
#zad 4. ile jest liczb całkowitych dodatnich
# licz2 = 0
# for i in temp:
#   if int(i) > 0:
#     licz2 += 1
# print(licz2)
#zad 5. sprawdż ile w pliku jest liczb pierwszych - utwórz dodatkowo nową tabelą z liczbami pierwszymi. Wyświetl tablicę z liczbami pierszymi i liczbę znalezionych liczb pierwszych 
# liczpierwsze = []
# licz3 = 0
# for i in temp:
#   if int(i) > 1:
#     for j in range(2, int(i)):
#       if int(i) % j == 0:
#         break
#   else:
#     licz3 += 1
#     liczpierwsze.append(i)
# print(liczpierwsze,licz3)
#zad 6. ile jest liczb, które są kwadratem liczby. np. 4 jest kwadratem liczby 2, 1 jest kwadratem 1. utwórz dodatkowo nową tabelą z tymi liczbami i oblicz ile ich jest
# from math import *
# licz4 = 0
# for i in temp:
#   if int(i) > 0:
#     for j in range(1,int(i)):
#       if int(i)**(1/j):
#         licz4 += 1
# print(licz4)

#zad 6. ile jest liczb, które są sześcianem liczby - Sześcian liczby to wynik przemnożenia trzy razy liczby przez siebie . np. 64 sześcian liczby 4. utwórz dodatkowo nową tabelą z tymi liczbami i oblicz ile ich jest
