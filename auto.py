from vehiculo import Vehiculo

class Auto(Vehiculo):
    """
    Representa un automóvil en el taller mecánico.
    """
    def __init__(self, patente: str, anio: int, capacidad_maletero: int):
        super().__init__(patente, anio)
        self.capacidad_maletero = capacidad_maletero  # Valida mediante setter

    @property
    def capacidad_maletero(self) -> int:
        """Getter para la capacidad del maletero en litros."""
        return self._capacidad_maletero

    @capacidad_maletero.setter
    def capacidad_maletero(self, valor: int) -> None:
        """Setter con validación de tipo y rango no negativo."""
        if not isinstance(valor, int):
            raise TypeError("La capacidad del maletero debe ser un entero.")
        if valor < 0:
            raise ValueError("La capacidad del maletero no puede ser negativa.")
        self._capacidad_maletero = valor

    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para Auto ($25.000)."""
        return 25000
