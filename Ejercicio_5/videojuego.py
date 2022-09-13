
from datetime import datetime

class videojuego:

    def __init__(self, titulo:str, genero:Genero, plataformas:list, descripcion:str, precio:float, emp_desarrolladora: Empresa, emp_distribuidora: Empresa, fecha_lanzamiento: datetime.date, ranking_metacritic: float) -> None:
            self.titulo = titulo
            self.genero = genero
            self.plataformas = plataformas
            self.descripcion = descripcion
            self.precio = precio 
            self.emp_desarrolladora = emp_desarrolladora
            self.emp_distribuidora = emp_distribuidora
            self.fecha_lanzamiento = fecha_lanzamiento
            self.ranking_metacritic = ranking_metacritic