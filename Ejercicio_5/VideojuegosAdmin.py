from videojuego import Videojuego
from VideojuegoAdminAbstract import VideojuegosAdminAbstract
from Empresa import Empresa
from Genero import Genero

class VideojuegosAdmin(VideojuegosAdminAbstract):

    def agregar(self, videojuego : Videojuego) -> None:
        """Agrega el parámetro al final de videojuegos
        Args:
        videojuego (Videojuego): instancia de clase videojuego que se
        va a agregar al final de la lista de videojuegos.        """
        self.videojuegos.append(videojuego)
    
    def __str__(self) -> str:
        """Concatena en un str todos los videojuegos del catálogo."""
        cadena = ""
        for game in self.videojuegos:
            cadena += f"| {game.titulo} |"
        return cadena
        
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        """Devuelve los videojuegos desarrollados por la empresa pasada por parámetro.""" 
        desarrolladores = [] 
        for des in self.videojuegos:
            if desarrolladora == des.emp_desarrolladora:
                desarrolladores.append(des)
        return(desarrolladores)

    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        """Devuelve los videojuegos distribuídos por la empresa pasada por parámetro."""
        distri = []
        for dis in self.videojuegos:
            if distribuidora == dis.emp_distribuidora:
                distri.append(dis)
        return(distri)

    def filtrar_por_genero(self, genero: Genero) -> list:
        """Devuelve los videojuegos del género pasado por parámetro. """  
        gender = []
        for gen in self.videojuegos:
            if genero == gen.genero:
                gender.append(gen)      
        return(gender)
     
    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """  
        lista = []
        dicc = {"PlayStation": 0, "Xbox": 0, "PC": 0, "Nintendo": 0}
        for i in self.videojuegos:
            for j in i.plataformas:
                if j.nombre == "PlayStation":
                    dicc["PlayStation"] += 1 
                if j.nombre == "Xbox":
                    dicc["Xbox"] += 1
                if j.nombre == "PC":
                    dicc["PC"] += 1
                if j.nombre == "Nintendo":
                    dicc["Nintendo"] += 1
        lista.append(dicc)
        return(lista)
                
    
    def ordenar_titulo(self) -> None:
        """Ordena los videojuegos por titulo.""" 
        self.videojuegos.sort(key=lambda juego: juego.titulo)       

    
    def ordenar_mejores_primero(self) -> None:
        """Ordena los videojuegos por ranking descendente. """    
        self.videojuegos.sort(key=lambda mejores: mejores.ranking_metacritic, reverse=True)
        