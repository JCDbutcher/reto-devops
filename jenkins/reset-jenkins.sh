#!/bin/bash

echo "Limpiando entorno de Jenkins..."

# Detener y eliminar contenedor
docker rm -f jenkins 2>/dev/null && echo " Contenedor 'jenkins' eliminado" || echo " Contenedor 'jenkins' no encontrado"

# Eliminar volumen
docker volume rm jenkins_home 2>/dev/null && echo " Volumen 'jenkins_home' eliminado" || echo " Volumen 'jenkins_home' no encontrado"

# Eliminar imagen (opcional)
docker rmi jenkins/jenkins:lts 2>/dev/null && echo " Imagen 'jenkins/jenkins:lts' eliminada" || echo " Imagen Jenkins no encontrada o en uso"

# Limpiar contenedores dangling (opcional)
docker system prune -f --volumes

echo "Jenkins ha sido reseteado correctamente"
