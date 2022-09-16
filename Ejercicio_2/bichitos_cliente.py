from Especie import Especie
from Persona import Persona
from Raza import Raza
from Mascota import Mascota

def imprimir(mascotas : list)-> None:
    print("{titulo:*^40}".format(titulo = "Lista"))
    for i in mascotas: 
        print(i)
        print("\n" + "*" * 40 + "\n")
    return ""

def filtrar_gerontes(mascotas : list)-> list: #Retorna una lista
    print("{titulo:*^40}".format(titulo = "Lista de Gerontes"))
    lista = []
    for i in mascotas: 
        if i.calc_edad() > 12:
            lista.append(i)
    return lista

def filtrar_por_especie(mascotas : list, especie : Especie):
    print("{titulo:*^40}".format(titulo = "Lista por especie"))
    for i in mascotas:
        if i.raza.especie == especie:
            print(i)
    return("\n" + "*" * 40 + "\n")

def max_mascotero(mascotas : list)-> Persona:
    print("{titulo:*^40}".format(titulo = "Maximo mascotero"))
    max = 0
    pers = Persona
    for i in mascotas:
        cont = 0
        for j in mascotas:
            if i.persona == j.persona:
                cont += 1 
        if cont > max:
            max = cont
            pers = i.persona
    return pers

especie1 = Especie("Perro")
raza1 = Raza("Labrador", especie1)
persona1 = Persona("Messi", "Leonel", 33500541)
mascota1 = Mascota(10, "Tobi", raza1, 2010, persona1)

especie2 = Especie("Gato")
raza2 = Raza("Montes", especie2)
persona2 = Persona("Ferndandez", "Karla", 35520574)
mascota2 = Mascota(11, "Garfield", raza2, 2020, persona2)

especie3 = Especie("Perro")
raza3 = Raza("Caniche", especie3)
persona3 = Persona("Messi", "Leonel", 33500541)
mascota3 = Mascota(15, "Peco", raza3, 2002, persona3)

especie4 = Especie("Loro")
raza4 = Raza("Papagayo", especie4)
persona4 = Persona("Alvarez", "Julian", 40521562)
mascota4 = Mascota(5, "Carlos", raza4, 2021, persona4)

especie5 = Especie("Canguro")
raza5 = Raza("Gris Oriental", especie5)
persona5 = Persona("Gomez", "Richard", 33500545)
mascota5 = Mascota(20, "Hector", raza5, 2008, persona5)

lista = [mascota1, mascota2, mascota3, mascota4, mascota5]

print(imprimir(lista))
print(filtrar_gerontes(lista))
print(filtrar_por_especie(lista, Especie("Perro")))
print(max_mascotero(lista))