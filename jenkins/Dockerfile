# Dockerfile
FROM jenkins/jenkins:lts

USER root

# Instala Docker CLI dentro del contenedor de Jenkins
RUN apt-get update && \
    apt-get install -y docker.io && \
    usermod -aG docker jenkins

USER jenkins
