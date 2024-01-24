#Utworz tablice 20 liczb pseudolosowych 0-50
# import random
# tablica = [random.randint(0, 50) for i in range(20)]
# print(tablica)
#Czy w tablicy znajduje sie przynajmiej 1 liczba nieparzysta?
#Czy w tablicy znajduje sie przynajmniej 1 liczba zlozona?
# def zlozona(a):
#     if a < 2:
#         return False
#     for f in range(2, int(a ** 0.5) + 1):
#         if a % f != 0:
#             return False
#     return True
# if any(zlozona(b) for b in tablica) and any(c % 2 != 0 for c in tablica):
#     print("True")
# else:
#     print("False")
#1.Do tabeli wpisz 6 marek samochodow - pytajac sie za kazdym razem uzytkownika
#2.W nowej tabeli wpisz ile ma znakow kazda nazwa
# tabela = []
# for i in range(6):
#   marka_ulubiona = input("Napisz ulubiona marke samochodow: ")
#   tabela.append(marka_ulubiona)
# print(tabela)

# tabela2 = []
# for j in tabela:
#   tabela2.append(len(j))
# print(tabela2)
