from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la clase Auto heredando de la clase Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Auto
        return 25000 # Retorna el valor de la tarifa por hora específica para autos (25000)
