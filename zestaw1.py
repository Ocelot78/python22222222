
# Zadanie 1
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej. Podaj dwa największe dzielniki otrzymanej liczby. Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr.

  



# Zadanie 2
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej.  Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr. sprawdz czy dla kliku wybranych liczb otrzymana suma dzieli się przez sumę cyfr jednej z liczb dwucyfrowej - tj. czy np. 42 +24 dzieli się przez 6



#Zadanie 3
# W liczbie trzycyfrowej została zatarta cyfra dziesiątek: 3*4. Jaka jest cyfra dziesiątek jeżeli wiadomo, że liczba ta jest podzielna przez 6 ale nie jest podzielna przez 9?
# for i in range(10):
#   x = 304 + (10*i)
#   if x%9 != 0 and x%6 == 0:
#     print(x)
#zadanie 4
#Dwucyfrowa liczba została podzielona przez sumę swoich cyfr. oblicz resztę tego działania? Sprawdź dla kilku przypadków
# def najwieszka_liczba(liczba):
#   suma = (liczba % 10) + liczba // 10
#   print(suma)
#   return liczba % suma
# print(najwieszka_liczba(12))

#Zadanie 5 
# Czy z podanych trzech boków można utworzyć trójkąt?
# def trojkat(a,b,c):
#   if a + b > c and a + c > b and b + c > a:
#     return True 
#   else:
#     return False
# print(trojkat(2,5,4))
#