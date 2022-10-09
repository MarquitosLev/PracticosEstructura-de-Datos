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
print("\n", client)

#Eliminacion del ultimo elemento
print("\nEliminacion del ultimo elemento:")
client.delete_last()
print(client)

#Eliminacion del primer elemento
print("\nEliminacion del primer elemento:")
client.delete_first()
print(client)

#Impresion del primer elemento
print("\nPrimer eLemento actual: ", client.first())

#Impresion del ultimo elemento
print("\nÚltimo eLemento actual: ", client.last())

#Impresion del tamaño del deque
print("\nTamaño final de la estructura: ", len(client), "\n")