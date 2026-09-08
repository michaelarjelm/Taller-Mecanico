from camion import Camion

class CamionMineria(Camion):
    """
    Representa un camión de minería (maquinaria pesada de alta extracción).
    Hereda de Camion y aplica validaciones estrictas de alto tonelaje y tarifas mineras.
    """
    def __init__(self, patente: str, anio: int, capacidad_carga: int, peso: int, tonelaje_maximo: int):
        # Inicializa patente, año, capacidad de carga y peso en la clase Camion
        super().__init__(patente, anio, capacidad_carga, peso)
        self.tonelaje_maximo = tonelaje_maximo  # Valida mediante setter especializado

    @Camion.peso.setter
    def peso(self, valor: int) -> None:
        """
        Validación especializada para Camión de Minería:
        Exige un peso mínimo de 15.000 kg (15 toneladas) para ser considerado maquinaria pesada.
        """
        if not isinstance(valor, int):
            raise TypeError("El peso debe ser un número entero.")
        if valor < 15000:
            raise ValueError(f"Un Camión de Minería debe tener un peso bruto de al menos 15.000 kg. Valor ingresado: {valor} kg.")
        self._peso = valor

    @property
    def tonelaje_maximo(self) -> int:
        """Getter para el tonelaje máximo de extracción en toneladas."""
        return self._tonelaje_maximo

    @tonelaje_maximo.setter
    def tonelaje_maximo(self, valor: int) -> None:
        """
        Validación especializada para Camión de Minería:
        Exige un tonelaje máximo de al menos 30 toneladas de extracción.
        """
        if not isinstance(valor, int):
            raise TypeError("El tonelaje máximo debe ser un número entero.")
        if valor < 30:
            raise ValueError(f"El tonelaje máximo para minería debe ser de al menos 30 toneladas. Valor ingresado: {valor}t.")
        self._tonelaje_maximo = valor

    def tarifa_hora(self) -> int:
        """Retorna la tarifa por hora para un Camión de Minería ($100.000)."""
        return 100000

    def precio_trabajo(self, horas: int = 1) -> int:
        """
        Calcula el precio de trabajo para un Camión de Minería.
        Incluye tarifa horaria minera, recargo por tonelaje de extracción y cargo fijo operacional de minería ($150.000).
        """
        if not isinstance(horas, int) or horas <= 0:
            raise ValueError("Las horas de trabajo deben ser un entero positivo.")
        cargo_fijo_operacion = 150000
        recargo_tonelaje = self.tonelaje_maximo * 1000
        return (self.tarifa_hora() * horas) + recargo_tonelaje + cargo_fijo_operacion
