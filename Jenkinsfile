pipeline {
    agent any  // Ejecuta el pipeline en cualquier agente disponible

    environment {
        DOCKER_IMAGE = "juanca547/reto_devops"  // Nombre de la imagen Docker
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"  // Etiqueta dinámica para la imagen
    }

    stages {

        stage('Preparar entorno') {
            steps {
                sh '''
                    echo " Verificando Docker..."
                    command -v docker || { echo " Docker no disponible"; exit 127; }

                    echo " Creando entorno virtual..."
                    apt-get update && apt-get install -y python3-venv

                    echo " Activando entorno virtual..."
                    . venv/bin/activate

                    echo " Instalando dependencias..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    echo " Ejecutando tests con cobertura..."
                    . venv/bin/activate

                    # Añadir el directorio actual al PYTHONPATH para evitar el error 'No module named app'
                    export PYTHONPATH=$(pwd)

                    pytest --cov=app --cov-report=term-missing
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    echo " Ejecutando flake8..."
                    . venv/bin/activate
                    pip install flake8
                    flake8 app/ --max-line-length=120
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh '''
                    echo " Construyendo imagen Docker..."
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo " Pushing imagen a Docker Hub..."
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
                    // Limpieza de recursos Docker (no es crítico si falla)
                    sh 'docker system prune -f || true'
                } catch (Exception e) {
                    echo " Limpieza falló pero el pipeline continúa"
                }
            }
        }
    }
}
