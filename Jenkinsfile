pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKER_IMAGE = "juanca547/reto_devops"
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Instalando dependencias de Python...'
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar tests') {
            steps {
                echo 'Ejecutando tests con cobertura...'
                sh '''
                    pytest --cov=app --cov-report=term-missing
                '''
            }
        }

        stage('Lint con flake8') {
            steps {
                echo 'Verificando estilo de código con flake8...'
                sh '''
                    pip install flake8
                    flake8 app/ --max-line-length=120
                '''
            }
        }

        stage('Construir imagen Docker') {
            steps {
                echo "Construyendo imagen: $DOCKER_IMAGE:$DOCKER_TAG"
                sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
            }
        }

        stage('Push a Docker Hub') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                    branch 'develop'
                }
            }
            steps {
                echo "Subiendo imagen a Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Limpieza de Docker local'
            sh 'docker system prune -f || true'
        }
    }
}
