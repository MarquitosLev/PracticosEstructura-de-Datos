from logging import exception
from dequeAbstract import DequeAbstract
from typing import Any, Union
from listNode import ListNode

class Deque(DequeAbstract):
    
    def __init__(self) -> None:
        self._front : Union[ListNode, None] = None
        self._back : Union[ListNode, None] = None
        self._size : int = 0

    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Deque()"
        
        concatenacion = ""
        frente = self._front

        while frente != None:
            concatenacion += str(frente.element) + ", "
            frente = frente.next

        concatenacion = concatenacion[:len(concatenacion)-2]
        
        return f"LinkedDeque({concatenacion})"
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self) -> Any:
        if self.is_empty():
            raise Exception("No se puede retornar ya que la cola está vacía")
        
        return self._front.element

    def last(self) -> Any:

        if self.is_empty():
            raise Exception("No se puede returnar ya que la cola está vacía")

        return self._back.element
    
    def add_first(self, element: Any) -> None:

        nuevo_nodo = ListNode(element, None)
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            nuevo_nodo.next = self._front
            self._front = nuevo_nodo
        
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("Doble cola vacía")
        else:
            self._front = self._front.next
            self._size -= 1

    def add_last(self, element: Any) -> None:
        
        nuevo_nodo = ListNode(element, None)

        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next

        self._size += 1
    
    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("Doble cola vacía")
        else:
            contador = self._front
            auxiliar = None
            while contador != None:
                auxiliar = contador
                contador = contador.next
                if contador.next == None:
                    auxiliar.next = contador.next
                    break
            self._back = auxiliar
            self._size -= 1
            del contador