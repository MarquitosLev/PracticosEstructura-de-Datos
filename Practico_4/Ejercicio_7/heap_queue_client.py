from HeapQueue import HeapQueue

heap_queue = HeapQueue()

print("* Is_empty()")
print(heap_queue.is_empty())

print("\n* METODO enqueue(k, v)")
heap_queue.enqueue(5, 99)
heap_queue.enqueue(2, "Heaps")
heap_queue.enqueue(11, 3)
heap_queue.enqueue(3, "Valor")

print("\n* Tamaño de heap_queue")
print(len(heap_queue))

print("\n* METODO dequeue()")
heap_queue.dequeue()

print("\n* Tamaño de heap_queue luego del quitado")
print(len(heap_queue))

print("\n* Elemento de la raiz")
print(heap_queue.first())

print("\n* Is_empty()")
print(heap_queue.is_empty())