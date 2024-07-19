from infrastructure.databases.user import user, password 

class Config:
    APP_NAME = "Travelix"
    VERSION = "1.0.0"
    DEBUG = True

    DATABASE_URL = (
        f"mssql+pyodbc://{user}:{password}@travelixdb.database.windows.net:1433/"
        "userflight?driver=ODBC+Driver+17+for+SQL+Server"
    )

    JWT_SECRET_KEY = "your-secret-key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_TIME_MINUTES = 30
