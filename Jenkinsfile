pipeline {
    agent any  // Ejecuta en cualquier agente disponible (incluido el contenedor por defecto)

    environment {
        DOCKER_IMAGE = "juanca547/reto_devops"  // Nombre base de la imagen Docker
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"  // Etiqueta dinámica por rama y build
    }

    stages {

        stage('Preparar entorno') {
            steps {
                sh '''
                    set -e  # Detener el script si algún comando falla

                    echo "Verificando Docker..."
                    command -v docker || { echo "Docker no disponible"; exit 127; }

                    echo " Instalando dependencias para entorno virtual..."
                    apt-get update && apt-get install -y python3-venv

                    echo " Creando entorno virtual..."
                    python3 -m venv venv

                    # Verificación de creación exitosa del entorno virtual
                    if [ ! -f "venv/bin/activate" ]; then
                        echo " No se creó el entorno virtual correctamente"
                        exit 1
                    fi

                    echo " Activando entorno e instalando dependencias..."
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    echo "Ejecutando tests con cobertura..."
                    . venv/bin/activate

                    # Evita error: ModuleNotFoundError: No module named 'app'
                    export PYTHONPATH=$(pwd)

                    pytest --cov=app --cov-report=term-missing
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    echo " Ejecutando flake8 (lint)..."
                    . venv/bin/activate
                    pip install flake8
                    flake8 app/ --max-line-length=120
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh '''
                    echo "Construyendo imagen Docker..."
                    docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage('Push Docker') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                    branch 'develop'
                }
            }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "Pushing imagen a Docker Hub..."
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Post-pipeline cleanup'
                try {
                    // Limpieza opcional de contenedores/imágenes viejas (no es crítico si falla)
                    sh 'docker system prune -f || true'
                } catch (Exception e) {
                    echo " Limpieza falló pero el pipeline continúa"
                }
            }
        }
    }
}
