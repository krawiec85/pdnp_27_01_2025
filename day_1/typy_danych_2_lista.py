# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejnosć przy dodawaniu danych

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Bogdan")
lista.append("Anna")
lista.append("Maciek")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
#    0         1        2        3         4       5
#    -6        -5      -4       -3         -2      -1
print(len(lista))  # 6
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Anna

# print(lista[10]) # IndexError: list index out of range

print(lista[5])  # Maciek
print(lista[len(lista) - 1])  # Maciek
print(lista[-1])  # Maciek, ostatni element z listy
print(lista[-3])  # Bogdan

# wyświetlanie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[2:])  # [['Zenek', 'Bogdan', 'Anna', 'Maciek'] 2345
print(lista[2:5])  # ['Zenek', 'Bogdan', 'Anna'] 234

print(lista[2:16])  # ['Zenek', 'Bogdan', 'Anna', 'Maciek']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']
print(lista[10:27])  # []

# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
#    0         1        2        3         4       5
#    -6        -5      -4       -3         -2      -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4] # ['Radek', 'Tomek', 'Zenek', 'Bogdan']

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # (start, stop, krok) [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Anna'], co drugi element

print(lista[::-1])  # krok w tył, wypisana odwrócona lista
# ['Maciek', 'Anna', 'Bogdan', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu w liście na wskazanym indeksie
# zmiana na oryginalnej liście
lista[3] = "Asia"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Asia', 'Anna', 'Maciek']

# dopisanie elementu do listy we wskazanym miejscu
# insert()
lista.insert(1, "Krzysztof")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Asia', 'Anna', 'Maciek']

lista.insert(15, "Mateusz")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Asia', 'Anna', 'Maciek', 'Mateusz']

# sprawdzenie indeksu dla wskazanego elementu, zwraca pierwszy napotkany
print(lista.index("Asia"))  # index numer 4
lista.append("Asia")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Asia', 'Anna', 'Maciek', 'Mateusz', 'Asia']
print(lista.index("Asia"))  # zwraca pierwszy napotkany, 4

# usunięcie elementu po indeksie, pierwszy napotkany
lista.remove("Asia")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Anna', 'Maciek', 'Mateusz', 'Asia']

# usunięcie po indeksie pop()
# lista.pop(5)
print(lista.pop(5))  # Maciek
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Anna', 'Mateusz', 'Asia']
print(lista.pop(-3))  # Anna
print(lista.pop())  # Asia, usunie ostatni element

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista_2 = lista  # odpowiednik a = b, kopia adersu listy, kopia referencji
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Mateusz']
print(lista)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Mateusz']
lista.clear()  # usuniécie wszystkich elemntów z listy
print(lista_2)  # []
print(lista)  # []
print(lista_copy)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Mateusz']
print(id(lista_2))  # 2188283810176
print(id(lista))  # 2188283810176
print(id(lista_copy))  # 2186140024640

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)  # [54, 999, 34, 22, 12.34, 567]
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 567, 999]

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 567, 'A']
print(type(liczby))  # <class 'list'>
# liczby.sort()# TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)
lista_copy.sort()
print(lista_copy)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Mateusz']
# ['Krzysztof', 'Mateusz', 'Radek', 'Tomek', 'Zenek']

lista_copy.sort(reverse=True)
print(lista_copy)
# ['Zenek', 'Tomek', 'Radek', 'Mateusz', 'Krzysztof']

lista_copy.reverse()
print(lista_copy)
# ['Krzysztof', 'Mateusz', 'Radek', 'Tomek', 'Zenek']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 567
print(liczby)  # [54, 999, 34, 666, 12.34, 567, 'A']

# rozpakowanie sekwencji
tekst = 'Pyth on.'
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Krzysztof', 'Mateusz', 'Radek', 'Tomek', 'Zenek')
