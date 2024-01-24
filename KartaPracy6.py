# # Zadanie 1: Sprawdź ciąg 3 liczb - arytmetyczny, geometryczny, rosnący, malejący
def sprawdz_ciąg(a, b, c):
    if b - a == c - b:
        print("arytmetyczny - TAK")
    else:
        print("arytmetyczny - NIE")

    if b / a == c / b:
        print("geometryczny - TAK")
    else:
        print("geometryczny - NIE")

    if a < b < c:
        print("rosnący - TAK")
    else:
        print("rosnący - NIE")

    if a > b > c:
        print("malejący - TAK")
    else:
        print("malejący - NIE")

# Sprawdzenie dla ciągu podanego przez użytkownika
a, b, c = map(int, input("Podaj ciąg trzech liczb oddzielonych spacją: ").split())
sprawdz_ciąg(a, b, c)
# # Zadanie 2: Oblicz sumę liczb trzycyfrowych podzielnych przez 8 i niepodzielnych przez 16
suma = sum(x for x in range(100, 1000) if x % 8 == 0 and x % 16 != 0)
print(suma)
# # Zadanie 3: Oblicz ilość liczb czterocyfrowych będących wielokrotnościami największej liczby dwucyfrowej podzielnej przez 7
# max_dv = 98  # Największa liczba dwucyfrowa podzielna przez 7
# ilość = sum(1 for x in range(1000, 10000) if x % max_dv == 0)
# print(ilość)











# # Zadanie 4: Oblicz ilość liczb dwucyfrowych, w których cyfra dziesiątek jest przynajmniej dwa razy większa od cyfry jedności
# ilość = sum(1 for i in range(10, 100) if i // 10 >= 2 * (i % 10))
# print(ilość)

# # Zadanie 5: Oblicz sumę i ilość liczb trzycyfrowych, w których cyfra setek jest większa od sumy cyfr dziesiątek i jedności
# suma = 0
# ilość = 0
# for i in range(100, 1000):
#     setki = i // 100
#     dziesiątki = (i // 10) % 10
#     jedności = i % 10
#     if setki > dziesiątki + jedności:
#         suma += i
#         ilość += 1
# print(suma, ilość)

# # Zadanie 6: Oblicz sumę n najmniejszych liczb dwucyfrowych podzielnych przez 19
# def suma_najmniejszych_dwucyfrowych_podzielnych_przez_19(n):
#     liczba = 19
#     suma = 0
#     for _ in range(n):
#         suma += liczba
#         liczba += 19
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_najmniejszych_dwucyfrowych_podzielnych_przez_19(n)
# print(wynik)

# # Zadanie 7: Oblicz sumę n największych liczb trzycyfrowych podzielnych przez 37
# def suma_największych_trzycyfrowych_podzielnych_przez_37(n):
#     liczba = 999
#     suma = 0
#     for _ in range(n):
#         suma += liczba
#         liczba -= 37
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_największych_trzycyfrowych_podzielnych_przez_37(n)
# print(wynik)

# # Zadanie 8: Ciąg skaczący. Oblicz sumę n pierwszych elementów poniższego ciągu: 2 − 5 + 8 − 11 + 14 − 17 + 20 − ...
# def suma_ciągu_skaczącego(n):
#     suma = 0
#     for i in range(n):
#         if i % 2 == 0:
#             suma += 3 * i // 2 + 2
#         else:
#             suma -= 3 * i // 2 + 5
#     return suma
# n = 10  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_skaczącego(n)
# print(wynik)

# # Zadanie 9: Ciąg zakręcony. Oblicz iloczyn n pierwszych elementów poniższego ciągu: 1 ∗ (−2) ∗ 4 ∗ (−8) ∗ 16 ∗ (−32) ∗ ...
# def iloczyn_ciągu_zakręconego(n):
#     iloczyn = 1
#     for i in range(n):
#         if i % 2 == 0:
#             iloczyn *= 2 ** i
#         else:
#             iloczyn *= -2 ** i
#     return iloczyn
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = iloczyn_ciągu_zakręconego(n)
# print(wynik)

# # Zadanie 10: Ciąg siłaczy. Oblicz sumę n pierwszych elementów poniższego ciągu: 1! + 2! + 3! + 4! + 5! + ...
# def silnia(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * silnia(x - 1)

# def suma_ciągu_siłaczy(n):
#     suma = sum(silnia(i) for i in range(1, n + 1))
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_siłaczy(n)
# print(wynik)

# # Zadanie 11: Ciąg niebanalny1. Oblicz sumę n ułamków następującej postaci: 1/1 + 3/4 + 5/9 + 7/16 + 9/25 + ...
# def suma_ciągu_niebanalnego_1(n):
#     suma = sum((2*i + 1) / ((i+1) ** 2) for i in range(n))
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_niebanalnego_1(n)
# print(wynik)

# # Zadanie 12: Ciąg niebanalny2. Oblicz ułamek n elementów licznika i mianownika następującej postaci: 1+3+5+7+9+... / 1+4+9+16+25+...
# def suma_ciągu_niebanalnego_2(n):
#     suma_licznik = sum(2 * i + 1 for i in range(n))
#     suma_mianownik = sum((i + 1) ** 2 for i in range(n))
#     ułamek = suma_licznik / suma_mianownik
#     return ułamek
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_niebanalnego_2(n)
# print(wynik)

# # Zadanie 13: Ciąg wymagający. Oblicz sumę n ułamków następującej postaci: 2/3 + 4/10 + 6/29 + 8/66 + 10/127 + ...
# def suma_ciągu_wymagającego(n):
#     suma = sum((2*i)/(3*(i*i + 1)) for i in range(1, n + 1))
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_wymagającego(n)
# print(wynik)

# # Zadanie 14: Ciąg wymagający. Oblicz sumę n ułamków następującej postaci: 2/3 + 4/10 + 6/29 + 8/66 + 10/127 + ...
# def suma_ciągu_wymagającego(n):
#     suma = sum(((i+1)*2)/((i+1)**2 - 1) for i in range(n))
#     return suma
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = suma_ciągu_wymagającego(n)
# print(wynik)

# # Zadanie 15: Ciąg totalny. Oblicz iloczyn n ułamków następującej postaci: 3/1 * 4/3 * 5/7 * 6/15 * 7/31 * ...
# def iloczyn_ciągu_totalnego(n):
#     iloczyn = 1
#     mianownik = 1
#     for i in range(3, 3+n*2, 2):
#         iloczyn *= i
#         mianownik *= mianownik + i - 2
#     return iloczyn / mianownik
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = iloczyn_ciągu_totalnego(n)
# print(wynik)

# # Zadanie 16: Ciąg ekstremalny. Oblicz iloczyn n ułamków następującej postaci: 1/1 * 2/2 * 3/4 * 5/8 * 8/16 * ...
# def iloczyn_ciągu_ekstremalnego(n):
#     iloczyn = 1
#     mianownik = 1
#     for i in range(2, n+2):
#         licznik = i
#         mianownik *= i ** 2 // (i-1)
#         iloczyn *= licznik / mianownik
#     return iloczyn
# n = 5  # Możesz zmienić na dowolną liczbę elementów
# wynik = iloczyn_ciągu_ekstremalnego(n)
# print(wynik)
