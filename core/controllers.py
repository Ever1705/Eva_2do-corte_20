from sqlalchemy.orm import Session
from core.models import Empresa, Consola, Juego
from db.conecction import db_session
from datetime import date

# ==================== CRUD PARA EMPRESAS ====================

def crear_empresa(nombre: str, sede_central: str = None):
    """
    Crear una nueva empresa en la base de datos
    """
    with db_session() as db:
        nueva_empresa = Empresa(
            nombre=nombre,
            sede_central=sede_central
        )
        db.add(nueva_empresa)
        db.flush()  # Para obtener el ID antes del commit
        print(f"✅ Empresa '{nombre}' creada con ID: {nueva_empresa.id}")
        return nueva_empresa.id

def leer_todas_empresas():
    """
    Obtener todas las empresas de la base de datos
    """
    with db_session() as db:
        empresas = db.query(Empresa).all()
        print(f"📋 Se encontraron {len(empresas)} empresas:")
        for empresa in empresas:
            print(f"  - ID: {empresa.id}, Nombre: {empresa.nombre}, Sede: {empresa.sede_central}")
        return empresas

def leer_empresa_por_id(empresa_id: int):
    """
    Obtener una empresa específica por su ID
    """
    with db_session() as db:
        empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
        if empresa:
            print(f"🔍 Empresa encontrada: {empresa.nombre} (Sede: {empresa.sede_central})")
            return empresa
        else:
            print(f"❌ No se encontró empresa con ID: {empresa_id}")
            return None

def actualizar_empresa(empresa_id: int, nuevo_nombre: str = None, nueva_sede: str = None):
    """
    Actualizar los datos de una empresa existente
    """
    with db_session() as db:
        empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
        if empresa:
            if nuevo_nombre:
                empresa.nombre = nuevo_nombre
            if nueva_sede:
                empresa.sede_central = nueva_sede
            print(f"✏️ Empresa ID {empresa_id} actualizada correctamente")
            return True
        else:
            print(f"❌ No se encontró empresa con ID: {empresa_id}")
            return False

def eliminar_empresa(empresa_id: int):
    """
    Eliminar una empresa de la base de datos
    """
    with db_session() as db:
        empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
        if empresa:
            nombre_empresa = empresa.nombre
            db.delete(empresa)
            print(f"🗑️ Empresa '{nombre_empresa}' eliminada correctamente")
            return True
        else:
            print(f"❌ No se encontró empresa con ID: {empresa_id}")
            return False

# ==================== CRUD PARA CONSOLAS ====================

def crear_consola(nombre: str, precio: float, fecha_lanzamiento: date, empresa_id: int):
    """
    Crear una nueva consola en la base de datos
    """
    with db_session() as db:
        # Verificar que la empresa existe
        empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
        if not empresa:
            print(f"❌ No existe empresa con ID: {empresa_id}")
            return None
        
        nueva_consola = Consola(
            nombre=nombre,
            precio=precio,
            fecha_lanzamiento=fecha_lanzamiento,
            empresa_id=empresa_id
        )
        db.add(nueva_consola)
        db.flush()
        print(f"✅ Consola '{nombre}' creada con ID: {nueva_consola.id}")
        return nueva_consola.id

def leer_todas_consolas():
    """
    Obtener todas las consolas de la base de datos
    """
    with db_session() as db:
        consolas = db.query(Consola).all()
        print(f"📋 Se encontraron {len(consolas)} consolas:")
        for consola in consolas:
            empresa_nombre = consola.empresa.nombre if consola.empresa else "Sin empresa"
            print(f"  - ID: {consola.id}, Nombre: {consola.nombre}, Precio: ${consola.precio}, Empresa: {empresa_nombre}")
        return consolas

def leer_consola_por_id(consola_id: int):
    """
    Obtener una consola específica por su ID
    """
    with db_session() as db:
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        if consola:
            empresa_nombre = consola.empresa.nombre if consola.empresa else "Sin empresa"
            print(f"🔍 Consola encontrada: {consola.nombre} (Empresa: {empresa_nombre}, Precio: ${consola.precio})")
            return consola
        else:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return None

def actualizar_consola(consola_id: int, nuevo_nombre: str = None, nuevo_precio: float = None, 
                      nueva_fecha: date = None, nueva_empresa_id: int = None):
    """
    Actualizar los datos de una consola existente
    """
    with db_session() as db:
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        if consola:
            if nuevo_nombre:
                consola.nombre = nuevo_nombre
            if nuevo_precio:
                consola.precio = nuevo_precio
            if nueva_fecha:
                consola.fecha_lanzamiento = nueva_fecha
            if nueva_empresa_id:
                # Verificar que la nueva empresa existe
                empresa = db.query(Empresa).filter(Empresa.id == nueva_empresa_id).first()
                if empresa:
                    consola.empresa_id = nueva_empresa_id
                else:
                    print(f"❌ No existe empresa con ID: {nueva_empresa_id}")
                    return False
            print(f"✏️ Consola ID {consola_id} actualizada correctamente")
            return True
        else:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return False

