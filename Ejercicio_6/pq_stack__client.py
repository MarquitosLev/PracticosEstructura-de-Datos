from Priority_queue_stack import PriorityQueueStack

ColaPrioridadPila = PriorityQueueStack()

ColaPrioridadPila.Push(value=10)
ColaPrioridadPila.Push(value=6)
ColaPrioridadPila.Push(value=1)
ColaPrioridadPila.Push(value=9)
ColaPrioridadPila.Push(value=2)

print(ColaPrioridadPila.Top())
print("**********************")
print(ColaPrioridadPila.Pop())
print(ColaPrioridadPila.Pop())
print(ColaPrioridadPila.Pop())
print(ColaPrioridadPila.Pop())

print("********************")
print(ColaPrioridadPila.Top())