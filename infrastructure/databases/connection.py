from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Config 


SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://a_travelix:adminT2024@travelixdb.database.windows.net:1433/userflight?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
