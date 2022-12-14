from Empresa import Empresa
from datetime import date
from Plataforma import Plataforma
from Genero import Genero
class Videojuego:

    def __init__(self, titulo:str, genero:Genero, plataformas:list, descripcion:str, precio:float, emp_desarrolladora: Empresa, emp_distribuidora: Empresa, fecha_lanzamiento: date, ranking_metacritic: float) -> None:
            self.titulo = titulo
            self.genero = genero
            self.plataformas = plataformas
            self.descripcion = descripcion
            self.precio = precio 
            self.emp_desarrolladora = emp_desarrolladora
            self.emp_distribuidora = emp_distribuidora
            self.fecha_lanzamiento = fecha_lanzamiento
            if ranking_metacritic > 10 or ranking_metacritic < 0:
                raise ValueError("Metacritic no admitido")
            else:
                self.ranking_metacritic = ranking_metacritic

    def __str__(self) -> str:
        return "\n* Titulo: {}\n* Genero: {}\n* Plataformas: {}\n* Descripcion: {}\n* Precio: {}\n* Empresa desarrolladora: {}\n* Empresa distribuidora: {}\n* Fecha de lanzamiento: {}\n* Ranking metacritic {}\n".format(self.titulo, self.genero, self.plataformas, self.descripcion, self.precio, self.emp_desarrolladora, self.emp_distribuidora, self.fecha_lanzamiento, self.ranking_metacritic) 
    
    def __repr__(self) -> str:
         return self.__str__()
