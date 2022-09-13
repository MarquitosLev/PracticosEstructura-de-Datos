from operator import attrgetter
from marcacionesadminabstract import MarcacionesAdminAbstract
from marcacion import Marcacion
from empleado import Empleado

class Marcacionesadmin(MarcacionesAdminAbstract):

    def agregar(self, marcacion : Marcacion) -> None:
        """Agrega la marcación pasada por parámetro al final de la lista de marcaciones
        Args: marcacion (Marcacion): instancia de clase marcación que se va a agregar al final de la lista de marcaciones.
        """
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        """Devuelve todos los empleados de los que se tiene registro de marcación(no repetir
        resultados).
        Returns:
        list: lista formada por las ocurrencias únicas de
        empleados dentro de la lista de marcaciones
        """
        #Crea una lista en la que ningún objeto está repetido y luego la retorna
        empleados_registrados = []
        for marcaciones in self.marcaciones:
            if marcaciones not in self.marcaciones:
                empleados_registrados.append(marcaciones)
        return empleados_registrados
         
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        """Devuelve todas las marcaciones de un empleado."""
        for i in self.marcaciones:
            if i.Empleado == empleado:
                return i
        
    
    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        """Devuelve todas las marcaciones del tipo especificado por parámetro."""
        for marcaciones in self.marcaciones:
            if marcaciones.Tipo == tipo.Tipo:
                return marcaciones    
    
    def llegadas_tarde(self) -> list:
        """Devuelve las marcaciones realizadas fuera del horario de ingreso."""
        pass
    
    def ordenar_legajo(self) -> None:
        """Ordena las marcaciones por legajo de empleado y luego por fecha/hora."""
        self.marcaciones.sort(key = lambda marcacion: marcacion.Empleado.Legajo)
        self.marcaciones.sort(key = lambda marcacion: marcacion.FechaHora)

    
    def ordenar_apellido_nombre(self) -> None:
        """Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora."""
        self.marcaciones.sort(key = attrgetter("Apellido", "Nombre"))
        self.marcaciones.sort(key = lambda marcacion: marcacion.FechaHora)
        