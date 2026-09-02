from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Moto(Vehiculo): # Define la clase Moto heredando de la clase Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Moto
        return 15000 # Retorna el valor de la tarifa por hora específica para motos (15000)
