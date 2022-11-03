from data_structures.priority_queues.array_heap import ArrayHeap

class HeapQueue():

    def __init__(self) -> None:
        self.dato = ArrayHeap()

    def __len__(self):
        return len(self.dato)

    def is_empty(self):
        return self.dato.is_empty()

    def first(self):
        return self.dato.min()

    def enqueue(self, clave, valor):
        self.dato.add(clave, valor)
    
    def dequeue(self):
        self.dato.remove_min()
