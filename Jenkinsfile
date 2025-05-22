pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "juanca547/reto_devops"  // Cambia por tu imagen si es diferente
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    }

    stages {

        stage('Preparar entorno') {
            steps {
                echo 'Clonando código y preparando entorno virtual...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar tests') {
            steps {
                echo 'Ejecutando pruebas unitarias con cobertura...'
                sh '''
                    . venv/bin/activate
                    pytest --cov=app --cov-report=term-missing
                '''
            }
        }

        stage('Lint con flake8') {
            steps {
                echo 'Validando estilo de código con flake8...'
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 app/ --max-line-length=120
                '''
            }
        }

        stage('Build imagen Docker') {
            steps {
                echo "Construyendo imagen Docker: $DOCKER_IMAGE:$DOCKER_TAG"
                sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
            }
        }

        stage('Push a Docker Hub') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                    branch 'master'
                }
            }
            steps {
                echo "Publicando imagen en Docker Hub..."
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
            echo 'Limpieza del entorno'
            sh 'docker system prune -f || true'
        }
    }
}
