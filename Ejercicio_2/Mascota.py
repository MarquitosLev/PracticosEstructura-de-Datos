from Persona import Persona
from Raza import Raza
class Mascota:
    
    def __init__(self, num_registro:int, nombre:str, Raza:Raza, anio_nacimiento:int, Persona:Persona):
        self.num_registro = num_registro
        self.nombre = nombre
        self.raza = Raza
        self.anio_nacimiento = anio_nacimiento
        self.persona = Persona

    def __str__(self):
        return "- N° Registro: %s\n- Nombre: %s\n- Raza: %s\n- Anio de nacimiento: %s\n- Duenio/amo %s" % (self.num_registro, self.nombre, self.raza, self.anio_nacimiento, self.persona)

    def __eq__(self, otro):
        if self.num_registro == otro.num_registro and self.nombre == otro.nombre and self.anio_nacimiento == otro.anio_nacimiento:
            return True
        else: return False    