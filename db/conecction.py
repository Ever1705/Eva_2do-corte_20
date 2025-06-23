from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

DATABASE_URL = "sqlite:///./db.sqlite"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def db_session():
    db = SessionLocal() 
    
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e  
    finally:
        db.close()