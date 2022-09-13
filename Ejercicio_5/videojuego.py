
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

    def __str__(self):
        return "- Titulo: %s\n- Genero: %s\n- Plataformas: %s\n- Descripcion: %s\n- Precio: %s\n- Empresa desarrolladora: %s\n- Empresa distribuidora: %s\n- Fecha de lanzamiento: %s\n- Ranking metacritic" % (self.titulo, self.genero, self.plataformas, self.descripcion, self.precio, self.emp_desarrolladora, self.emp_distribuidora, self.fecha_lanzamiento, self.ranking_metacritic)