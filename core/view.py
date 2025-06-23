from datetime import date
from core.controllers import *

def mostrar_menu_principal():
    """
    Muestra el menú principal de la aplicación
    """
    print("\n" + "="*50)
    print("🎮 SISTEMA DE GESTIÓN DE VIDEOJUEGOS")
    print("="*50)
    print("1. Gestionar Empresas")
    print("2. Gestionar Consolas")
    print("3. Gestionar Juegos")
    print("4. Gestionar Relaciones Juego-Consola")
    print("0. Salir")
    print("="*50)

def mostrar_menu_empresas():
    """
    Menú para gestionar empresas
    """
    print("\n📢 GESTIÓN DE EMPRESAS")
    print("-" * 30)
    print("1. Crear empresa")
    print("2. Ver todas las empresas")
    print("3. Buscar empresa por ID")
    print("4. Actualizar empresa")
    print("5. Eliminar empresa")
    print("0. Volver al menú principal")

def mostrar_menu_consolas():
    """
    Menú para gestionar consolas
    """
    print("\n🎮 GESTIÓN DE CONSOLAS")
    print("-" * 30)
    print("1. Crear consola")
    print("2. Ver todas las consolas")
    print("3. Buscar consola por ID")
    print("4. Actualizar consola")
    print("5. Eliminar consola")
    print("0. Volver al menú principal")

def mostrar_menu_juegos():
    """
    Menú para gestionar juegos
    """
    print("\n🕹️ GESTIÓN DE JUEGOS")
    print("-" * 30)
    print("1. Crear juego")
    print("2. Ver todos los juegos")
    print("3. Buscar juego por ID")
    print("4. Actualizar juego")
    print("5. Eliminar juego")
    print("0. Volver al menú principal")

def mostrar_menu_relaciones():
    """
    Menú para gestionar relaciones juego-consola
    """
    print("\n🔗 GESTIÓN DE RELACIONES JUEGO-CONSOLA")
    print("-" * 40)
    print("1. Agregar juego a consola")
    print("2. Quitar juego de consola")
    print("3. Ver juegos de una consola")
    print("0. Volver al menú principal")



# Interfaz para el manejo de la BD en la tabla empresas
def gestionar_empresas():

    while True:
        mostrar_menu_empresas()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la empresa: ")
            sede = input("Sede central (opcional): ")
            sede = sede if sede.strip() else None
            crear_empresa(nombre, sede)
            
        elif opcion == "2":
            leer_todas_empresas()
            
        elif opcion == "3":
            try:
                empresa_id = int(input("ID de la empresa: "))
                leer_empresa_por_id(empresa_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "4":
            try:
                empresa_id = int(input("ID de la empresa a actualizar: "))
                nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
                nueva_sede = input("Nueva sede (deja vacío para no cambiar): ")
                
                nuevo_nombre = nuevo_nombre if nuevo_nombre.strip() else None
                nueva_sede = nueva_sede if nueva_sede.strip() else None
                
                actualizar_empresa(empresa_id, nuevo_nombre, nueva_sede)
            except ValueError:
                print("❌ Por favor ingresa un número válido para el ID")
                
        elif opcion == "5":
            try:
                empresa_id = int(input("ID de la empresa a eliminar: "))
                confirmar = input("¿Estás seguro? (s/n): ")
                if confirmar.lower() == 's':
                    eliminar_empresa(empresa_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "0":
            break
        else:
            print("❌ Opción no válida")


# Interfaz para el manejo de la BD en la tabla consolas

def gestionar_consolas():
    """
    Maneja todas las operaciones relacionadas con consolas
    """
    while True:
        mostrar_menu_consolas()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la consola: ")
            try:
                precio = float(input("Precio: $"))
                print("Fecha de lanzamiento:")
                año = int(input("Año: "))
                mes = int(input("Mes: "))
                dia = int(input("Día: "))
                fecha = date(año, mes, dia)
                
                print("\nEmpresas disponibles:")
                leer_todas_empresas()
                empresa_id = int(input("ID de la empresa: "))
                
                crear_consola(nombre, precio, fecha, empresa_id)
            except ValueError:
                print("❌ Por favor ingresa valores válidos")
                
        elif opcion == "2":
            leer_todas_consolas()
            
        elif opcion == "3":
            try:
                consola_id = int(input("ID de la consola: "))
                leer_consola_por_id(consola_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "4":
            try:
                consola_id = int(input("ID de la consola a actualizar: "))
                nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
                
                precio_str = input("Nuevo precio (deja vacío para no cambiar): ")
                nuevo_precio = float(precio_str) if precio_str.strip() else None
                
                actualizar_consola(consola_id, 
                                 nuevo_nombre if nuevo_nombre.strip() else None,
                                 nuevo_precio)
            except ValueError:
                print("❌ Por favor ingresa valores válidos")
                
        elif opcion == "5":
            try:
                consola_id = int(input("ID de la consola a eliminar: "))
                confirmar = input("¿Estás seguro? (s/n): ")
                if confirmar.lower() == 's':
                    eliminar_consola(consola_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "0":
            break
        else:
            print("❌ Opción no válida")


# Interfaz para el manejo de la BD en la tabla juegos

def gestionar_juegos():
    while True:
        mostrar_menu_juegos()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del juego: ")
            crear_juego(nombre)
            
        elif opcion == "2":
            leer_todos_juegos()
            
        elif opcion == "3":
            try:
                juego_id = int(input("ID del juego: "))
                leer_juego_por_id(juego_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "4":
            try:
                juego_id = int(input("ID del juego a actualizar: "))
                nuevo_nombre = input("Nuevo nombre: ")
                actualizar_juego(juego_id, nuevo_nombre)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "5":
            try:
                juego_id = int(input("ID del juego a eliminar: "))
                confirmar = input("¿Estás seguro? (s/n): ")
                if confirmar.lower() == 's':
                    eliminar_juego(juego_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "0":
            break
        else:
            print("❌ Opción no válida")

# Interfaz para el manejo de la BD en la relasion entre juego y consolas

def gestionar_relaciones():

    while True:
        mostrar_menu_relaciones()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            try:
                print("\nJuegos disponibles:")
                leer_todos_juegos()
                juego_id = int(input("ID del juego: "))
                
                print("\nConsolas disponibles:")
                leer_todas_consolas()
                consola_id = int(input("ID de la consola: "))
                
                agregar_juego_a_consola(juego_id, consola_id)
            except ValueError:
                print("❌ Por favor ingresa números válidos")
                
        elif opcion == "2":
            try:
                juego_id = int(input("ID del juego: "))
                consola_id = int(input("ID de la consola: "))
                quitar_juego_de_consola(juego_id, consola_id)
            except ValueError:
                print("❌ Por favor ingresa números válidos")
                
        elif opcion == "3":
            try:
                consola_id = int(input("ID de la consola: "))
                listar_juegos_por_consola(consola_id)
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                
        elif opcion == "0":
            break
        else:
            print("❌ Opción no válida")



# Interfaz principal para la gestion de cada bd

def main():

    print("🚀 Iniciando aplicación...")
    
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            gestionar_empresas()
        elif opcion == "2":
            gestionar_consolas()
        elif opcion == "3":
            gestionar_juegos()
        elif opcion == "4":
            gestionar_relaciones()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo")
            

if __name__ == "__main__":
    main()