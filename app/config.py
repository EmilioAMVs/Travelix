class Config:
    # Aquí puedes definir variables de configuración para tu aplicación
    APP_NAME = "Travelix"
    VERSION = "1.0.0"
    DEBUG = True

    # Configuraciones de la base de datos
    DATABASE_URL = "sqlite:///./test.db"  # Ejemplo de URL de una base de datos SQLite

    # Configuraciones de JWT u otros middleware que se necesiten
    JWT_SECRET_KEY = "your-secret-key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_TIME_MINUTES = 30
