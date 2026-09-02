from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Camion(Vehiculo): # Define la clase Camion heredando de la clase Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, anio y capacidad_carga
        super().__init__(patente, anio) # Llama al constructor de la clase padre (Vehiculo) pasando patente y anio
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga recibida como un atributo privado

    def get_capacidad_carga(self) -> int: # Método getter para obtener la capacidad de carga
        return self.__capacidad_carga # Retorna el valor del atributo privado __capacidad_carga

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Camion
        return 40000 # Retorna el valor de la tarifa por hora específica para camiones (40000)
