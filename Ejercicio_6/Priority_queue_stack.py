from data_structures.priority_queues.priority_queue_base import PriorityQueueBase
from data_structures.priority_queues.array_heap import ArrayHeap
from typing import Any
class PriorityQueueStack(ArrayHeap, PriorityQueueBase):

    def __init__(self) -> None:
        self.prioridades = []
        self._head = None

    def is_empty(self) -> bool:

        return len(self.prioridades) == 0

    def push(self, key: any, value: Any) -> None:

        self._head = (key, value)
        self.prioridades.append((key, value))

        
    def top(self) -> int:

        if(self.is_empty()):
            raise Exception("La pila se encuentra vacía")
        return self._head
        
    def pop(self) -> Any:

        if(self.is_empty()):
            raise Exception("La pila se encuentra vacía")

        aux = self._head
        for i in range(len(self.prioridades) - 1):
            self._head = self.prioridades[i]
        
        self.prioridades.pop(len(self.prioridades)-1)
        return aux
