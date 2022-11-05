from DoubleLinkedList import DoubleLinkedList

lista = DoubleLinkedList()
lista.append(1)
lista.append("Hola")
lista.append(666)
lista.append("Elemento")
lista.append(19)
print("********Lista********\n")
print(lista)
lista.__setitem__(2, 555)
print("\n********Lista con prueba del __setitem__********\n")
print(lista)
print("\n********Prueba del __getitem__********\n")
print("__getitem__ : [3]", lista[3])
print("\n********Prueba del __delitem********\n")
del (lista[2]) 
print(lista)
print("\n********Prueba de __iter__********\n")
i = 0
for elem in iter(lista):
    print(f"lista[{i}]: {elem}")
    i += 1 