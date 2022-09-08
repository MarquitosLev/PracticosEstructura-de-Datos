#bichitos_cliente
from Mascota import Mascota
from Persona import Persona
from Raza import Raza

def imprimir(mascotas : list) -> None:
    for i in mascotas: print (i)

def filtrar_gerontes(mascotas :  list)   -> list :
    for i in mascotas:
        if i.edad >= 13:
            print(i)

n = Mascota(5, "Tobby", "Salchi", 2000, "Mica")
print(n.edad)
print(filtrar_gerontes([n]))
