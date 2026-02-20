# ==========================================
# PROYECTO: SISTEMA DE GESTIÓN ACADÉMICA
# ==========================================

# --- FASE 1: Funciones definidas por el usuario ---

def saludo(nombre):
    """Imprime un mensaje de bienvenida."""
    print(f"\n--- ¡Hola {nombre}, bienvenido al sistema! ---")

def promedio(lista_notas):
    """Recibe una lista de notas y devuelve el promedio (Uso de sum y len)."""
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

def registrar_estudiante(diccionario, nombre, edad, curso):
    """Agrega un estudiante al diccionario (Paso de diccionarios)."""
    # Se comprueba que el diccionario se modifica fuera de la función (por referencia)
    diccionario[nombre] = {
        "edad": edad, 
        "curso": curso, 
        "notas": []
    }

def combinar_listas(*args):
    """Recibe varias listas y las combina usando *args."""
    lista_final = []
    for lista in args:
        lista_final.extend(lista)
    return lista_final

def mostrar_info(**kwargs):
    """Imprime datos pasados como clave-valor usando **kwargs."""
    for clave, valor in kwargs.items():
        print(f"- {clave.replace('_', ' ').capitalize()}: {valor}")

# --- FASE 3: Funciones avanzadas y control de flujo ---

def calcular_note_final(notas, extra=0):
    """Calcula la suma de notas y aplica bonificación opcional."""
    return sum(notas) + extra

def listar_estudiantes(estudiantes):
    """Recorre el diccionario con for y enumerate."""
    print("\nLista de Estudiantes Registrados:")
    for i, (nombre, datos) in enumerate(estudiantes.items(), 1):
        print(f"{i}. {nombre} | Edad: {datos['edad']} | Curso: {datos['curso']}")

def validar_entrada(mensaje):
    """Usa un while hasta recibir un valor no vacío (Validación)."""
    valor = input(mensaje).strip()
    while not valor:
        print("Error: El campo no puede estar vacío.")
        valor = input(mensaje).strip()
    return valor

# --- FASE 4: Proyecto integrador con funciones (Menú) ---

def menu():
    estudiantes_db = {}
    
    # FASE 2: Uso de funciones matemáticas (Ejemplos rápidos requeridos)
    print("Iniciando componentes matemáticos...")
    print(f"Valor absoluto de -15: {abs(-15)}")
    print(f"Redondeo de 3.1416: {round(3.1416, 2)}")
    print(f"Potencia 2^5: {pow(2, 5)}")
    
    saludo("Administrador")

    while True:
        print("\n--- MENÚ DE GESTIÓN ---")
        print("1. Registrar estudiante")
        print("2. Registrar notas")
        print("3. Calcular promedio")
        print("4. Mostrar reporte general")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # Fase 2: Manipulación de cadenas (upper, strip)
            nombre = validar_entrada("Nombre del estudiante: ").strip().upper()
            edad = validar_entrada("Edad: ")
            curso = validar_entrada("Curso: ")
            registrar_estudiante(estudiantes_db, nombre, edad, curso)
            
        elif opcion == "2":
            nombre = input("Nombre del estudiante a calificar: ").upper()
            if nombre in estudiantes_db:
                nota = float(input(f"Ingrese nota para {nombre}: "))
                estudiantes_db[nombre]["notas"].append(nota)
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            nombre = input("Estudiante para promedio: ").upper()
            if nombre in estudiantes_db:
                notas = estudiantes_db[nombre]["notas"]
                p = promedio(notas)
                # Fase 2: Uso de funciones integradas (max, min)
                if notas:
                    print(f"Promedio: {p} | Máxima: {max(notas)} | Mínima: {min(notas)}")
                else:
                    print("No hay notas registradas.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            # Micro-check Fase 3: Ejecutar listar_estudiantes
            listar_estudiantes(estudiantes_db)
            
            # Fase 2: Aplicar sorted a nombres
            nombres_ordenados = sorted(estudiantes_db.keys())
            print(f"Orden alfabético: {nombres_ordenados}")
            
            # Fase 2: Validaciones con isinstance
            print(f"¿La base de datos es un diccionario? {isinstance(estudiantes_db, dict)}")

        elif opcion == "5" or opcion.lower() == "salir":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecución del programa
if __name__ == "__main__":
    menu()