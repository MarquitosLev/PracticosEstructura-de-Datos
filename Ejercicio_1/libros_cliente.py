from Autor import Autor
from Categoria import Categoria
from Libro import Libro

class libro_Cliente:

    def imprimir_libros(self, libros: list) -> None:
        for i in libros: 
            print("*" * 25)
            print(i)
            
    def filtrar_por_categoria(self, libros: list, cat: Categoria) -> list:
        for i in libros:
            if i.categoria == cat: 
                print("*" * 25)
                print(i)
    
    def filtrar_por_autor(self, libros : list, autor : Autor)-> list:
        for i in libros:
            if i.autor == autor: 
                print("*" * 25)
                print(i)
    
    def filtrar_por_anio(self, libros :  list, anio :  int)-> list:
        for i in libros:
            if i.anio_publi == anio: 
                print("*" * 25)
                print(i)

l1 = Libro(4, "HP", "JKR", "Fantasia", 1991)
l2 = Libro(11, "Joker", "El bromas", "Humor", 1996)
l3 = Libro(13, "Señor de los anillos", "JR Tolkien", "Fantasia", 1996)
f = libro_Cliente()
lista = [l1, l2, l3]
# print(f.imprimir_libros(lista))
# print(f.filtrar_por_anio(lista, 1991))
# print(f.filtrar_por_autor(lista, "JKR"))
# print(f.filtrar_por_categoria(lista, "Fantasia"))
# Quitar # para probar
