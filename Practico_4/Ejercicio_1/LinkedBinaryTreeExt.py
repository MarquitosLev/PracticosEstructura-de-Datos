from typing import Any, List
from LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode, LinkedBinaryTree
from data_structures import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        queue = LinkedQueue()
        queue.enqueue(self._root)

        if(nodo1 == queue.first() or nodo2 == queue.first()):
            return False
        padre1 = ""
        padre2 = ""
        while (queue._front is not None):

            if(queue._front.element.left_child is not None):
                queue.enqueue(queue._front.element.left_child)

                if(queue._front.element.left_child == nodo1 or queue._front.element.left_child == nodo2):
                    padre1 = queue._front.element.element

                if(queue._front.element.right_child is not None):
                    queue.enqueue(queue._front.element.right_child)

                    if(queue._front.element.right_child == nodo1 or queue._front.element.right_child == nodo2):
                        padre2 = queue._front.element.element
                queue.dequeue()
            else:
                queue.dequeue()

        return padre1 == padre2

    def hojas(self) -> List[Any]:
        hojas = []
        queue = LinkedQueue()
        queue.enqueue(self._root)
        while queue._front is not None:
            if(queue._back is not None):
                if(queue._front.element.left_child is not None):
                    queue.enqueue(queue._front.element.left_child)
                    if(queue._front.element.right_child is not None):
                        queue.enqueue(queue._front.element.right_child)
                    queue.dequeue()
                else:
                    while(queue._front is not None):
                        if(queue._front.element.children_count() == 0): 
                            hojas.append(queue._front.element.element)  
                            queue.dequeue()
                        else:
                            break
                        if(queue.is_empty()):
                            break 
        return hojas

    def internos(self) -> List[Any]:
        """ Devuelve los elementos de los nodos que tienen padre y algún hijo.
            Returns:List[Any]: lista formada por los elementos de los nodos internos.
        """
        internos = []
        queue = LinkedQueue()
        queue.enqueue(self._root)

        while (queue._front is not None):
            # COMPRUEBA SI TIENE HIJO IZQUIERDO
            if(queue._front.element.left_child is not None):
                # AGREGA EL HIJO IZQUIERDO A LA COLA
                queue.enqueue(queue._front.element.left_child)

                # COMPRUEBA SI EL HIJO IZQUIERDO NO TENGA HIJOS
                if(queue._front.element.left_child.children_count() != 0):
                    #LO AGREGA A LA LISTA DE INTERNOS
                    internos.append(queue._front.element.left_child.element)

                # COMPRUEBA SI TIENE HIJO DERECHO
                if(queue._front.element.right_child != None):

                    # AGREGA EL HIJO DERECHO A LA COLA
                    queue.enqueue(queue._front.element.right_child)

                    # COMPRUEBA SI EL HIJO DERECHO NO TENGA HIJOS
                    if(queue._front.element.right_child.children_count() != 0):
                        # LO AGREGA A LA LISTA DE INTERNOS
                        internos.append(queue._front.element.right_child.element)

                #QUITA EL FRONT
                queue.dequeue()
            else:
                # QUITA EL FRONT SIN HIJOS Y CONTINUA ITERANDO
                queue.dequeue()
                continue 

        # RETURN LISTA INTERNOS
        return internos
                 
    def profundidad(self, nodo: BinaryTreeNode) -> int:
        """ Devuelve la longitud del camino entre la raíz y un nodo.
            Args:                       
                nodo (BinaryTreeNode): nodo del que se quiere conocer la profundidad.
            Returns:                        
                int: devuelve el número de arcos entre la raíz y nodo. 0 si nodo es la raíz.
        """
        if (self._root is None): 
            return -1
        padre = self._search_parent(nodo)
        if (not padre):
            return 0     
        profundidad = 1
        while padre:
            padre = self._search_parent(padre)

            if (not padre):
                return profundidad
            else:
                profundidad += 1
    
    def altura(self, nodo: BinaryTreeNode) -> int:
        """Retorna la longitud del camino entre nodo y la hoja más lejana.
            Args:                        
                nodo (BinaryTreeNode): nodo del que se quiere conocer la altura.
            Returns:                        
                int:Devuelve 0 en caso que nodo sea hoja, caso contrario, 
                    la cantidad de arcos entre nodo y la hoja más lejana
        """
        # Si la cantidad de hijos del nodo es 0, return 0
        if self.is_empty():
            raise Exception("Arbol vacío")

        if(nodo.children_count() == 0):
            return 0        

        # Recorre recursivamente, saca la mayor altura de toda la iteracion
        return max(self.altura(nodo.left_child), self.altura(nodo.right_child)) + 1
