#zad 1 lampki podłączone są szeregowo. Jeśli, któraś nie działa to nie działa cały lampkowy łańcuch. Sprawdź w tabeli 20 elementowej wypełnionej 0 lub 1 (opcjonalnie False True), reprezentującej łańcuch lampkowy.
#Policz ile jest lampek działających a ile nie - 0/False - nie działają
#Zamień wszystkie 0 na 1.

# def zadanie_1(tablica):
#   ilosc_dzial = tablica.count(1)
#   ilosc_nie_dziel = tablica.count(0)

#   print(f"Ilosc dzialajcych lampek : {ilosc_dzial}")
#   print(f"Ilosc nie dzialacych lampek{ilosc_nie_dziel}")

#   tablica = [1 if x == 0 else x for x in tablica]

#   print(f"Zamienione wszystkie 0 na 1: {tablica}")

# tablica_lamp = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0]

# zadanie_1(tablica_lamp)

#zad 2 W tym roku św. Mikołaj związał worek łańcuchem na kod. Aby otworzyć kod trzeba dwa razy podać ten sam kod. Poproś o wpisanie kodu, i ponowne wspisanie i wyświetl "Kod jest poprawny - worek otwarty" jeśli kody się zgadzają lub "próbuj jeszcze raz". Można trzy razy spróbować otworzyć worek - za trzecim razem pojawia się komunikat "Do siego roku"

# def zadanie_2():
#   kod = "aha"
#   kod2 = "oho"
#   if input("Podaj kod: ") == kod:
#     print("Kod Poprawny - Jeszcze musisz wpisać drugi kod")
#     if input("Podaj drugi kod: ") == kod2:
#       print("Dwa kody poprawne - prezent otwarty")
#   else:
#     print("Kod błedny")
      
      

# zadanie_2()


#zad 3 Narysuj choinkę
# def zadanie_3(poziomy):
#   for i in range(1, poziomy + 1):
#     print(" " * (poziomy - i) + "*" * (2 * i - 1))
# zadanie_3(5)


#zad 4 
#zad 4 Czy zasługujesz na prezenty  św. Mikołaja? Program pyta się "czy w Twoich oczach zasługujesz na prezent?" Jeśli odpowiedź jest nie (bez względu na wielkość liter) - to program "Do zobaczenia za rok"kończy zadanie,jeśli tak (bez względu na wielkość liter) to program pyta się jakiego rodzaju chcesz dostać prezent - wybierz ten, który chcesz dostać najbardziej: 1. kosmetyki, 2. ubrania, 3. gry 4. książki, 5. elektronikę, 6. inne. Program wypisuje:
# (*) Wynik zapisuje to pliku domikolaja.txt
# def zadanie_4():
#     odpowiedz = input("Czy w Twoich oczach zasługujesz na prezent? (tak/nie): ")
#     if odpowiedz.lower() == "nie":
#         print("Do zobaczenia za rok")
#     elif odpowiedz.lower() == "tak":
#         rodzaj_prezentu = input("Jakiego rodzaju chcesz dostać prezent? (1. kosmetyki, 2. ubrania, 3. gry, 4. książki, 5. elektronika, 6. inne): ")
#         with open("domikolaja.txt", "w") as plik:
#             plik.write(f"Życzenie: {rodzaj_prezentu}")

# zadanie_4()

#zad 5
# ile zostało dni do Wigilii - 24.12. *do końca nauki w tym roku
# from datetime import datetime

# def zadanie_5():
#     dzisiaj = datetime.now()
#     wigilia = datetime(dzisiaj.year, 12, 24)
#     dni_do_wigilii = (wigilia - dzisiaj).days

#     print(f"Do Wigilii zostało {dni_do_wigilii} dni")

# zadanie_5()


#zad 6
#Losuj prezent - napisz program, który wylosuje dwa rodzaje prezentów z dostępnej puli. Przykładowa pula: kosmetyki,  ubrania,  gry  książki, elektronikę,  inne. Możesz trzy razy losować, jeśli nie jesteś zadowolony z wyboru
# import random

# def zadanie_6():
#     prezenty = ["kosmetyki", "ubrania", "gry", "książki", "elektronika", "inne"]
#     for _ in range(3):
#         print("Wylosowany prezent:", random.choice(prezenty))
#         wybor = input("Czy jesteś zadowolony z wyboru? (tak/nie): ")
#         if wybor.lower() == "tak":
#             return
#     print("Nie udało się znaleźć satysfakcjonującego prezentu")

# zadanie_6()


#zad 7 
#kalkulator zakupów - najpierw podaj ile chcesz kupić produktów, a potem pytaj się o kolejną cenę produktu, na końcu podaj kwotę zakupów, kwoty można podawać po przecinku
#wersja 2 bez limitu liczby produktów - pytaj się za każdym razem czy coś jeszcze, na końcu podaj wynik
# def zadanie_7():
#     koszty = []
#     while True:
#         cena = input("Podaj cenę produktu lub wpisz 'koniec': ")
#         if cena.lower() == "koniec":
#             break
#         else:
#             koszty.append(float(cena))

#     suma = sum(koszty)
#     print(f"Suma zakupów wynosi: {suma}")

# zadanie_7()

#zad 8 
##zad 8 policz ile jest samogłosek w podanych przez użytkownika życzeniach świątecznych np. dla Wesołych Świąt podaje 5
# def zadanie_8(zyczenia):
#   samogloski = "aeiouyąę"
#   ilosc_samoglosek = sum(zyczenia.lower().count(s) for s in samogloski)
#   print(f"Ilość samogłosek w życzeniach świątecznych: {ilosc_samoglosek}")

# zyczenia = input("Podaj życzenia świąteczne: ")
# zadanie_8(zyczenia)