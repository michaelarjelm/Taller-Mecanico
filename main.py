from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion

def probar_taller():
    print("=== 1. PRUEBA DE INSTANCIACIÓN Y VALIDACIÓN ===")
    
    # Instanciaciones válidas
    auto = Auto("ab1234", 2018, 200)       # Auto limpio (patente se pasa a mayúsculas 'AB1234')
    moto = Moto("CD5678", 2020)           # Moto válida
    camion = Camion("EF9012", 2023, 5000)  # Camión válido

    print(f"Objeto Auto: {auto}")
    print(f"Objeto Moto: {moto}")
    print(f"Objeto Camión: {camion}")

    print("\n=== 2. PRUEBA DE CONTROL DE ERRORES Y VALIDACIONES DE SEGURIDAD ===")

    # Prueba 1: Intento de instanciar la clase abstracta
    try:
        v_base = Vehiculo("BASE01", 2015)
    except TypeError as e:
        print(f"[OK - Error Capturado] No se puede instanciar la clase abstracta Vehiculo: {e}")

    # Prueba 2: Patente inválida (menos de 6 caracteres o vacía)
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

    print("\n=== 3. PRUEBA DE INGRESO Y SALIDA DEL TALLER ===")
    print(auto.ingresar())
    print(auto.ingresar())  # Intento duplicado de ingreso
    print(auto.entregar())
    print(auto.entregar())  # Intento duplicado de entrega

    print("\n=== 4. PRUEBA DE TARIFAS POR HORA (MÉTODO ABSTRACTO) ===")
    print(f"Tarifa por hora Auto:   ${auto.tarifa_hora():,}")
    print(f"Tarifa por hora Moto:   ${moto.tarifa_hora():,}")
    print(f"Tarifa por hora Camión: ${camion.tarifa_hora():,}")

if __name__ == "__main__":
    probar_taller()
