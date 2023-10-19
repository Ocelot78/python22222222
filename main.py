#KartaPracy1
#Zad 1
# def kwadrat(a,b):
#   return a**2+b**2 
# print(kwadrat(int(input()),int(input())))
#Zad 2
# def kwadrat_sumy(a,b):
#   return (a+b)**2
# print(kwadrat_sumy(int(input()),int(input())))
#Zad 3
# def roznica(a,b):
#   return (a-b)**3
# print(roznica(int(input()),int(input())))
#Zad 4
# def iloczyn_3(a,b,c):
#   return a*b*c
# print(iloczyn_3(int(input()),int(input()),int(input())))
#Zad 5
# def sumy_20(a,b):
#   print(2*(a+b)/5)
#   print((a+b)*0,4)
# print(sumy_20(float(input()),float(input())))
#Zad 6
# def VAT(brutto):
#   return brutto*1.23
# print(VAT(int(input())))
#Zad 7
# def reszta(a,b):
#   return a%b
# print(reszta(int(input()),int(input())))
#KartaPracy 2
#Zad 1
# def podziel_3(a):
#   if a % 3 == 0:
#     return True
#   else:
#     return False
# print(podziel_3(int(input())))
#Zad 2
# def podziel_17(a):
#   if a % 17 == 0 and a > 99 and a < 1000:
#     return True
#   else:
#     return False
# print(podziel_17(int(input())))
#Zad 3
# def  wiek(a):
#   if a >= 18:
#     return True
#   else:
#     return False
# print(wiek(int(input())))
#Zad 4
# def most(a):
#   if a > 20:
#     return False
#   else:
#     return True
# print(most(int(input())))
#Zad 5
# def miedzy(a,b,c):
#   if (a < c < b) or (b < c < a):
#     print("TAK")
#   else:
#     print("NIE")
# miedzy(a = int(input("Podaj pierwszą liczbę: ")),b = int(input("Podaj drugą liczbę: ")),c = int(input("Podaj trzecią liczbę: ")))
#Zad 6
# def czy_spelnia_mtf(a, p):
#   return True if pow(a, p - a, p) == 1 else False
# a = int(input("Podaj liczbę a: "))
# p = int(input("Podaj liczbę p: "))
# wynik = czy_spelnia_mtf(a, p)
# print(wynik)
#Zad 7
# def bajtozabka(p,k,s):
#   if p >= 0 or k >= 0 or s >= 0:
#     if (s*3)+p >= k:
#       print("TAK")
#     else:
#       print("NIE")
#   else:
#     print("NIE")
# bajtozabka(int(input()),int(input()),int(input()))
#KartaPracy 2a
#Zad 1
# def parzyste(a,b):
#   if (a+b)%2==0:
#     print("TAK")
#   else:
#     print("NIE")
# parzyste(int(input()),int(input()))
#Zad 2
# import math
# def srednie(a,g):
#   if (a + g) / 2 > math.sqrt(a * g):
#     print("TAK")
#   else:
#     print("NIE")
# srednie(float(input()),float(input()))
#Zad 3
# def rowne(k,l,m):
#   if k == l and k != m:
#     print("TAK")
#     print(f"Równe liczby to: {k} i {l}")
#   elif k == m and k != l:
#     print("TAK")
#     print(f"Równe liczby to: {k} i {m}")
#   elif l == m and l != k:
#     print("TAK")
#     print(f"Równe liczby to: {l} i {m}")
#   else:
#     print("NIE")
# rowne(int(input()),int(input()),int(input()))
#Zad 4
# def mniejsza(a,b,c,d):
#   print(min(a,b,c,d))
# mniejsza(int(input()),int(input()),int(input()),int(input()))
#Zad 5
# def trojkat(a,b,c):
#   if (a + b > c) and (a + c > b) and (b + c > a):
#     print("TAK")
#   else:
#     print("NIE")
# trojkat(int(input()),int(input()),int(input()))
# def trojkat2(a,b,c):
#   if a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or c**2 + a**2 > b**2:
#     print("Trójkąt ostrokątny")
#   elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
#     print("Trójkąt rozwarty")
#   elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
#     print("Trójkąt prostokątny")
# trojkat2(int(input()),int(input()),int(input()))
#KartaPracy 3B
#Zad 1
# def listopad():
#   for i in range(1,31):
#     print(i,end=" ")
# listopad()
#Zad 2
# def nie_cyfry():
#   for i in range(1,10):
#     if i%2 == 1:
#       print(i**2,end=" ")
# nie_cyfry()
#Zad 3
# for i in range(1000,10000):
#   if i%379 == 0:
#     print(i,end=" ")
#Zad 4
# for i in range(100,1000):
#   if i%5 == 0 or i%6 == 0 or i%11 == 0:
#     print(i,end=" ")
#Zad 5
# nliczb = int(input())
# suma = 0
# for i in range(nliczb):
#   n = int(input())
#   suma += n
# print(suma)
#Zad 6
# k = int(input())
# suma = 0
# for i in range(1,k+1):
#   if i%2 == 0:
#     suma += i
# print(suma)
#Zad 7
# m = int(input())
# suma = 0
# for i in range(10,m+1):
#   if i%2 != 0:
#     suma += i
# print(suma)
#Zad 8
# def inwestycja(W0,L):
#   wartosc = W0
#   for i in range(L):
#     wartosc += wartosc*0.03
#   print(round(wartosc))
# inwestycja(int(input()),int(input()))
#Zad 9
# def suma_liczb_konczacych_sie_21(n):
#   suma = 0
#   liczba = 21
#   for _ in range(n):
#     suma += liczba
#     liczba += 10  
#   return suma
# print(suma_liczb_konczacych_sie_21(int(input())))
