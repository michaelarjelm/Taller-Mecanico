from vehiculo import Vehiculo

class Camion(Vehiculo):
    """
    Representa un camión convencional en el taller mecánico.
    Contempla peso bruto, capacidad de carga, tarifa por hora y precio de trabajo.
    """
    def __init__(self, patente: str, anio: int, capacidad_carga: int, peso: int):
        super().__init__(patente, anio)
        self.capacidad_carga = capacidad_carga  # Valida mediante setter
        self.peso = peso                        # Valida mediante setter

    @property
    def capacidad_carga(self) -> int:
        """Getter para la capacidad de carga en kg."""
        return self._capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor: int) -> None:
        """Setter con validación de tipo y rango no negativo."""
        if not isinstance(valor, int):
            raise TypeError("La capacidad de carga debe ser un número entero.")
        if valor < 0:
            raise ValueError("La capacidad de carga no puede ser negativa.")
        self._capacidad_carga = valor

    @property
    def peso(self) -> int:
        """Getter para el peso bruto del camión en kg."""
        return self._peso

    @peso.setter
    def peso(self, valor: int) -> None:
        """Setter con validación de peso positivo."""
        if not isinstance(valor, int):
            raise TypeError("El peso del camión debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El peso del camión debe ser un valor positivo mayor a 0 kg.")
        self._peso = valor

    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para Camión ($40.000)."""
        return 40000

    def precio_trabajo(self, horas: int = 1) -> int:
        """
        Calcula el precio de trabajo total para el camión.
        Fórmula: (Tarifa por hora * horas) + (Adicional por peso kg * $2/kg)
        """
        if not isinstance(horas, int) or horas <= 0:
            raise ValueError("Las horas de trabajo deben ser un entero positivo.")
        adicional_peso = self.peso * 2
        return (self.tarifa_hora() * horas) + adicional_peso
