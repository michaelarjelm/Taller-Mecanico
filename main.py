from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion
from camionmineria import CamionMineria

def probar_taller():
    print("=== 1. PRUEBA DE INSTANCIACIÓN Y VALIDACIÓN ===")
    
    # Instanciaciones válidas
    auto = Auto("ab1234", 2018, 200)               # Auto limpio
    moto = Moto("CD5678", 2020)                   # Moto válida
    camion = Camion("EF9012", 2023, 5000)          # Camión válido
    camion_minero = CamionMineria("MN3344", 2024, 30000, 100) # Camión de Minería (30t carga, 100t max)

    print(f"Objeto Auto: {auto}")
    print(f"Objeto Moto: {moto}")
    print(f"Objeto Camión: {camion}")
    print(f"Objeto Camión Minería: {camion_minero}")

    print("\n=== 2. PRUEBA DE CONTROL DE ERRORES Y VALIDACIONES DE SEGURIDAD ===")

    # Prueba 1: Intento de instanciar la clase abstracta
    try:
        v_base = Vehiculo("BASE01", 2015)
    except TypeError as e:
        print(f"[OK - Error Capturado] No se puede instanciar la clase abstracta Vehiculo: {e}")

    # Prueba 2: Patente inválida
    try:
        auto_invalido = Auto("AB12", 2020, 100)
    except ValueError as e:
        print(f"[OK - Error Capturado] Patente inválida: {e}")

    # Prueba 3: Año futuro no permitido
    try:
        moto_invalida = Moto("AA1122", 2099)
    except ValueError as e:
        print(f"[OK - Error Capturado] Año fuera de rango: {e}")

    # Prueba 4: Capacidad de carga negativa en Camión
    try:
        camion_invalido = Camion("CC3344", 2021, -500)
    except ValueError as e:
        print(f"[OK - Error Capturado] Capacidad negativa: {e}")

    # Prueba 5: Tonelaje máximo inválido en Camión de Minería
    try:
        minero_invalido = CamionMineria("MIN001", 2022, 10000, -10)
    except ValueError as e:
        print(f"[OK - Error Capturado] Tonelaje minero inválido: {e}")

    print("\n=== 3. PRUEBA DE INGRESO Y SALIDA DEL TALLER ===")
    print(camion_minero.ingresar())
    print(camion_minero.ingresar())  # Intento duplicado
    print(camion_minero.entregar())

    print("\n=== 4. PRUEBA DE TARIFAS POR HORA (MÉTODO ABSTRACTO) ===")
    print(f"Tarifa por hora Auto:           ${auto.tarifa_hora():,}")
    print(f"Tarifa por hora Moto:           ${moto.tarifa_hora():,}")
    print(f"Tarifa por hora Camión:         ${camion.tarifa_hora():,}")
    print(f"Tarifa por hora Camión Minería: ${camion_minero.tarifa_hora():,}")

if __name__ == "__main__":
    probar_taller()

