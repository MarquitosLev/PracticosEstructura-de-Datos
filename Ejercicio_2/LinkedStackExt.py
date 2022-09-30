from ctypes import Union
from socket import AI_NUMERICHOST
from LinkedStack import LinkedStack
from LinkedStackExtAbstract import LinkedStackExtAbstract
from typing import Any, List

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num: int) -> List[Any]:
        """Realiza la cantidad de operaciones pop() indicada por num.
        Args:
        num (int): número de veces que se va a ejecutar pop().
        Raises:
        Exception: Arroja excepción si se invoca a pop() por cuando la estructura
        está vacía.
        Returns:
        List[Any]: lista formada por todos los topes que se quitaron de la pila.
        """
        
        tope_quitado = []
        for i in range(num):
            if not self.is_empty():    
                tope_quitado.append(self.pop())
            else: 
                raise Exception("Limite superado. La pila se encuentra vacia")
        return tope_quitado

    
    def replace_all(self, param1: Any, param2: Any) -> None:
        """Reemplaza todas las ocurrencias de param1 en la pila por param2.
        Args:
        param1 (Any): Valor a buscar/reemplazar.
        param2 (Any): Nuevo valor.
        """
        actual = self._head
        while actual:
            if actual.element == param1:
                actual.element = param2
                break
            actual = actual.next

    def exchange(self) -> None:
        """Intercambia el elemento ubicado en el tope con el más antigüo o último.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """
        #Obtencion del ultimo elemento de la pila
        actual = self._head
        while actual:
            actual = actual.next
            if actual.next == None:
                actual = actual.element
                break
            
        if not self.is_empty():
            #Intercambio del tope con lo obtenido del primer elemento ingresado
            self._head.element = actual
            pass
        else:
            raise Exception("Pila vacia. No se puede intercambiar.")