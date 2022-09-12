from Especie import Especie
from Persona import Persona
from Raza import Raza
from Mascota import Mascota
class bichito_cliente:
    def imprimir(self, mascotas : list)-> None:
        print("\n" + "*" * 25 + "\n")
        for i in mascotas: 
            print (i)
            print("\n" + "*" * 25 + "\n")

    def filtrar_gerontes(self, mascotas : list)-> list:
        print("\n" + "*" * 25 + "\n")
        for i in mascotas:
            a = i.calc_edad 
            if a > 12:
                print (i)

    def filtrar_por_especie(self, mascotas : list, especie : str):
        print("\n" + "*" * 25 + "\n")
        for i in mascotas:
            if i.especie == especie:
                print(i)

    #def max_mascotero(mascotas : list)-> Persona:
        #print(counter.most_common(Persona))

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
mascota3 = Mascota(15, "Peco", raza, 2015, persona)

especie = [Especie("Loro")]
raza = [Raza("Papagayo", especie)]
persona = [Persona("Alvarez", "Julian", 40521562)]
mascota4 = Mascota(5, "Carlos", raza, 2021, persona)

especie = [Especie("Canguro")]
raza = [Raza("Gris Oriental", especie)]
persona = [Persona("Messi", "Leonel", 33500541)]
mascota5 = Mascota(10, "Hector", raza, 2009, persona)

m = bichito_cliente()
lista = [mascota1, mascota2, mascota3, mascota4, mascota5
]

#print(m.calc_edad(lista, 1991))
print(m.imprimir(lista))
#print(m.filtrar_gerontes(lista))
#print(m.filtrar_por_especie(lista, "Perro"))
#print(M.max_mascotero(lista))