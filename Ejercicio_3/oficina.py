from datetime import time, date, datetime

class Oficina:

    def __init__(self, Nombre : str, HoraEntrada : time, HoraSalida : time) -> None:
        self.Nombre = Nombre
        self.HoraEntrada = HoraEntrada
        self.HoraSalida = HoraSalida

    def __str__(self) -> str:
        return "\n   - Nombre: %s\n   - Hora Entrada: %s\n   - Hora Salida: %s" % (self.Nombre, self.HoraEntrada, self.HoraSalida)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if self.Nombre == otro.Nombre and self.HoraEntrada == otro.HoraEntrada and self.HoraSalida == otro.HoraSalida:
            return True
        else:
            return False
    
