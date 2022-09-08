#bichitos_cliente
def imprimir(mascotas : list) -> None:
    for i in mascotas: print (i)

def filtrar_gerontes(mascotas :  list)   -> list :
    for i in mascotas:
        if i.edad() >= 13:
            print(i)
