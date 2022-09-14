from empleado import Empleado
from marcaciontipo import MarcacionTipo
from datetime import datetime, time
import random
from oficina import Oficina

class Marcacion:

    def __init__(self,Empleado : Empleado, FechaHora : datetime, Tipo : MarcacionTipo):
        self.num_registro = random.randint(1, 1000)
        self.Empleado = Empleado
        self.FechaHora = FechaHora
        self.Tipo = Tipo
        self.Ultimo_numRegistro = self.num_registro
    
    def __str__(self) -> str:
        return "* Numero de registro: %s\n* Empleado: %s\n* Fecha-Hora: %s\n* Tipo: %s\n" % (self.num_registro, self.Empleado, self.FechaHora, self.Tipo)
    
    def __repr__(self) -> str:
        return self.__str__()

    #En este caso sería verificar que se trate del mismo empleado o de la misma marcación? 

    def __eq__(self, otro : object) -> bool:
        if self.num_registro == otro.num_registro and self.Empleado == otro.Empleado:
            return True
        else:
            return False
    
    @classmethod
    def guardar_numero(cls):
        cls.Ultimo_numRegistro = cls.num_registro

    @property
    def NumRegistro(self):
        try:
            return self.num_registro
        except Exception:
            print("No se puede modificar el numero de registro")
            

# ofi1 = Oficina("tukson", time(8,10), time(16,10))
# e1 = Empleado("Hola", 44624249, "González", "Leandro", ofi1)
# o1 = Marcacion(e1, datetime(2022, 9, 13, 22, 13), MarcacionTipo.Entrada.value)
# print(o1)

