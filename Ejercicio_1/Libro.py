from Autor import Autor
from Categoria import Categoria

class Libro:
    # num_invent = 0
    # titulo = ""
    # autor= Autor
    # categoria= Categoria
    # anio_publi = 0

    def __init__(self, num_invent, titulo, Autor, Categoria, anio_publi):
        self.num_invent = num_invent
        self.titulo = titulo
        self.autor = Autor
        self.categoria = Categoria
        self.anio_publi = anio_publi

    #Retorna cadena con los atributos
    def __str__(self):
        return "- N° inventario: %s\n- Título: %s\n- Autor: %s\n- Categoria: %s\n- Anio Publicación: %s" % (self.num_invent, self.titulo, self.autor, self.categoria, self.anio_publi)

    #retorna si 2 objetos de la misma clase son iguales
    def __eq__(self, otro):
        if self.titulo == otro.titulo and self.num_invent == otro.num_invent and self.autor == otro.autor:
            return True
        else: return False
        
        
            
n1 = Libro(3, "HP", "JKR", "Fantasy", 1991)
n2 = Libro(3, "HP", "JKR", "Fantasy", 1991)
print(n1 == n2)

