from Mascota import Mascota
#bichitos_cliente
def imprimir(mascotas : list)-> None:
    for i in mascotas: print (i)

def filtrar_gerontes(mascotas : list)-> list:
    for i in mascotas: 
        if i.calc.edad > 12:
            print (i)

def filtrar_por_especie(mascotas : list, especie : str):
    for i in mascotas:
        if i.especie == especie:
            print(i)

#def max_mascotero(mascotas : list)-> Persona:
    print(counter.most_common(Persona))

M1 = Mascota(5, "Tobi", "Labrador", "Perro", "2010", "Messi", "Leonel", 33500541)
M2 = Mascota(10, "Garfield", "Montes", "Gato", "2017", "Ferndanez", "Karla", 3950249)
M3 = Mascota(15, "Negro", "Caniche", "Perro", "2007", "Torres", "Gabriel", 31560521)
M4 = Mascota(2, "Carlos", "Papagayo", "Loro", "2020", "Alvarez", "Julian", 41610549)
M5 = Mascota(5, "Hector", "Gris oriental", "Canguro", "2004", "Aguero", "Sergio", 33431575)
M = Mascota()
lista = [M1, M2, M3, M4, M5]

print(f.filtrar_por_anio(lista, 1991))
print(M.imprimir(lista))
print(M.filtrar_gerontes(lista))
print(M.filtrar_por_especie(lista, "Perro"))
#print(M.max_mascotero(lista))