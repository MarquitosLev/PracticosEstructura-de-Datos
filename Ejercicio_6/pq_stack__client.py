from Priority_queue_stack import PriorityQueueStack

ColaPrioridadPila = PriorityQueueStack()

ColaPrioridadPila.push(10, 4214)
ColaPrioridadPila.push(14, "hola")
ColaPrioridadPila.push(2, "soyBatman")
ColaPrioridadPila.push(9, 1115)
ColaPrioridadPila.push(6, "Ultimo")

print("******** top ************")
print(ColaPrioridadPila.top())
print("******** pop ************")
print(ColaPrioridadPila.pop())
print("******** pop ***********")
print(ColaPrioridadPila.pop())
print("******** top ***********")
print(ColaPrioridadPila.top())