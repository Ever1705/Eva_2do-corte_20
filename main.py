from core.models import Base
from db.conecction import engine
from core.view import main

if __name__ == "__main__":

    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas exitosamente")
    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")
    
    # Inicio de la interfaz
    main()