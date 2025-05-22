"""
test_models.py
---------------
Este archivo contiene pruebas unitarias básicas para los modelos definidos en la aplicación.
Se verifica que los modelos se creen correctamente.
"""

from app.models import Data
# Prueba simple para verificar que se puede crear una instancia del modelo
def test_data_model_creation():
    item = Data(name="Test Item")
    assert item.name == "Test Item"
