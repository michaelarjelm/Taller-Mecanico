from vehiculo import Vehiculo

class Camion(Vehiculo):
    """
    Representa un camión en el taller mecánico.
    """
    def __init__(self, patente: str, anio: int, capacidad_carga: int):
        super().__init__(patente, anio)
        self.capacidad_carga = capacidad_carga  # Valida mediante setter

    @property
    def capacidad_carga(self) -> int:
        """Getter para la capacidad de carga en kg."""
        return self._capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor: int) -> None:
        """Setter con validación de tipo y rango no negativo."""
        if not isinstance(valor, int):
            raise TypeError("La capacidad de carga debe ser un entero.")
        if valor < 0:
            raise ValueError("La capacidad de carga no puede ser negativa.")
        self._capacidad_carga = valor

    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para Camión ($40.000)."""
        return 40000
