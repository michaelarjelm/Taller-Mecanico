from auto import Auto # Importa la clase Auto desde auto.py
from moto import Moto # Importa la clase Moto desde moto.py
from camion import Camion # Importa la clase Camion desde camion.py

camion1 = Camion("AA111AA", 2021, 8000) # Instancia el primer camión con 8000 kg de capacidad
camion2 = Camion("BB222BB", 2023, 12000) # Instancia el segundo camión con 12000 kg de capacidad

print(camion1.ingresar()) # Registra el ingreso del primer camión
print(camion2.ingresar()) # Registra el ingreso del segundo camión

if camion1.get_capacidad_carga() > camion2.get_capacidad_carga(): # Compara cuál de los dos camiones tiene mayor capacidad de carga
    print(f"El camión 1 tiene mayor capacidad de carga ({camion1.get_capacidad_carga()} kg).") # Imprime si el primer camión carga más
elif camion2.get_capacidad_carga() > camion1.get_capacidad_carga(): # Evalúa si el segundo camión tiene mayor capacidad
    print(f"El camión 2 tiene mayor capacidad de carga ({camion2.get_capacidad_carga()} kg).") # Imprime si el segundo camión carga más
else: # En caso de que ambos tengan la misma capacidad
    print("Ambos camiones tienen la misma capacidad de carga.") # Imprime que las capacidades son iguales
