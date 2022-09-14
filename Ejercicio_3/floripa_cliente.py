from marcacionesadmin import Marcacionesadmin
from marcaciontipo import MarcacionTipo
from empleado import Empleado
from marcacion import Marcacion
from oficina import Oficina
from datetime import time, datetime

#RICHARD EL LEGAJO ES ENTERO REY

oficina1 = Oficina("Almacenes", time(8,00), time(15,00))
empleado1 = Empleado(515, 40131051, "Gomez", "Santiago", oficina1)

oficina2 = Oficina("Compras", time(16,10),time(22,30))
empleado2 = Empleado(590, 33673517, "Leiva", "Joel", oficina2)

oficina3 = Oficina("Ventas", time(9,45), time(12,50))
empleado3 = Empleado(142, 20562721, "Fister", "Ricardo", oficina3)

oficina4 = Oficina("Administracion", time(9,00), time(12,30))
empleado4 = Empleado(251, 36163472, "Etchepare", "Sebastian", oficina4)

oficina5 = Oficina("Contable", time(15,15), time(20, 15))
empleado5 = Empleado(710, 40134511, "Boggia", "Tomas", oficina5)

#Me olvide agregar la hora en datetime
marcacion1 = Marcacion(empleado1, datetime(2021, 6, 15, 9, 10), MarcacionTipo.Entrada.value)
marcacion2 = Marcacion(empleado2, datetime(2021, 8, 30), MarcacionTipo.Entrada.value)
marcacion3 = Marcacion(empleado3, datetime(2020, 1, 29, 9,44), MarcacionTipo.Salida.value)
marcacion4 = Marcacion(empleado4, datetime(2021, 7, 25), MarcacionTipo.Entrada.value)
marcacion5 = Marcacion(empleado5, datetime(2020, 3, 1), MarcacionTipo.Salida.value)
marcacion6 = Marcacion(empleado4, datetime(2021, 9, 22),MarcacionTipo.Entrada.value)
marcacion7 = Marcacion(empleado2, datetime(2018, 9, 19, 15,1),MarcacionTipo.Entrada.value)
marcacion8 = Marcacion(empleado1, datetime(2020, 6, 14),MarcacionTipo.Salida.value)
marcacion9 = Marcacion(empleado3, datetime(2003, 5, 20, 9, 45),MarcacionTipo.Salida.value)
marcacion10 = Marcacion(empleado5, datetime(2018, 2, 28), MarcacionTipo.Entrada.value)
marcacion11 = Marcacion(empleado5, datetime(2021, 11, 12),MarcacionTipo.Salida.value)
marcacion12 = Marcacion(empleado2, datetime(2017, 10, 19),MarcacionTipo.Salida.value)
marcacion13 = Marcacion(empleado3, datetime(2019, 3, 2),MarcacionTipo.Salida.value)
marcacion14 = Marcacion(empleado2, datetime(2020, 5, 20), MarcacionTipo.Entrada.value)
marcacion15 = Marcacion(empleado3, datetime(2022, 1, 1), MarcacionTipo.Entrada.value)

admin = Marcacionesadmin()

admin.agregar(marcacion1)
admin.agregar(marcacion9)
admin.agregar(marcacion9) #Repetido para probar admin.empleados()
admin.agregar(marcacion3)
admin.agregar(marcacion7)


# admin.ordenar_apellido_nombre() #No funciona el ordenamiento
# admin.ordenar_legajo() 
# print(admin.llegadas_tarde())
# print(admin.filtrar_por_tipo(marcacion9)) #Mismo caso con filtrar_por_empleado()
# print(admin.filtrar_por_empleado(empleado3)) #Salen repetidos en caso de que haya repetidos
# print(admin.empleados())
# print(admin)
