from data_structures.priority_queues.priority_queue_base import PriorityQueueBase
from data_structures.priority_queues.array_heap import ArrayHeap
from abc import ABC, abstractmethod
from typing import Any, Tuple
from UnsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract
class UnsortedPriorityQueueAbstract(ABC):

    """Cola de prioridad mínima no ordenada utilzando representación posicional."""
    @abstractmethod
    def __len__(self) -> int:
        return len(self._data)

    @abstractmethod
    def is_empty(self) -> bool:
        return len(self) == 0

    @abstractmethod
    def add(self, k: Any, v: Any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.
        Args:
        k (Any): Clave que determina la prioridad del ítem.
        v (Any): Valor del ítem.
        """
        pass
    @abstractmethod
    def min(self) -> Tuple[Any]:
        return min(self)

    @abstractmethod
    def remove_min(self) -> Tuple[Any]:
        """ Quita de la estructura el ítem con menor valor de clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        pass 