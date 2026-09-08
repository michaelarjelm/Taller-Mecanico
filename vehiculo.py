import datetime
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase abstracta base para representar un vehículo en el taller mecánico.
    Incluye encapsulamiento robusto, validación de datos y control de estado.
    """
    def __init__(self, patente: str, anio: int):
        self.patente = patente  # Asigna usando el setter para ejecutar la validación
        self.anio = anio        # Asigna usando el setter para ejecutar la validación
        self._en_taller: bool = False  # Estado privado del vehículo

    @property
    def patente(self) -> str:
        """Getter para la patente del vehículo."""
        return self._patente

    @patente.setter
    def patente(self, valor: str) -> None:
        """Setter con validación de tipo, formato y seguridad para la patente."""
        if not isinstance(valor, str):
            raise TypeError("La patente debe ser una cadena de texto (str).")
        valor_limpio = valor.strip().upper()
        if len(valor_limpio) < 6 or " " in valor_limpio:
            raise ValueError("La patente debe tener al menos 6 caracteres y no debe contener espacios.")
        self._patente = valor_limpio

    @property
    def anio(self) -> int:
        """Getter para el año del vehículo."""
        return self._anio

    @anio.setter
    def anio(self, valor: int) -> None:
        """Setter con validación de rango y tipo para el año del vehículo."""
        if not isinstance(valor, int):
            raise TypeError("El año debe ser un número entero (int).")
        anio_actual = datetime.datetime.now().year
        if valor < 1900 or valor > anio_actual + 1:
            raise ValueError(f"El año debe estar en un rango válido (entre 1900 y {anio_actual + 1}).")
        self._anio = valor

    @property
    def en_taller(self) -> bool:
        """Getter para consultar si el vehículo está en el taller."""
        return self._en_taller

    def get_patente(self) -> str:
        """Método getter tradicional para compatibilidad."""
        return self.patente

    def set_patente(self, valor: str) -> None:
        """Método setter tradicional para compatibilidad."""
        self.patente = valor

    def ingresar(self) -> str:
        """Registra el ingreso del vehículo al taller."""
        if self._en_taller:
            return "El vehículo ya se encuentra en el taller."
        self._en_taller = True
        return "El vehículo ha ingresado al taller."

    def entregar(self) -> str:
        """Registra la salida/entrega del vehículo del taller."""
        if not self._en_taller:
            return "El vehículo no se encuentra en el taller."
        self._en_taller = False
        return "El vehículo ha sido entregado."

    @abstractmethod
    def tarifa_hora(self) -> int:
        """Método abstracto que retorna el costo de la tarifa por hora."""
        pass

    def __repr__(self) -> str:
        estado = "En Taller" if self._en_taller else "Fuera del Taller"
        return f"<{self.__class__.__name__} Patente={self.patente}, Año={self.anio}, Estado={estado}>"
