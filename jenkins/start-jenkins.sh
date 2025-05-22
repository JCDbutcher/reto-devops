#!/bin/bash

set -e  # Detiene el script si algún comando falla

echo " Iniciando Jenkins con Docker Compose..."

# Verifica que docker-compose.yml existe
if [ ! -f docker-compose.yml ]; then
  echo " No se encontró docker-compose.yml en el directorio actual."
  exit 1
fi

# Levanta Jenkins en segundo plano
docker-compose up -d

# Espera unos segundos para que arranque Jenkins
echo " Esperando a que Jenkins se inicie..."
sleep 5

# Verifica si el contenedor está corriendo
if docker ps --format '{{.Names}}' | grep -q '^jenkins$'; then
  echo " Jenkins se está ejecutando en: http://localhost:8080"
else
  echo " Error: El contenedor de Jenkins no está corriendo."
  docker-compose logs jenkins
fi
