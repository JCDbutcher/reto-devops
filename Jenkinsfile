pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "juanca547/reto_devops"
        BRANCH_NAME = "${env.BRANCH_NAME ?: 'main'}"  // Valor por defecto si no se detecta
    }

    stages {

        stage('Preparar entorno') {
            steps {
                sh '''
                    set -e
                    echo " Verificando Docker..."
                    command -v docker || { echo "Docker no disponible"; exit 127; }

                    echo " Instalando entorno virtual..."
                    apt-get update && apt-get install -y python3-venv

                    python3 -m venv venv
                    if [ ! -f "venv/bin/activate" ]; then
                        echo "Fallo creando entorno virtual"
                        exit 1
                    fi

                    echo "Instalando dependencias..."
                    . venv/bin/activate
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
                script {
                    def tag = "${BRANCH_NAME}-${env.BUILD_NUMBER}"
                    sh """
                        echo " Construyendo imagen Docker con tag: $tag"
                        docker build -t $DOCKER_IMAGE:$tag .
                    """
                }
            }
        }

        stage('Push Docker') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main' }
                    expression { env.BRANCH_NAME == 'master' }
                    expression { env.BRANCH_NAME == 'develop' }
                }
            }
            steps {
                script {
                    def tag = "${BRANCH_NAME}-${env.BUILD_NUMBER}"
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh """
                            echo "Subiendo imagen a Docker Hub..."
                            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                            docker push $DOCKER_IMAGE:$tag
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                echo '🧹 Limpieza post-pipeline'
                try {
                    sh 'docker system prune -f || true'
                } catch (Exception e) {
                    echo "Limpieza falló (no crítico)"
                }
            }
        }
    }
}


 /*       stage('Desplegar en servidor remoto') {
    when {
        branch 'main'
    }
    steps {
        sshagent(['mi-clave-ssh']) {
            sh '''
                ssh user@mi-servidor 'docker pull juanca547/reto_devops:main-${BUILD_NUMBER} &&
                                      docker stop reto_devops || true &&
                                      docker rm reto_devops || true &&
                                      docker run -d --name reto_devops -p 5000:5000 juanca547/reto_devops:main-${BUILD_NUMBER}'
            '''
        }
    }
}
*/