def eliminar_consola(consola_id: int):
    """
    Eliminar una consola de la base de datos
    """
    with db_session() as db:
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        if consola:
            nombre_consola = consola.nombre
            db.delete(consola)
            print(f"🗑️ Consola '{nombre_consola}' eliminada correctamente")
            return True
        else:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return False

# ==================== CRUD PARA JUEGOS ====================

def crear_juego(nombre: str):
    """
    Crear un nuevo juego en la base de datos
    """
    with db_session() as db:
        nuevo_juego = Juego(nombre=nombre)
        db.add(nuevo_juego)
        db.flush()
        print(f"✅ Juego '{nombre}' creado con ID: {nuevo_juego.id}")
        return nuevo_juego.id

def leer_todos_juegos():
    """
    Obtener todos los juegos de la base de datos
    """
    with db_session() as db:
        juegos = db.query(Juego).all()
        print(f"📋 Se encontraron {len(juegos)} juegos:")
        for juego in juegos:
            consolas_nombres = [consola.nombre for consola in juego.consolas]
            print(f"  - ID: {juego.id}, Nombre: {juego.nombre}, Consolas: {consolas_nombres}")
        return juegos

def leer_juego_por_id(juego_id: int):
    """
    Obtener un juego específico por su ID
    """
    with db_session() as db:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if juego:
            consolas_nombres = [consola.nombre for consola in juego.consolas]
            print(f"🔍 Juego encontrado: {juego.nombre} (Disponible en: {consolas_nombres})")
            return juego
        else:
            print(f"❌ No se encontró juego con ID: {juego_id}")
            return None

def actualizar_juego(juego_id: int, nuevo_nombre: str):
    """
    Actualizar el nombre de un juego existente
    """
    with db_session() as db:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if juego:
            juego.nombre = nuevo_nombre
            print(f"✏️ Juego ID {juego_id} actualizado correctamente")
            return True
        else:
            print(f"❌ No se encontró juego con ID: {juego_id}")
            return False

def eliminar_juego(juego_id: int):
    """
    Eliminar un juego de la base de datos
    """
    with db_session() as db:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if juego:
            nombre_juego = juego.nombre
            db.delete(juego)
            print(f"🗑️ Juego '{nombre_juego}' eliminado correctamente")
            return True
        else:
            print(f"❌ No se encontró juego con ID: {juego_id}")
            return False

# ==================== FUNCIONES PARA RELACIÓN JUEGOS-CONSOLAS ====================

def agregar_juego_a_consola(juego_id: int, consola_id: int):
    """
    Asociar un juego con una consola (relación muchos a muchos)
    """
    with db_session() as db:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        
        if not juego:
            print(f"❌ No se encontró juego con ID: {juego_id}")
            return False
        if not consola:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return False
        
        if consola not in juego.consolas:
            juego.consolas.append(consola)
            print(f"✅ Juego '{juego.nombre}' agregado a consola '{consola.nombre}'")
            return True
        else:
            print(f"⚠️ El juego '{juego.nombre}' ya está disponible en '{consola.nombre}'")
            return False

def quitar_juego_de_consola(juego_id: int, consola_id: int):
    """
    Quitar la asociación entre un juego y una consola
    """
    with db_session() as db:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        
        if not juego:
            print(f"❌ No se encontró juego con ID: {juego_id}")
            return False
        if not consola:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return False
        
        if consola in juego.consolas:
            juego.consolas.remove(consola)
            print(f"🗑️ Juego '{juego.nombre}' quitado de consola '{consola.nombre}'")
            return True
        else:
            print(f"⚠️ El juego '{juego.nombre}' no está disponible en '{consola.nombre}'")
            return False

def listar_juegos_por_consola(consola_id: int):
    """
    Mostrar todos los juegos disponibles para una consola específica
    """
    with db_session() as db:
        consola = db.query(Consola).filter(Consola.id == consola_id).first()
        if consola:
            print(f"🎮 Juegos disponibles para {consola.nombre}:")
            for juego in consola.juegos:
                print(f"  - {juego.nombre}")
            return consola.juegos
        else:
            print(f"❌ No se encontró consola con ID: {consola_id}")
            return []