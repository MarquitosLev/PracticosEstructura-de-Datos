from data_structures.priority_queues.array_heap import ArrayHeap

class HeapQueue():

    def __init__(self) -> None:
        self.queue = ArrayHeap()

    def is_empty(self):
        return self.queue.is_empty()

    def first(self):
        return self.queue.min()

    def enqueue(self, clave, valor):
        self.queue.add(clave, valor)

# SOLO PARA PRUEBAS, BORRAR
heap = HeapQueue()

print(heap.is_empty())
heap.enqueue(1,7)
heap.enqueue(4,10)
heap.enqueue(2,1)


# Metodo de queue
print(heap.queue.min())

# Metodo de heap
print(heap.first())