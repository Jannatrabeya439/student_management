from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/db_training"
DATABASE_URL = "postgresql+psycopg2://student_db_myla_user:e2jTi3gxwpDD71L1VjlgnTIPq7Z29qRo@dpg-dbcthljrjlhs73elkf6g-a.oregon-postgres.render.com/student_db_myla"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()