#użyj owoce.txt
with open("owoce.txt", "r") as plik:
  lista_owocow = plik.read().split()

#1. Policz ile znaków ma każdy owoc w nowej tabeli
dlugosc = [0] * len(lista_owocow)
for i in range(len(lista_owocow)):
  for j in lista_owocow[i]:
    dlugosc[i] += 1
print(dlugosc)
#2. Utwórz nowy wyraz, który powstał przez złączenie każdego pierwszego znaku każdego elementu tablicy np. dla ["ufo", "fa"] wyraz to "uf"

#3. Wypisz na ekranie, każdy z owoców pisany od tyłu np. dla kiwi -> iwik 
#4. Utwórz zmienną max_dl i owocek, która będzie przechowywać najdłuższy znaleziony element - nie korzystaj z funkcji wbudowanych - napisz algorytm szukający najdłuższego ciągu znaków
#3. Wypisz na ekranie, każdy z owoców pisany dużymi literami np. dla kiwi -> KIWI 
#5. Otwórz plik w trybie write i zapisz w nim nazwa_owocu dl_wyrazu np. ziemniak 8 - użyj wcześniej wczytanej tablicy 
