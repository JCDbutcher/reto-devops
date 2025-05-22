# Imagen base
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Copiar dependencias y instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Puerto que expone Flask (si aplica)
EXPOSE 5000

# Comando por defecto al iniciar el contenedor
CMD ["python", "run.py"]
