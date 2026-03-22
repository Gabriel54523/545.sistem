import os
from datetime import timedelta

class Config:
    """Configuración base de la aplicación"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', '/var/log/inventario/app.log')

class DevelopmentConfig(Config):
    """Configuración de desarrollo"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///inventario.db'
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Configuración de producción"""
    DEBUG = False
    TESTING = False

    # SECRET_KEY desde variable de entorno (obligatoria en producción)
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

    # Base de datos: PostgreSQL si está configurado, si no SQLite (funcional en Windows)
    _db_url = os.getenv('DATABASE_URL')
    if _db_url:
        SQLALCHEMY_DATABASE_URI = _db_url
    elif os.getenv('DB_PASSWORD') or os.getenv('USE_POSTGRES'):
        DB_USER = os.getenv('DB_USER', 'inventario')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = os.getenv('DB_PORT', '5432')
        DB_NAME = os.getenv('DB_NAME', 'inventario_db')
        SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    else:
        # SQLite por defecto: funcional sin PostgreSQL (ideal para desarrollo/despliegue simple)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///inventario.db'

    SQLALCHEMY_ECHO = False
    
    # Seguridad
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    PREFERRED_URL_SCHEME = 'https'

class TestingConfig(Config):
    """Configuración de pruebas"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
