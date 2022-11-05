# INTEGRANTES:
    # LEANDRO GONZALEZ FISTER
    # SEBASTIAN ETCHEPARE
    # MARCOS JOEL LEIVA
    
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

emp_desa6 = Empresa("Spike Chunsoft")
emp_dis6 = Empresa("Atari")
juego6 = Videojuego("Dragon Ball Z: Budokai Tenkaichi 3", Genero.Lucha.value, [Plataforma("PlayStation 2", True), Plataforma("PC", False)], "Es la tercera entrega del juego de lucha basado en el anime y el manga Dragon Ball de Akira Toriyama", 550.0, emp_desa6, emp_dis6, date(2007, 10, 4), 9.0)

emp_desa7 = Empresa("Konami")
emp_dis7 = Empresa("Konami")
juego7 = Videojuego("Pro Evolution Soccer 2012", Genero.Deportes.value, [Plataforma("PlayStation 2", True), Plataforma("PC", True)], "Es una de las tantas ediciones del juego de fútbol tan conocido como -Pes-", 2000.0, emp_desa7, emp_dis7, date(2011, 9, 27), 8.2)

emp_desa8 = Empresa("Ubisoft Montreal")
emp_dis8 = Empresa("Ubisoft")
juego8 = Videojuego("Assassin's Creed: Valhalla", Genero.Accion_aventuras.value, [Plataforma("PlayStation 4", True), Plataforma("PC", True)], "Ambientado en el siglo IX, el juego tiene lugar durante la invasión de Gran Bretaña por parte de los Vikingos", 7000.0, emp_desa8, emp_dis8, date(2020, 11, 10), 7.5)
# emp_desa9 = Empresa("Criterion Games")
# emp_dis9 = Empresa("Electronics Arts")
# juego9 = Videojuego("Need for Speed Most Wanted", Genero.Carreras.value, [Plataforma("PlayStation", False), Plataforma("PC", False)], "Need for Speed: Most Wanted es un videojuego de carreras de la saga Need for Speed ", 1499.9, emp_desa6, emp_dis6, date(2012, 10, 30), 99.2)

# QUITAR COMENTARIO PARA EXCEPTION RANKING METACRITIC 

# Agregado a la lista de VideojuegosAdmin
admin.agregar(juego8)
admin.agregar(juego7)
admin.agregar(juego6)
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
