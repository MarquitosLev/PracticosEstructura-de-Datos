from data_structures.priority_queues.priority_queue_base import PriorityQueueBase
from data_structures.priority_queues.array_heap import ArrayHeap
from typing import Any, List, Union
from data_structures.linear.list_node import ListNode
class PriorityQueueStack(ArrayHeap, PriorityQueueBase):

    def __init__(self) -> None:
        self.prioridades = []
        self._head = 0

    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.
        Returns:
        bool: True si está vacía. False en caso contrario.
        """
        return len(self.prioridades) == 0

    def Push(self, value: Any) -> None:
        """Agrega el elemento elem en el tope de la pila.

        Args:
            elem (Any): Nuevo elemento que se va agregar a la pila.
        """
        self._head = value
        self.prioridades.append(value)

        
    def Top(self) -> int:
        """Devuelve (sin quitar) el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if(self.is_empty()):
            raise Exception("La pila se encuentra vacía")
        return self._head
        
    def Pop(self) -> Any:
        """Quita y devuelve el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if(self.is_empty()):
            raise Exception("La pila se encuentra vacía")

        aux = self._head
        for i in range(len(self.prioridades) - 1):
            self._head = self.prioridades[i]
        
        self.prioridades.pop(len(self.prioridades)-1)
        return aux
