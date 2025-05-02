from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite uchun .env faylingizda shunday yozing: DATABASE_URL=sqlite:///./test.db
DATABASE_URL =  "sqlite:///./test.db"

# SQLite uchun connect_args kerak, aks holda ba'zi xatoliklar bo'lishi mumkin
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
