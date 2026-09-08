from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion
from camionmineria import CamionMineria

def probar_taller():
    print("=== 1. PRUEBA DE INSTANCIACION Y CONFIGURACION DE PESOS Y VALORES ===")
    
    # Instanciaciones válidas
    auto = Auto("AB1234", 2018, 200)
    moto = Moto("CD5678", 2020)
    camion = Camion("EF9012", 2023, 8000, 10000)                # Camión convencional (8t carga, 10.000 kg peso)
    camion_minero = CamionMineria("MN3344", 2024, 40000, 25000, 150) # Camión minería (40t carga, 25.000 kg peso, 150t max)

    print(f"Objeto Auto:           {auto}")
    print(f"Objeto Moto:           {moto}")
    print(f"Objeto Camion:         {camion} | Peso: {camion.peso:,} kg")
    print(f"Objeto Camion Mineria: {camion_minero} | Peso: {camion_minero.peso:,} kg | Tonelaje Max: {camion_minero.tonelaje_maximo}t")

    print("\n=== 2. PRUEBA DE VALIDACIONES ESPECIFICAS PARA CAMION Y MINERIA (TRY/EXCEPT) ===")

    # Prueba 1: Peso inválido en Camión Convencional (<= 0)
    try:
        camion_peso_invalido = Camion("CC1122", 2021, 5000, 0)
    except (ValueError, TypeError) as e:
        print(f"[ERROR CAPTURADO] Peso Camion invalido: {e}")

    # Prueba 2: Peso insuficiente en Camión de Minería (< 15.000 kg)
    try:
        minero_peso_liviano = CamionMineria("MIN001", 2022, 10000, 8000, 50)
    except ValueError as e:
        print(f"[ERROR CAPTURADO] Validacion Mineria (Peso insuficiente): {e}")

    # Prueba 3: Tonelaje máximo insuficiente en Camión de Minería (< 30 toneladas)
    try:
        minero_tonelaje_bajo = CamionMineria("MIN002", 2023, 15000, 20000, 15)
    except ValueError as e:
        print(f"[ERROR CAPTURADO] Validacion Mineria (Tonelaje insuficiente): {e}")

    print("\n=== 3. PRUEBA DE TARIFAS POR HORA Y PRECIO DE TRABAJO (2 HORAS) ===")
    horas_trabajo = 2
    print(f"Tarifa por Hora Camion Convencional: ${camion.tarifa_hora():,}")
    print(f"PRECIO DE TRABAJO TOTAL Camion ({horas_trabajo} hrs): ${camion.precio_trabajo(horas_trabajo):,}")
    
    print(f"\nTarifa por Hora Camion Mineria:      ${camion_minero.tarifa_hora():,}")
    print(f"PRECIO DE TRABAJO TOTAL Minero ({horas_trabajo} hrs): ${camion_minero.precio_trabajo(horas_trabajo):,}")

    print("\n[PROCESO FINALIZADO] ¡Se validaron los pesos y precios de trabajo correctamente sin interrumpir el programa!")

if __name__ == "__main__":
    probar_taller()
