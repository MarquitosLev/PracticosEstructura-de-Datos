# INTEGRANTES:
    # LEANDRO GONZALEZ FISTER
    # SEBASTIAN ETCHEPARE
    # MARCOS JOEL LEIVA
    
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
autor2 = Autor("Jim", "Starlin")
l2 = Libro(11, "Batman: A Death in the Family", autor2, cate2, 1988)

cate3 = Categoria("Fantasia")
autor3 = Autor("JR", "Tolkien")
l3 = Libro(13, "Señor de los anillos", autor3 ,cate3, 1996)

cate4 = Categoria("Filosofía")
autor4 = Autor("Friedrich", "Nietzsche")
l4 = Libro(15, "Así habló Saratustra", autor4, cate4, 1883)

cate5 = Categoria("Ciencia Ficción/Ficción Política")
autor5 = Autor("George", "Orwell")
l5 = Libro(16, "1984", autor5, cate5, 1949)

cate6 = Categoria("Poema")
autor6 = Autor("Edgar Allan", "Poe")
l6 = Libro(20, "El Cuervo", autor6, cate6, 1845)

lista = [l1, l2, l3, l4, l5, l6]

#Pruebas de funcionamiento: 

# print(imprimir_libros(lista))
# print(filtrar_por_anio(lista, 1940)) #imprime libros con anio de publicacion 1991
# print(filtrar_por_autor(lista, autor5))  #imprime libros con autor Jerry Robinson
# print(filtrar_por_categoria(lista, cate5))  #imprime libros con categoria Fantasia

#Pruebas del equals de cada clase: 

# print(l5 == l6)
# print(l4 == l4)
# print(cate6 == cate5)
# print(cate1 == cate1)
# print(autor1 == autor4)
# print(autor2 == autor2)