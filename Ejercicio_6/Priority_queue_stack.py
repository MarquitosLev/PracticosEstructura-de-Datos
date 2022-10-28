from data_structures.priority_queues.priority_queue_base import PriorityQueueBase
from data_structures.priority_queues.array_heap import ArrayHeap
from data_structures.linear.stacks.array_stack import ArrayStack
from data_structures.linear.stacks.linked_stack import LinkedStack
from typing import Any, List, Tuple, Union
class PriorityQueueStack(ArrayStack, LinkedStack, ArrayHeap, PriorityQueueBase):

    def push(self, elem: Any) -> None:
        """Agrega el elemento elem en el tope de la pila.

        Args:
            elem (Any): Nuevo elemento que se va agregar a la pila.
        """
        #nuevo_tope tiene como siguiente al actual tope (self._head)

        self._data.append(self._Item(elem))
        self._upheap(len(self._data) - 1)

        self._head = elem
        self._size += 1
        
    def top(self) -> int:
        """Devuelve (sin quitar) el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        return self._head.element
        
    def pop(self) -> Any:
        """Quita y devuelve el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        #Dejo en resultado el valor a devolver.
        resultado = self._head.element
        
        #Hago tope al siguiente al tope.
        self._head = self._head.next
        self._size -= 1
        
        return resultado