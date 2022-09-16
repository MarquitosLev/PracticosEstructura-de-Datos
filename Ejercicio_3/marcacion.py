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
        if self.__num_registro == otro.__num_registro and self.Empleado == otro.Empleado:
            return True
        else:
            return False

    @property
    def NumeroRegistro(self) -> int:
        return self.__num_registro
    
    @NumeroRegistro.setter
    def NumeroRegistro(self, valor : int):
        raise Exception("No se puede modificar el número de registro.")
            