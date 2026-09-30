class Repuesto:
    def __init__(self, codigo: str, nombre: str, stock: int, es_importado: bool, precio: float):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__stock = stock
        self.__es_importado = es_importado
        self.__precio = precio

    @property
    def nombre(self) -> str:
        return self.__nombre

    def precio_en_pesos(self, dolar: float) -> int:
        if self.__es_importado:
            return round(self.__precio * dolar)
        return round(self.__precio)

    def hay_stock(self) -> bool:
        return self.__stock > 0

    def disminuir_stock(self, cantidad: int):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
