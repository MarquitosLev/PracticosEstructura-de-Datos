from operator import attrgetter
from marcacionesadminabstract import MarcacionesAdminAbstract
from marcacion import Marcacion
from empleado import Empleado
from oficina import Oficina
from marcaciontipo import MarcacionTipo
from datetime import time, datetime

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
        print("{titulo:*^40}".format(titulo = "Lista sin ningun registro repetido"))
        empleados_registrados = []
        for marcaciones in self.marcaciones:
            if marcaciones not in empleados_registrados:
                empleados_registrados.append(marcaciones)
        return empleados_registrados
         
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        """Devuelve todas las marcaciones de un empleado."""
        print("{titulo:*^40}".format(titulo = "Filtrado por empleado"))
        marcaciones_empleado = []
        for i in self.marcaciones:
            if i.Empleado == empleado:
                marcaciones_empleado.append(i)
        return marcaciones_empleado
        
    
    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        marcaciones_Portipo = []
        """Devuelve todas las marcaciones del tipo especificado por parámetro."""
        print("{titulo:*^40}".format(titulo = "Filtrado por tipo"))
        for marcaciones in self.marcaciones:
            if marcaciones.Tipo == tipo.Tipo:
                marcaciones_Portipo.append(marcaciones)
        return marcaciones_Portipo
    
    def llegadas_tarde(self) -> list:
        print("{titulo:*^40}".format(titulo = "Impuntuales"))
        llegada_tarde = []
        for marc in self.marcaciones:
            if marc.Tipo == "Entrada":
                if datetime.time(marc.FechaHora) > marc.Empleado.Oficina.HoraEntrada:  
                    llegada_tarde.append(marc)
        return llegada_tarde, print("\n" + "*" * 40 + "\n")
    
    def ordenar_legajo(self) -> None:
        """Ordena las marcaciones por legajo de empleado y luego por fecha/hora."""
        print("{titulo:*^40}".format(titulo = "Ordenado por legajo"))
        self.marcaciones.sort(key = lambda marcacion: marcacion.FechaHora)
        self.marcaciones.sort(key = lambda marcacion: marcacion.Empleado.Legajo)
    
    def ordenar_apellido_nombre(self) -> None:
        """Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora."""
        print("{titulo:*^40}".format(titulo = "Ordenado por Apellido y Nombre"))
        self.marcaciones.sort(key = lambda clave: clave.FechaHora) 
        self.marcaciones.sort(key = lambda clave: clave.Empleado.Nombre and clave.Empleado.Apellido)
        