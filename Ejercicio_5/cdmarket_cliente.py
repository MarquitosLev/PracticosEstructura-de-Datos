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

emp_desa3 = Empresa("Spike Chunsoft")
emp_dis3 = Empresa("Atari")
juego3 = Videojuego("Dragon Ball Z: Budokai Tenkaichi 3", Genero.Lucha.value, [Plataforma("PlayStation 2", True), Plataforma("PC", False)], "Es la tercera entrega del juego de lucha basado en el anime y el manga Dragon Ball de Akira Toriyama", 550.0, emp_desa3, emp_dis3, date(2007, 10, 4), 9.0)

emp_desa4 = Empresa("Konami")
emp_dis4 = Empresa("Konami")
juego4 = Videojuego("Pro Evolution Soccer 2012", Genero.Deportes.value, [Plataforma("PlayStation 2", True), Plataforma("PC", True)], "Es una de las tantas ediciones del juego de fútbol tan conocido como -Pes-", 2000.0, emp_desa4, emp_dis4, date(2011, 9, 27), 8.2)

emp_desa5 = Empresa("Ubisoft Montreal")
emp_dis5 = Empresa("Ubisoft")
juego5 = Videojuego("Assassin's Creed: Valhalla", Genero.Accion_aventuras.value, [Plataforma("PlayStation 4", True), Plataforma("PC", True)], "Ambientado en el siglo IX, el juego tiene lugar durante la invasión de Gran Bretaña por parte de los Vikingos", 7000.0, emp_desa5, emp_dis5, date(2020, 11, 10), 7.5)


admin.agregar(juego1)
admin.agregar(juego2)
admin.agregar(juego3)
admin.agregar(juego4)
admin.agregar(juego5)
#print(admin.filtrar_por_desarrolladora(emp_desa1))
#print(admin.filtrar_por_distribuidora(emp_dis2))
print(admin.filtrar_por_genero(Genero.Accion_aventuras.value))
# admin.ordenar_mejores_primero()
# admin.ordenar_titulo()
# print(admin)
# print(admin.cantidad_por_plataforma())
