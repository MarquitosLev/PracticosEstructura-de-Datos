from abc import ABC, abstractmethod
from Plataforma import Plataforma
from Genero import Genero
from Empresa import Empresa
from videojuego import Videojuego

class VideojuegosAdminAbstract(ABC):
    def __init__(self) -> None:
        self.videojuegos = []
        
    def __len__(self) -> int:
        # Indica la cantidad de videojuegos registrados.
        # Returns: int: cantidad de elementos almacenados actualmente en videojuegos.
        return len(self.videojuegos)

    def __getitem__(self, key:int) -> Videojuego:
        #Obtiene el elemento en la posicion indicada por el key
        return self.videojuegos[key]
    
    def __delitem__(self, key: int) -> None:
        """Elimina el videojuego ubicado en la posición indicada por key."""        
        del self.videojuegos[key]

    @abstractmethod
    def __str__(self) -> str:
        """Concatena en un str todos los videojuegos del catálogo."""
        pass

    @abstractmethod    
    def agregar(self, videojuego : Videojuego) -> None:
        """Agrega el parámetro al final de videojuegos
        Args:
        videojuego (Videojuego): instancia de clase videojuego que se
        va a agregar al final de la lista de videojuegos.        """
        pass

    @abstractmethod    
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        """Devuelve los videojuegos desarrollados por la empresa pasada por parámetro."""        
        pass

    @abstractmethod    
    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        """Devuelve los videojuegos distribuídos por la empresa pasada por parámetro."""
        pass        
    
    @abstractmethod    
    def filtrar_por_genero(self, genero: Genero) -> list:
        """Devuelve los videojuegos del género pasado por parámetro. """        
        pass        
    
    @abstractmethod    
    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """        
        pass        
    
    @abstractmethod    
    def ordenar_titulo(self) -> None:
        """Ordena los videojuegos por titulo."""        
        pass                
    
    @abstractmethod    
    def ordenar_mejores_primero(self) -> None:
        """Ordena los videojuegos por ranking descendente. """     
        pass