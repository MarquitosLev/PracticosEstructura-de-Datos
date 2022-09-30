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
        if self.isEmpty():
            return "Deque()"
        
        concatenacion = ""
        frente = self._front

        while frente != None:
            concatenacion += str(frente.element) + ", "
            frente = frente.next
        
        return f"LinkedDeque({concatenacion})"
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self) -> Any:
        if self.isEmpty():
            raise Exception("No se puede retornar ya que la cola está vacía")
        
        return self.first.element

    def last(self) -> Any:

        if self.isEmpty():
            raise Exception("No se puede returnar ya que la cola está vacía")

        return self.back.element
    
    def add_first(self, element: Any) -> None:

        nuevo_nodo = ListNode(element, None)
        if self.isEmpty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            ultimo = self._back
            self._back = nuevo_nodo
            self._front.next = self._front
            self._front = self._back
            self._back = ultimo
        
        self._size += 1

    def delete_first(self) -> None:
        if self.isEmpty():
            raise Exception("Doble cola vacía")
        else:
            self._front = self._front.next
            self._size -= 1

    def add_last(self, element: Any) -> None:
        
        nuevo_nodo = ListNode(element, None)

        if self.isEmpty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next

        self._size += 1
    
    def delete_last(self) -> None:
        if self.isEmpty():
            raise Exception("Doble cola vacía")
        else:
            elem = self._front
            while elem:
                if elem.next == self._back:
                    self._back = elem
                    self._size -= 1
                    break
                else:
                    elem = elem.next