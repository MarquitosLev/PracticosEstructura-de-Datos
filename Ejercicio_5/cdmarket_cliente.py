from Empresa import Empresa
from datetime import date
from Plataforma import Plataforma
from Genero import Genero
from videojuego import Videojuego
from VideojuegosAdmin import VideojuegosAdmin

admin = VideojuegosAdmin()
emp_desa1 = Empresa("Naughty Dog")
emp_dis1 = Empresa("Sony")
juego1 = Videojuego("The Last of Us", Genero.Accion_aventuras.value, [Plataforma("PlayStation", False), Plataforma("PC", False)], "Historia postapocaliptica con un mundo de infectados", 5999.9, emp_desa1, emp_dis1, date(2014, 7, 29), 9.7)

emp_desa2 = Empresa("Bungie Studios")
emp_dis2 = Empresa("Microsoft")
juego2 = Videojuego("Halo 2", Genero.FPS.value, [Plataforma("Xbox", True), Plataforma("PC", False)], "Es la segunda entrega en la franquicia de Halo y su trama continúa los sucesos relatados en Halo: Combat Evolved.", 999.9, emp_desa2, emp_dis2, date(2004, 11, 9), 9.5)

emp_desa3 = Empresa("Santa Monica Studios")
emp_dis3 = Empresa("Sony")
juego3 = Videojuego("God of War 3", Genero.Accion_aventuras.value, [Plataforma("PlayStation", True)], "El jugador controla al protagonista y antiguo dios de la guerra Kratos, tras su traición a manos de su padre Zeus, rey de los dioses del Olimpo.", 3599.9, emp_desa3, emp_dis3, date(2010, 3, 16), 9.6)

emp_desa4 = Empresa("Game Freak")
emp_dis4 = Empresa("Nintendo")
juego4 = Videojuego("Pokemon Diamante", Genero.RPG.value, [Plataforma("Nintendo", True)], "Unos esperados remakes en los que se ha respetado la historia original, pero que cuentan con funciones muy útiles e intuitivas propias de los juegos más recientes de Pokémon.", 16400.0, emp_desa4, emp_dis4, date(2006, 9, 28), 9.4)

emp_desa5 = Empresa("Visual Concept")
emp_dis5 = Empresa("2K Sports")
juego5 = Videojuego("NBA2K15", Genero.Deportes.value, [Plataforma("PlayStation", False), Plataforma("Xbox", False)], "NBA 2K15 es un videojuego de baloncesto de la temporada 14-15", 2499.9, emp_desa5, emp_dis5, date(2014, 10, 7), 8.7)

# emp_desa6 = Empresa("Criterion Games")
# emp_dis6 = Empresa("Electronics Arts")
# juego6 = Videojuego("Need for Speed Most Wanted", Genero.Carreras.value, [Plataforma("PlayStation", False), Plataforma("PC", False)], "Need for Speed: Most Wanted es un videojuego de carreras de la saga Need for Speed ", 1499.9, emp_desa6, emp_dis6, date(2012, 10, 30), 99.2)

# QUITAR COMENTARIO PARA EXCEPTION RANKING METACRITIC 

# Agregado a la lista de VideojuegosAdmin
admin.agregar(juego5)
admin.agregar(juego3)
admin.agregar(juego4)
admin.agregar(juego2)
admin.agregar(juego1)

# Prueba de metodos de VideojuegosAdmin
print(admin.filtrar_por_desarrolladora(Empresa("Visual Concept")))
print(admin.filtrar_por_distribuidora(Empresa("Sony")))
print(admin.filtrar_por_genero(Genero.FPS.value))
print("\n{titulo:*^80}\n".format(titulo = "Ordenado por Ranking Metacritic"))
admin.ordenar_mejores_primero()
print(admin)
print("\n{titulo:*^80}\n".format(titulo = "Ordenado por Titulo"))
admin.ordenar_titulo()
print(admin)
print(admin.cantidad_por_plataforma())
