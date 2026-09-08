# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel  
**Institución:** Inacap  
**Alumno:** Marcos Montenegro  
**Rama Activa de Desarrollo:** `feature/desarrollo`

---

## 📋 Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

---

### 31 de Agosto de 2026
- **Creación de Rama de Trabajo:** Creación y publicación de la rama `feature/desarrollo`.
- **Implementación de Herencia (Subclases):**
  - **Clase Auto (`auto.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_maletero` (en litros).
  - **Clase Moto (`moto.py`):** Hereda de `Vehiculo` (estructura base).
  - **Clase Camion (`camion.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_carga` (en kilos).
- **Actualización de Script Principal (`main.py`):**
  - Se importaron las subclases `Auto`, `Moto` y `Camion`.
  - Se instanciaron objetos de cada una de las clases hijas y se verificó la invocación de métodos heredados (`ingresar()` y `tarifa_hora()`).
- **Documentación:** Código comentado línea por línea con fines pedagógicos.

---

### 8 de Septiembre de 2026

#### 1. ⚙️ Reconfiguración de Entorno Git y Remotos
- **Separación de Remotos:** Configuración del repositorio remoto del profesor (`michaelarjelm`) como `upstream` y el repositorio del alumno (`Marcos-Montenegro2026`) como `origin`.
- **Publicación en Rama de Desarrollo:** Publicación y vinculación directa de la rama `feature/desarrollo` en GitHub.

#### 2. 🏛️ Implementación de Clase y Métodos Abstractos (`vehiculo.py`)
- **Herencia de `ABC`:** La clase `Vehiculo` pasa a ser abstracta mediante la librería estándar `abc`.
- **Método Abstracto `@abstractmethod`:** Se declaró `tarifa_hora(self) -> int` como método abstracto, impidiendo la instanciación directa de la clase base y obligando a cada subclase a implementar su propia lógica tarifaria.

#### 3. 🛡️ Seguridad, Encapsulamiento y Validaciones Robustas
- **Saneamiento de Patentes:** Implementación de `@property` y `@patente.setter` para verificar tipo de dato (`str`), eliminación de espacios y formateo a mayúsculas automático con longitud mínima de 6 caracteres.
- **Rango de Año Seguro:** Validación del atributo `anio` garantizando valores numéricos dentro de un rango realista (1900 a año actual + 1).
- **Control de Capacidades:** Validaciones en los setters de `capacidad_maletero` y `capacidad_carga` para evitar capacidades negativas.
- **Control de Estado de Taller:** Creación del getter `en_taller` para consultar el estado del vehículo de forma segura.

#### 4. 🚛 Nueva Subclase `CamionMineria` (`camionmineria.py`)
- **Herencia Avanzada:** Creación de la subclase `CamionMineria` que hereda de `Camion`.
- **Atributo Especializado:** Incorporación del atributo `tonelaje_maximo` con validación de valores estrictamente positivos mayores a 0.
- **Tarifa Especializada:** Implementación del método abstracto `tarifa_hora()` retornando $100.000/hr.

#### 5. 🧪 Suite de Pruebas Integradas (`main.py`)
- **Demostración de Polimorfismo:** Ejecución de `tarifa_hora()` para todas las categorías (`Auto`: $25.000, `Moto`: $15.000, `Camion`: $40.000, `CamionMineria`: $100.000).
- **Pruebas de Captura de Excepciones:** Verificación en bloque `try-except` para control de errores de instanciación abstracta, patentes inválidas, años fuera de rango y tonelajes negativos.
