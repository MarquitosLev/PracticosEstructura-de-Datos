from unsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    
    def __init__(self) -> None:
        self.prioridades = []
    
    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos en la estructura.
        Returns:
        int: Cantidad de elementos en la estructura. 0 en caso que esté vacía.
        """
        return len(self.prioridades)

    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.
        Returns:
        bool: True si está vacía. False en caso contrario.
        """
        return len(self.prioridades) == 0

    def add(self, k: any, v: any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.
        Args:
        k (Any): Clave que determina la prioridad del ítem.
        v (Any): Valor del ítem.
        """
        self.prioridades.append((k, v))

    def min(self):
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de
        clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        menor_tupla = ()
        aux = 0

        """Lo que hace este primer bucle es recorrer las tuplas dentro de la lista 'self.prioridades' en busca de la clave
        'k' mas alta y luego la almacena en la variable 'aux' """

        for j in range(len(self.prioridades)):
            tupla1 = self.prioridades[j]
            if aux < tupla1[0]:
                aux = tupla1[0]

        """Lo que hace este segundo bucle es recorrer las tuplas dentro de 'self.prioridades' y compara si las claves son 

menores
        a la clave almacenada en aux. En el caso de que lo sea, aux tomará ese valor y 'var1' tomará la tupla completa"""

        for i in range(len(self.prioridades)):
            tupla2 = self.prioridades[i]
            if tupla2[0] < aux:
                aux = tupla2[0]
                menor_tupla = tupla2
        return menor_tupla


    def remove_min(self):
        """ Quita de la estructura el ítem con menor valor de clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """

        """Se asigna la menor tupla encontrada en la lista 'self.prioridades' a la variable 'menor_tupla', despues,
        Con ayuda del index(), se obtiene la posición de ésta dentro de la lista, y se la elimina con el pop()"""

        menor_tupla = self.min()
        self.prioridades.pop(self.prioridades.index(menor_tupla))
        return menor_tupla

"""Pruebas hechas antes de colocarlas en la clase Unsorted_Priority_Queque """


# colaDesordenada = UnsortedPriorityQueue()

# colaDesordenada.add(42, "hola")
# colaDesordenada.add(76, "adios")
# colaDesordenada.add(36, "Hola mundo")

# print(len(colaDesordenada))
# print(colaDesordenada.is_empty())
# print(colaDesordenada.min())
# print(colaDesordenada.remove_min())
# print(colaDesordenada.prioridades)