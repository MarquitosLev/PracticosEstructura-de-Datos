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
        
        # quitados = []
        # actual = LinkedStack.top()
        # while num >= 0:
        #     quitados.append(LinkedStack.top())
        #     LinkedStack.pop()
        #     num -= 1
        # return quitados
        pass


