class Autor:
    # nombre = ""
    # apellido = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self) -> str:
        return "- Nombre: %s\n- Apellido: %s" % (self.nombre, self.apellido)
    
    def __eq__(self, otro):
        if self.nombre == otro.nombre and self.apellido == otro.apellido:
            return True
        else: return False