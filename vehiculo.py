class Vehiculo: # Define la clase Vehiculo
    def __init__(self, patente: str, anio: int): # Constructor que recibe patente y año al crear el objeto
        self.patente: str = patente # Asigna mediante la property para ejecutar la validación del setter
        self.__anio: int = anio # Asigna el año recibido a un atributo privado
        self.__en_taller: bool = False # Inicializa el estado en False (no está en el taller por defecto) como privado

    @property
    def patente(self) -> str: # Getter de la propiedad patente
        return self.__patente # Retorna el valor del atributo privado __patente

    @patente.setter
    def patente(self, nueva_patente: str): # Setter de la propiedad patente con validaciones
        if not isinstance(nueva_patente, str) or len(nueva_patente) < 6 or " " in nueva_patente: # Valida longitud mínima de 6 y sin espacios
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.") # Lanza excepción si no cumple
        self.__patente = nueva_patente # Asigna la patente válida al atributo privado

    @property
    def en_taller(self) -> bool: # Getter de solo lectura de la propiedad en_taller
        return self.__en_taller # Retorna el valor del atributo privado __en_taller

    def ingresar(self) -> str: # Método para registrar el ingreso del vehículo al taller
        if self.__en_taller: # Verifica si el vehículo ya está marcado como dentro del taller
            return "El vehículo ya se encuentra en el taller." # Devuelve mensaje si ya estaba ingresado
        self.__en_taller = True # Cambia el estado a True (ingresado)
        return "El vehículo ha ingresado al taller." # Devuelve mensaje de éxito

    def entregar(self) -> str: # Método para registrar la salida o entrega del vehículo
        if not self.__en_taller: # Verifica si el vehículo no está en el taller
            return "El vehículo no se encuentra en el taller." # Devuelve mensaje indicando que no se puede entregar
        self.__en_taller = False # Cambia el estado a False (fuera del taller)
        return "El vehículo ha sido entregado." # Devuelve mensaje de éxito

    def tarifa_hora(self) -> int: # Método que retorna el costo de la tarifa por hora
        return 5000 # Retorna un valor fijo de 5000
