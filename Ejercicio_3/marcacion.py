from empleado import Empleado
from marcaciontipo import MarcacionTipo
from datetime import datetime, time
from oficina import Oficina

class Marcacion():

    contador = 1
    ultimo_numRegistro = 0

    def __init__(self,Empleado : Empleado, FechaHora : datetime, Tipo : MarcacionTipo):
        self.__num_registro = Marcacion.contador
        self.Empleado = Empleado
        self.FechaHora = FechaHora
        self.Tipo = Tipo

        Marcacion.ultimo_numRegistro = Marcacion.contador
        Marcacion.contador = Marcacion.contador + 1;

    def __str__(self) -> str:
        return "* Numero de registro: %s\n* Empleado: %s\n* Fecha-Hora: %s\n* Tipo: %s\n" % (self.__num_registro, self.Empleado, self.FechaHora, self.Tipo)
    
    def __repr__(self) -> str:
        return self.__str__()

    #En este caso sería verificar que se trate del mismo empleado o de la misma marcación? 

    def __eq__(self, otro : object) -> bool:
        if self.num_registro == otro.num_registro and self.Empleado == otro.Empleado:
            return True
        else:
            return False

    @property
    def NumeroRegistro(self) -> int:
        return self.__num_registro
    
    @NumeroRegistro.setter
    def NumRegistro(self, valor : int) -> None:
        raise ValueError("No se puede modificar el número de registro.")
            
#Estas son pruebas que utilicé para saber si todo iba bien. 

ofi1 = Oficina("tukson", time(8,10), time(16,10))
e1 = Empleado(10, 44624249, "González", "Leandro", ofi1)
o1 = Marcacion(e1, datetime(2022, 9, 13, 8, 13), MarcacionTipo.Entrada.value)
print(o1)
#Estos print a contianuación son los que me tiran errores. Si no, ya estaría terminado
print(o1.NumeroRegistro)
print(o1.NumeroRegistro(15))

ofi2 = Oficina("ventas", time(8,00), time(15,30))
e2 = Empleado(11, 30567894, "Fernández", "Santiago", ofi2)
o2 = Marcacion(e2, datetime(2022, 9, 13, 8, 00), MarcacionTipo.Entrada.value)
print(o2)

ofi3 = Oficina("tukson", time(8,10), time(16,10))
e3 = Empleado(12, 23456789, "Etchepare", "Sebastián", ofi3)
o3 = Marcacion(e3, datetime(2022, 9, 13, 8, 15), MarcacionTipo.Entrada.value)
print(o3)

#Este imprime el último número de registro asignado. FUNCIONA BIEN
print(Marcacion.ultimo_numRegistro)
