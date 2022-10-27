from abc import ABC, abstractmethod
from typing import Any, List, Union
from LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from data_structures.trees.binary_tree_node import BinaryTreeNode
from data_structures.trees.linked_binary_tree import LinkedBinaryTree

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        return self._search_parent(nodo1) == self._search_parent(nodo2)
    
    def hojas(self) -> List[Any]:
        hojas = []

    def internos(self) -> List[Any]:
        return super().internos()
    
    def profundidad(self, nodo: BinaryTreeNode) -> int:
        return super().profundidad(nodo)
    
    def altura(self, nodo: BinaryTreeNode) -> int:
        return super().altura(nodo)


nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
# nodo_c = BinaryTreeNode('C')
# nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
# nodo_g = BinaryTreeNode('G')
# nodo_h = BinaryTreeNode('H')
# nodo_i = BinaryTreeNode('I')
# nodo_k = BinaryTreeNode('K')
# nodo_m = BinaryTreeNode('M')
# nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()
arbol.add_left_child(None, nodo_a)
arbol.add_left_child(nodo_a, nodo_b)
arbol.add_right_child(nodo_a, nodo_f)
# arbol.add_left_child(nodo_b, nodo_c)
# arbol.add_right_child(nodo_b, nodo_d)
# arbol.add_left_child(nodo_f, nodo_g)
# arbol.add_right_child(nodo_f, nodo_k)
# arbol.add_left_child(nodo_g, nodo_h)
# arbol.add_right_child(nodo_g, nodo_i)
# arbol.add_left_child(nodo_k, nodo_m)
# arbol.add_right_child(nodo_k, nodo_n)
print(arbol.hermanos(nodo_b, nodo_f))
print(arbol._search_parent(nodo_f))
print(arbol.hojas())
print(arbol)