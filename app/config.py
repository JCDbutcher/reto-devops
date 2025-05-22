import os


class Config:
    """Configuración base compartida por todos los entornos"""
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Configuración específica para testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # DB en memoria


class DevelopmentConfig(Config):
    """Configuración específica para desarrollo"""
    DEBUG = True


class ProductionConfig(Config):
    """Configuración específica para producción"""
    DEBUG = False


# Diccionario para acceder a las configuraciones por nombre
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
