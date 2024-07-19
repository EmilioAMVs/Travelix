# from app.config import Config
# from sqlalchemy import create_engine, text

# Prueba la conexión a la base de datos
# try:
    engine = create_engine(Config.DATABASE_URL)
    connection = engine.connect()
    
    result = connection.execute(text("SELECT DB_NAME() AS DatabaseName"))
    db_name = result.scalar()
    
    print(f"Conexión exitosa a la base de datos: {db_name}!")
    connection.close()
# except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
