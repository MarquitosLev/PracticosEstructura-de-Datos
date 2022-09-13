from empleado import Empleado
from marcaciontipo import MarcacionTipo
import datetime

class Marcacion:
    Ultimo_numRegistro = 0

    def __init__(self,  num_registro: int,Empleado : Empleado, FechaHora : datetime.datetime, Tipo : MarcacionTipo):
        self.num_registro = num_registro
        self.Empleado = Empleado
        self.FechaHora = FechaHora
        self.Tipo = Tipo
    
    def __str__(self) -> str:
        return "-Numero de registro: %s\n -Empleado: %s\n -fecha_hora: %s\n -Tipo: %s" % (self.num_registro, self.Empleado, self.fecha_hora, self.Tipo)
    
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