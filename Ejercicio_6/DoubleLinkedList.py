from csv import list_dialects
from operator import getitem
from typing import Any, Iterator, List
from DoubleLindedListAbstract import DoubleLinkedListAbstract
from ListNode import ListNode

class DoubleLinkedList(DoubleLinkedListAbstract):
    
    def __init__(self) -> None:
        """Crea una lista vacía"""
        self._curr: ListNode = ListNode(None, None, None)
        self._size: int = 0

    def __len__(self) -> int:
        "Tamaño de lista"
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleLinkedList()"
        
        cadena = ""
        actual = self._curr #No debe ser con variable auxiliar, cambiar

        while actual:
            cadena += str(actual.element) + ", "
            actual = actual.next

        cadena = cadena[:len(cadena) - 2]
        return f"DoubleLinkedList({cadena})"

    def is_empty(self) -> bool:
        "Pregunta si esta vacia"
        return self._size == 0

    def append(self, elem: Any) -> None:
        "Agrega un elemento al final de la lista segun parametro pasado"

        if self.is_empty():
            self._curr = ListNode(elem, None, None)
            self._size += 1
            return
        else:
            current = self._curr
            while current.next is not None: #Va al ultimo elemento de la lista enlazada
                current = current.next 
            current.next = ListNode(elem)
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
        while self._curr:
            if cont == key:
                return self._curr.element
            self._curr = self._curr.next
            cont += 1

    def __delitem__(self, key: int) -> None:
        """Elimina de la estructura el elemento ubicado en la posición key.
        Args: key (int): posición cuyo nodo se va a quitar de la estructura.
        Raises: Exception: Arroja excepción si el índice está fuera de rango."""
        
        if key < 0 or key >= self._size:
            raise Exception("Key fuera de rango")
        if self.is_empty():
            raise Exception("La lista esta vacia")
        
        #Eliminacion 
        pass

    def __iter__(self) -> Iterator[Any]:
        """ Visita desde el principio hacia el final todos los nodos de la lista y
        retorna sus elementos.
        Yields: Iterator[Any]: Cada uno de los elementos de los nodos de lista."""
        self[0]
        n = self._curr
        while n is not None:
            yield n.element
            n = n.next

lista = DoubleLinkedList()
lista.append(1)
lista.append("Hola")
lista.append(666)
lista.append("Elemento")
lista.append(19)
print(lista)

#Prueba metodo __getitem__
print("__getitem__ : ", lista[3]) 

i = 0
for elem in lista:
    print(f"lista[{i}]: {elem}")
    i += 1

#Prueba metodo __getitem__ pero el nodo queda en otra posicion (Preguntar al profe)
print("__getitem__ : ", lista[3]) 






