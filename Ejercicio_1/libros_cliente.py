from Autor import Autor
from Categoria import Categoria
from Libro import Libro

def imprimir_libros(libros: list) -> None:
    print("{titulo:*^40}".format(titulo = "Lista de Libros"))
    for i in libros: 
        print("\n" + "*" * 40 + "\n")
        print(i)

def filtrar_por_categoria(libros: list, cat: Categoria) -> list:
    print("\n{titulo:*^40}\n".format(titulo = "Lista filtrado por Categoria"))
    lista_cat = []
    for i in libros:
        if i.categoria == cat: 
            lista_cat.append(i)
    return(lista_cat)

def filtrar_por_autor(libros : list, autor : Autor)-> list:
    print("\n{titulo:*^40}\n".format(titulo = "Lista filtrado por Autor"))
    lista_aut = []
    for i in libros:
        if i.autor == autor: 
            lista_aut.append(i)
    return lista_aut

def filtrar_por_anio(libros :  list, anio :  int)-> list:
    print("\n{titulo:*^40}\n".format(titulo = "Lista filtrado por anio"))
    lista_anio = []
    for i in libros:
        if i.anio_publi == anio: 
            lista_anio.append(i)
    return lista_anio


autor1 = Autor("Joan", "Rowling")
cate1 = Categoria("Fantasia")
l1 = Libro(7, "Harry Potter", autor1, cate1, 1991)

cate2 = Categoria("Comic")
autor2 = Autor("Jerry", "Robinson")
l2 = Libro(11, "Joker", autor2, cate2, 1940)

cate3 = Categoria("Fantasia")
autor3 = Autor("JR", "Tolkien")
l3 = Libro(13, "Señor de los anillos", autor3 ,cate3, 1996)

lista = [l1, l2, l3]

print(imprimir_libros(lista))
print(filtrar_por_anio(lista, 1991)) #imprime libros con anio de publicacion 1991
print(filtrar_por_autor(lista, autor2))  #imprime libros con autor Jerry Robinson
print(filtrar_por_categoria(lista, cate3))  #imprime libros con categoria Fantasia
