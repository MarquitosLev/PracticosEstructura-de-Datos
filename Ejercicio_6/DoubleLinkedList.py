from asyncio import shield
from csv import list_dialects
from operator import getitem
from typing import Any, Iterator, List
from DoubleLindedListAbstract import DoubleLinkedListAbstract
from ListNode import ListNode

class DoubleLinkedList(DoubleLinkedListAbstract):
    
    def __init__(self) -> None:
        """Crea una lista vacía"""
        self._curr: ListNode = ListNode(None)
        self._size: int = 0

    def __len__(self) -> int:
        "Tamaño de lista"
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleLinkedList()"
        cadena = ""
        n = self._curr
        while n:
            cadena += str(n.element) + ", "
            n = n.next

        cadena = cadena[:len(cadena) - 2]
        return f"DoubleLinkedList({cadena})"

    def is_empty(self) -> bool:
        "Pregunta si esta vacia"
        return self._size == 0

    def __setitem__(self, key: int, value: Any) -> None:
        if key < 0 or key >= self._size:
            raise Exception("Key fuera de rango")
        """En la posición indicada por key se va a colocar value.
        Args: key (int): posición que se va a actualizar.                        
        value (Any): nuevo valor que se va a colocar.                                        
        Raises:                        
        Exception: Arroja excepción si el índice está fuera de rango.                
        """
        cont = 0
        while self._curr is not None:
            if key == cont:
                self._curr.element = value
                break
            self._curr = self._curr.next
            cont += 1
        while self._curr.prev != None:
            self._curr = self._curr.prev

    def append(self, elem: Any) -> None:
        "Agrega un elemento al final de la lista segun parametro pasado"
        n = ListNode(elem)
        if self.is_empty():
            self._curr = n
            self._size += 1
            return
        else:
            current = self._curr
            while current.next != None: #Va al ultimo elemento de la lista enlazada
                current = current.next 
            current.next = n
            n.prev = current
        self._size += 1

    def __getitem__(self, key: int) -> Any:
        """Devuelve el elemento ubicado en la posición indicada por key.
        Args:key (int): posición de la que se va a retornar el elemento de la lista.                                        
        Raises:Exception: Arroja excepción si el índice está fuera de rango.
        Returns:Any: Devuelve el valor ubicado en la posición indicada por key."""

        if key < 0 or key >= self._size:
            raise Exception("Key fuera de rango")
        if self.is_empty():
            raise Exception("La lista esta vacia")
        
        cont = 0
        n = self._curr
        while n:
            if cont == key:
                return n.element
            n = n.next
            cont += 1


    def __delitem__(self, key: int) -> None:
        """Elimina de la estructura el elemento ubicado en la posición key.
        Args: key (int): posición cuyo nodo se va a quitar de la estructura.
        Raises: Exception: Arroja excepción si el índice está fuera de rango."""
        
        if key < 0 or key >= self._size:
            raise Exception("Key fuera de rango")
        if self.is_empty():
            raise Exception("La lista esta vacia")
        cont = 0
        n = self._curr
        while cont < key:
            n = n.next
            cont += 1
        n.prev.next = n.next


    def __iter__(self) -> Iterator[Any]:
        """ Visita desde el principio hacia el final todos los nodos de la lista y
        retorna sus elementos.
        Yields: Iterator[Any]: Cada uno de los elementos de los nodos de lista."""
        n = self._curr
        while n is not None:
            yield n.element
            n = n.next






