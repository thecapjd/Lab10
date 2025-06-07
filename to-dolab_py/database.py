from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database - se crea automáticamente
SQLALCHEMY_DATABASE_URL = "sqlite:///./laboratorio.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Necesario para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para obtener la sesión de BD en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()