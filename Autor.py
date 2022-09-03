class Autor:
    # nombre = ""
    # apellido = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self) -> str:
        return "- Nombre: %s\n- Apellido: %s" % (self.nombre, self.apellido)
    
