from camion import Camion

class CamionMineria(Camion):
    """
    Representa un camión de minería (maquinaria pesada) en el taller mecánico.
    Hereda de la clase Camion y añade especificaciones para trabajo minero.
    """
    def __init__(self, patente: str, anio: int, capacidad_carga: int, tonelaje_maximo: int):
        super().__init__(patente, anio, capacidad_carga)
        self.tonelaje_maximo = tonelaje_maximo  # Valida mediante setter

    @property
    def tonelaje_maximo(self) -> int:
        """Getter para el tonelaje máximo de extracción en toneladas."""
        return self._tonelaje_maximo

    @tonelaje_maximo.setter
    def tonelaje_maximo(self, valor: int) -> None:
        """Setter con validación de tipo y rango positivo."""
        if not isinstance(valor, int):
            raise TypeError("El tonelaje máximo debe ser un entero.")
        if valor <= 0:
            raise ValueError("El tonelaje máximo debe ser un valor positivo mayor a 0.")
        self._tonelaje_maximo = valor

    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para un Camión de Minería ($100.000)."""
        return 100000
