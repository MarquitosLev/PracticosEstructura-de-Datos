from deque import Deque

client = Deque()

#Agregados a lo ultimo
client.add_last(12)
client.add_last("Hogwarts")
client.add_last("last")

#Agregados al principio
client.add_first(666)
client.add_first(422)
client.add_first("first")
print(client)

#Eliminacion del ultimo elemento
print("\nEliminacion del ultimo elemento")
client.delete_last()
print(client)

#Eliminacion del primer elemento
print("\nEliminacion del primer elemento e imprime tamaño")
client.delete_first()
print(client)

#Impresion del primer elemento
print("\nPrimer ELemento: ", client.first())

#Impresion del ultimo elemento
print("\nPrimer ELemento: ", client.last())

#Impresion del tamaño del deque
print(len(client))