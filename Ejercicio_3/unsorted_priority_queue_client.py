from unsortedPriorityQueue import UnsortedPriorityQueue

colaDesordenada = UnsortedPriorityQueue()

colaDesordenada.add(42, "hola")
colaDesordenada.add(76, "adios")
colaDesordenada.add(36, "Hola mundo")
colaDesordenada.add(43, "Hola mundo")
colaDesordenada.add(31, "Hola mundo")

print(len(colaDesordenada))
print(colaDesordenada.is_empty())
print(colaDesordenada.min())
print(colaDesordenada.remove_min())

#Esta no sería tan necesaria, es para ver si funcionó en la lista
print(colaDesordenada.prioridades)