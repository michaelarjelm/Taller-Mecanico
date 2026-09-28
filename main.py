import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
from model.marca import Marca  # Importa el modelo Marca para instanciar objetos
import sys

def mostrar_menu():
    print("\n" + "="*30)
    print("      MANTENEDOR DE MARCAS")
    print("="*30)
    print("1. Listar todas las marcas")
    print("2. Buscar marca por ID")
    print("3. Insertar nueva marca")
    print("4. Actualizar marca existente")
    print("5. Eliminar marca")
    print("6. Salir")
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
        opcion = input("Seleccione una opción (1-6): ")
        
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
            print("\nCerrando el sistema. ¡Hasta luego!")
            conn.close()
            sys.exit(0)
            
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
