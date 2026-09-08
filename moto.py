from vehiculo import Vehiculo

class Moto(Vehiculo):
    """
    Representa una motocicleta en el taller mecánico.
    """
    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para Moto ($15.000)."""
        return 15000
