from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/db_training"
DATABASE_URL = "postgresql+psycopg2://training_db_zxhv_user:hGIRDDqC40KjceSnJtumrr72uioBnRq2@dpg-dbc7e60473hc73fc6sng-a.virginia-postgres.render.com/training_db_zxhv"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()