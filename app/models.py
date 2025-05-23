from app import db

class Data(db.Model):
    """
    Modelo de base de datos que representa un registro de datos simple.
    """
    id = db.Column(db.Integer, primary_key=True)  # ID único autoincremental
    name = db.Column(db.String(100))              # Campo de texto para el nombre

    def __repr__(self):
        """
        Representación legible del objeto, útil para depuración.
        """
        return f"<Data id={self.id} name={self.name}>"
