from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion
from camionmineria import CamionMineria

def probar_taller():
    print("=== 1. PRUEBA DE CREACION DE AUTO CON TRY/EXCEPT Y PROPIEDADES VALIDABLES ===")
    
    # Intento 1: Creación de un Auto con datos inválidos usando try/except
    print("\n--- Probando creacion de un Auto con datos invalidos (capacidad de maletero negativa: -50) ---")
    try:
        # Intenta instanciar un Auto cuya propiedad 'capacidad_maletero' dispara la validación del setter
        auto_fallido = Auto("AB1234", 2020, -50)
    except (ValueError, TypeError) as e:
        # Captura la excepción y muestra un mensaje entendible sin detener la ejecución
        print(f"[ERROR CAPTURADO] No se pudo crear el vehiculo: {e}")
        print("[CONTROLADO] La excepcion fue capturada de forma segura. El programa NO exploto y continua su ejecucion normal.\n")

    # Intento 2: Creación del Auto con datos válidos tras haber capturado la falla
    print("--- Creando el objeto Auto con datos validos ---")
    auto = Auto("AB1234", 2018, 200)
    print(f"[EXITO] Objeto Auto creado correctamente: {auto}")

    print("\n=== 2. OTROS VEHICULOS DEL TALLER ===")
    moto = Moto("CD5678", 2020)
    camion = Camion("EF9012", 2023, 5000)
    camion_minero = CamionMineria("MN3344", 2024, 30000, 100)

    print(f"Objeto Moto: {moto}")
    print(f"Objeto Camion: {camion}")
    print(f"Objeto Camion Mineria: {camion_minero}")

    print("\n=== 3. PRUEBAS DE CONTROL DE ERRORES ADICIONALES (SETTERS Y PROPIEDADES) ===")

    # Prueba de Patente Inválida capturada en try/except
    try:
        auto_patente_corta = Auto("XYZ", 2021, 150)
    except ValueError as e:
        print(f"[ERROR EN PATENTE] {e}")

    # Prueba de Año Fuera de Rango capturada en try/except
    try:
        moto_ano_invalido = Moto("AA1122", 2099)
    except ValueError as e:
        print(f"[ERROR EN AÑO] {e}")

    print("\n=== 4. PRUEBA DE INGRESO Y SALIDA DEL TALLER ===")
    print(auto.ingresar())
    print(auto.ingresar())  # Intento duplicado
    print(auto.entregar())

    print("\n=== 5. CONFIRMACION DE EJECUCION CONTINUA Y TARIFAS (METODO ABSTRACTO) ===")
    print(f"Tarifa por hora Auto:           ${auto.tarifa_hora():,}")
    print(f"Tarifa por hora Moto:           ${moto.tarifa_hora():,}")
    print(f"Tarifa por hora Camion:         ${camion.tarifa_hora():,}")
    print(f"Tarifa por hora Camion Mineria: ${camion_minero.tarifa_hora():,}")
    
    print("\n[PROCESO FINALIZADO] ¡El programa continuo y finalizo con exito! Todas las pruebas se ejecutaron sin interrupcion.")

if __name__ == "__main__":
    probar_taller()
