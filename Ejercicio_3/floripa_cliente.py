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
marcacion1 = Marcacion(empleado1, datetime(2021, 6, 15, 8, 28), MarcacionTipo.Entrada.value)
marcacion2 = Marcacion(empleado2, datetime(2021, 8, 30, 16, 5), MarcacionTipo.Entrada.value)
marcacion3 = Marcacion(empleado3, datetime(2021, 1, 29, 12, 53), MarcacionTipo.Salida.value)
marcacion4 = Marcacion(empleado4, datetime(2020, 7, 25, 9, 14), MarcacionTipo.Entrada.value)
marcacion5 = Marcacion(empleado5, datetime(2020, 3, 1, 20, 20), MarcacionTipo.Salida.value)
marcacion6 = Marcacion(empleado4, datetime(2021, 9, 22, 8, 49),MarcacionTipo.Entrada.value)
marcacion7 = Marcacion(empleado2, datetime(2018, 3, 19, 16, 15),MarcacionTipo.Entrada.value)
marcacion8 = Marcacion(empleado1, datetime(2020, 6, 14, 15, 10),MarcacionTipo.Salida.value)
marcacion9 = Marcacion(empleado3, datetime(2015, 5, 20, 12, 30),MarcacionTipo.Salida.value)
marcacion10 = Marcacion(empleado5, datetime(2018, 2, 28, 15,5), MarcacionTipo.Entrada.value)
marcacion11 = Marcacion(empleado5, datetime(2021, 11, 12, 20,21),MarcacionTipo.Salida.value)
marcacion12 = Marcacion(empleado2, datetime(2017, 10, 19, 22,36),MarcacionTipo.Salida.value)
marcacion13 = Marcacion(empleado3, datetime(2019, 3, 2, 12, 56),MarcacionTipo.Salida.value)
marcacion14 = Marcacion(empleado2, datetime(2020, 5, 20, 16, 6), MarcacionTipo.Entrada.value)
marcacion15 = Marcacion(empleado3, datetime(2022, 1, 9, 9, 42), MarcacionTipo.Entrada.value)

admin = Marcacionesadmin()

admin.agregar(marcacion1)
admin.agregar(marcacion2)
admin.agregar(marcacion3) #Repetido para probar admin.empleados()
admin.agregar(marcacion4)
admin.agregar(marcacion5)
admin.agregar(marcacion6)
admin.agregar(marcacion7)
admin.agregar(marcacion8)
admin.agregar(marcacion9)
admin.agregar(marcacion10)
admin.agregar(marcacion11)
admin.agregar(marcacion12)
admin.agregar(marcacion13)
admin.agregar(marcacion14)
admin.agregar(marcacion15)


admin.ordenar_apellido_nombre() #Ya anda
# admin.ordenar_legajo() #Ya anda
# print(admin.llegadas_tarde())
# print(admin.filtrar_por_tipo(marcacion9)) #Mismo caso con filtrar_por_empleado()
# print(admin.filtrar_por_empleado(empleado4)) #Salen repetidos en caso de que haya repetidos
# print(admin.empleados())
# print(admin)
