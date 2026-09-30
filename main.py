import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
from model.marca import Marca  # Importa el modelo Marca para instanciar objetos
import sys
from servicios.miindicador import MiIndicador
from model.repuesto import Repuesto

def mostrar_menu():
    print("\n" + "="*30)
    print("      MANTENEDOR DE MARCAS")
    print("="*30)
    print("1. Listar todas las marcas")
    print("2. Buscar marca por ID")
    print("3. Insertar nueva marca")
    print("4. Actualizar marca existente")
    print("5. Eliminar marca")
    print("6. Obtener valores económicos")
    print("7. Cotizar repuesto")
    print("8. Salir")
    print("="*30)

def main():
    print("--- Inicializando Sistema ---")
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()
    
    # 2. Instanciar el DAO
    marca_dao = MarcaDao(conn)
    
    # 3. Asegurar que la tabla exista
    marca_dao.crear_tabla()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == '1':
            print("\n--- Listado de Marcas ---")
            marcas = marca_dao.listar()
            if not marcas:
                print("No hay marcas registradas en la base de datos.")
            else:
                for m in marcas:
                    print(f"ID: {m.id} | Nombre: {m.nombre}")
                    
        elif opcion == '2':
            print("\n--- Buscar Marca ---")
            try:
                id_buscar = int(input("Ingrese el ID de la marca a buscar: "))
                marca = marca_dao.buscar(id_buscar)
                if marca:
                    print(f"Marca encontrada -> ID: {marca.id} | Nombre: {marca.nombre}")
                else:
                    print(f"No se encontró ninguna marca con el ID {id_buscar}.")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
                
        elif opcion == '3':
            print("\n--- Insertar Nueva Marca ---")
            nombre = input("Ingrese el nombre de la nueva marca: ")
            if nombre.strip():
                nueva_marca = Marca(nombre)
                marca_dao.insertar(nueva_marca)
                conn.commit() # Importante confirmar los cambios
                print(f"Marca '{nueva_marca.nombre}' insertada exitosamente con el ID: {nueva_marca.id}")
            else:
                print("Error: El nombre de la marca no puede estar vacío.")
                
        elif opcion == '4':
            print("\n--- Actualizar Marca ---")
            try:
                id_actualizar = int(input("Ingrese el ID de la marca a actualizar: "))
                marca_existente = marca_dao.buscar(id_actualizar)
                
                if marca_existente:
                    print(f"Marca actual: {marca_existente.nombre}")
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    
                    if nuevo_nombre.strip():
                        marca_existente.nombre = nuevo_nombre # Necesitamos asegurarnos que el modelo tenga un setter para nombre, o modificarlo directamente si no es privado, o recrear la instancia.
                        # Dado que el nombre es __nombre y solo tiene un getter en el modelo actual, instanciamos una nueva
                        marca_modificada = Marca(nuevo_nombre)
                        marca_modificada.id = id_actualizar
                        
                        resultado = marca_dao.actualizar(marca_modificada)
                        if resultado:
                            print(f"Marca actualizada con éxito. Nuevo nombre: {resultado.nombre}")
                        else:
                            print("No se pudo actualizar la marca.")
                    else:
                        print("Error: El nombre no puede estar vacío.")
                else:
                    print(f"No se encontró ninguna marca con el ID {id_actualizar}.")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
                
        elif opcion == '5':
            print("\n--- Eliminar Marca ---")
            try:
                id_eliminar = int(input("Ingrese el ID de la marca a eliminar: "))
                # Opcional: mostrar la marca antes de eliminarla para confirmar
                marca = marca_dao.buscar(id_eliminar)
                if marca:
                    confirmacion = input(f"¿Está seguro que desea eliminar la marca '{marca.nombre}'? (s/n): ")
                    if confirmacion.lower() == 's':
                        if marca_dao.eliminar(id_eliminar):
                            print("Marca eliminada exitosamente.")
                        else:
                            print("Ocurrió un error al intentar eliminar la marca.")
                    else:
                        print("Operación cancelada.")
                else:
                    print(f"No se encontró ninguna marca con el ID {id_eliminar}.")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
                
        elif opcion == '6':
            print("\n--- Valores Económicos ---")
            indicador = MiIndicador()
            print("Indicadores disponibles comunes: uf, dolar, euro, utm, ipc")
            codigo = input("Ingrese el código del indicador que desea consultar: ").strip().lower()
            
            if codigo:
                try:
                    valor = indicador.valor(codigo)
                    print(f"\nEl valor actual de '{codigo.upper()}' es: ${valor}")
                except KeyError:
                    print(f"\nError: No se encontró el indicador '{codigo}'.")
                except Exception as e:
                    print(f"\nError al consultar la API: {e}")
            else:
                print("Error: El código no puede estar vacío.")

        elif opcion == '7':
            print("\n--- Cotizar Repuesto ---")
            try:
                codigo_rep = input("Ingrese el código del repuesto: ")
                nombre_rep = input("Ingrese el nombre del repuesto: ")
                stock_rep = int(input("Ingrese el stock disponible: "))
                importado_input = input("¿El repuesto es importado? (s/n): ").strip().lower()
                es_importado = True if importado_input == 's' else False
                precio_rep = float(input(f"Ingrese el precio en {'dólares' if es_importado else 'pesos'}: "))

                repuesto = Repuesto(codigo_rep, nombre_rep, stock_rep, es_importado, precio_rep)

                # Si es importado, consultar el valor del dólar
                valor_dolar = 1
                if es_importado:
                    print("Consultando el valor actual del dólar...")
                    indicador = MiIndicador()
                    valor_dolar = indicador.valor('dolar')
                
                precio_final = repuesto.precio_en_pesos(valor_dolar)
                print(f"\n> El precio final de '{repuesto.nombre}' es: ${precio_final} CLP")

            except ValueError:
                print("Error: Ingrese valores numéricos válidos para stock y precio.")
            except Exception as e:
                print(f"Error al cotizar el repuesto: {e}")

        elif opcion == '8':
            print("\nCerrando el sistema. ¡Hasta luego!")
            conn.close()
            sys.exit(0)
            
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
