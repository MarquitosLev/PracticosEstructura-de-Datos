from Empresa import Empresa
from datetime import date
from Plataforma import Plataforma
from Genero import Genero
from videojuego import Videojuego
from VideojuegosAdmin import VideojuegosAdmin

admin = VideojuegosAdmin()
emp_desa1 = Empresa("Naughty Dog")
emp_dis1 = Empresa("Sony")
juego1 = Videojuego("The Last of Us", Genero.Accion_aventuras.value, [Plataforma("PS4", False), Plataforma("PC", False)], "Historia postapocaliptica con un mundo de infectados", 5999.9, emp_desa1, emp_dis1, date(2014, 7, 29), 9.7)

emp_desa2 = Empresa("Bungie Studios")
emp_dis2 = Empresa("Microsoft")
juego2 = Videojuego("Halo 2", Genero.FPS.value, [Plataforma("Xbox", True), Plataforma("PC", False)], "Es la segunda entrega en la franquicia de Halo y su trama continúa los sucesos relatados en Halo: Combat Evolved.", 999.9, emp_desa2, emp_dis2, date(2004, 11, 9), 9.5)

admin.agregar(juego1)
admin.agregar(juego2)
print(admin)

