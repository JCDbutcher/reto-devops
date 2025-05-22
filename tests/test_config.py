"""
test_config.py
---------------
Este archivo contiene pruebas para la configuración de la aplicación.
Se asegura que los valores de configuración por entorno sean los esperados.
"""

from app.config import config_dict

# Verifica que la configuración de desarrollo tenga DEBUG=True
def test_development_config():
    dev_config = config_dict["development"]()
    assert dev_config.DEBUG is True
    assert dev_config.SQLALCHEMY_TRACK_MODIFICATIONS is False

# Verifica que la configuración de producción tenga DEBUG=False
def test_production_config():
    prod_config = config_dict["production"]()
    assert prod_config.DEBUG is False
    assert prod_config.SQLALCHEMY_TRACK_MODIFICATIONS is False
