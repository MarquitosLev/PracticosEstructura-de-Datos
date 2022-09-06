from Autor import Autor
from Categoria import Categoria
from Libro import Libro

class libro_Cliente:

    def imprimir_libros(libros: list) -> None:
        for i in libros:
            print(i)

    def filtrar_por_categoria(libros: list, cat: Categoria) -> list:
        print(None)
    
    def filtrar_por_autor(libros : list, autor : Autor)-> list:
        print(None)
    
    def filtrar_por_anio(libros :  list, anio :  int)-> list:
        print(None)
