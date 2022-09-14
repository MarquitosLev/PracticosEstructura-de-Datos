from empleado import Empleado
from marcacion import Marcacion
from oficina import Oficina
from datetime import datetime, time

oficina1 = Oficina("Almacenes", "8:00:00", "15:30:00")
empleado1 = Empleado(515, 40131051, "Gomez", "Santiago", oficina1)

oficina2 = Oficina("Compras", "15:00:00", "11:30:00")
empleado2 = Empleado(590, 33673517, "Leiva", "Joel", oficina2)

oficina3 = Oficina("Ventas", "10:00:00", "18:10:00")
empleado3 = Empleado(142, 20562721, "Fister", "Ricardo", oficina3)

oficina4 = Oficina("Administracion", "06:00:00", "13:20:00")
empleado4 = Empleado(251, 36163472, "Etchepare", "Sebastian", oficina4)

oficina5 = Oficina("Contable", "15:00:00", "12:00:00")
empleado5 = Empleado(710, 40134511, "Boggia", "Tomas", oficina5)

marcacion1 = Marcacion(empleado1, "", "Entrada")
marcacion2 = Marcacion(empleado2, "", "Salida")
marcacion3 = Marcacion(empleado3, "","Salida")
marcacion4 = Marcacion(empleado4, "","Salida")
marcacion5 = Marcacion(empleado5, "","Entrada")
marcacion6 = Marcacion(empleado4, "","Entrada")
marcacion7 = Marcacion(empleado2, "","Salida")
marcacion8 = Marcacion(empleado1, "","Entrada")
marcacion9 = Marcacion(empleado3, "","Salida")
marcacion10 = Marcacion(empleado5, "","Entrada")
marcacion11 = Marcacion(empleado5, "","Entrada")
marcacion12 = Marcacion(empleado2, "","Salida")
marcacion13 = Marcacion(empleado3, "","Entrada")
marcacion14 = Marcacion(empleado2, "","Salida")
marcacion15 = Marcacion(empleado3, "","Salida")
