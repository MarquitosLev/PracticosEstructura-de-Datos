from Especie import Especie
from Persona import Persona
from Raza import Raza
from Mascota import Mascota

def imprimir(mascotas : list)-> None:
    for i in mascotas: 
        print("\n" + "*" * 25 + "\n")
        print(i)
    return ""

def filtrar_gerontes(mascotas : list)-> list:
    for i in mascotas: 
        if i.calc_edad() > 12:
            print("\n" + "*" * 25 + "\n")
            print (i)
    return ""

def filtrar_por_especie(mascotas : list, especie : Especie):
    for i in mascotas:
        if i.especie == especie: #Como ingresar al atributo "Especie" de raza
            print("\n" + "*" * 25 + "\n")
            print(i)
    return ""

# def max_mascotero(mascotas : list)-> Persona:
#     print(counter.most_common(Persona))

especie = [Especie("Perro")]
raza = [Raza("Labrador", especie)]
persona = [Persona("Messi", "Leonel", 33500541)]
mascota1 = Mascota(10, "Tobi", raza, 2010, persona)

especie = [Especie("Gato")]
raza = [Raza("Montes", especie)]
persona = [Persona("Ferndandez", "Karla", 35520574)]
mascota2 = Mascota(11, "Garfield", raza, 2020, persona)

especie = [Especie("Perro")]
raza = [Raza("Caniche", especie)]
persona = [Persona("Perez", "Lucho", 38156141)]
mascota3 = Mascota(15, "Peco", raza, 2002, persona)

especie = [Especie("Loro")]
raza = [Raza("Papagayo", especie)]
persona = [Persona("Alvarez", "Julian", 40521562)]
mascota4 = Mascota(5, "Carlos", raza, 2021, persona)

especie = [Especie("Canguro")]
raza = [Raza("Gris Oriental", especie)]
persona = [Persona("Gomez", "Richard", 33500545)]
mascota5 = Mascota(20, "Hector", raza, 2008, persona)

lista = [mascota1, mascota2, mascota3, mascota4, mascota5]

print("Lista: ")
print(imprimir(lista))
print("Filtrado Gerontes: ")
print(filtrar_gerontes(lista))
print("Filtrado por especies: ")
#print(filtrar_por_especie(lista, "Perro"))
#print(m.max_mascotero(lista))