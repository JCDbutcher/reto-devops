pipeline {
    agent any

    environment {
<<<<<<< HEAD
        DOCKER_IMAGE = "juanca547/reto_devops"
=======
        DOCKER_IMAGE = "tuusuario/reto-devops"
>>>>>>> 949af94 (Add Jenkinsfile)
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    }

    stages {
<<<<<<< HEAD

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
=======
        stage('Clonar código') {
            steps {
                git branch: 'main', url: 'https://github.com/tuusuario/tu-repo.git'
            }
        }

        stage('Instalar dependencias y ejecutar tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest --cov=app --cov-report=term-missing'
            }
        }
        

        stage('Lint con flake8') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app/ --max-line-length=120'
>>>>>>> 949af94 (Add Jenkinsfile)
            }
        }

        stage('Build imagen Docker') {
            steps {
<<<<<<< HEAD
                echo "Construyendo imagen Docker: $DOCKER_IMAGE:$DOCKER_TAG"
                sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
=======
                script {
                    sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
                }
>>>>>>> 949af94 (Add Jenkinsfile)
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
<<<<<<< HEAD
                echo "Publicando imagen en Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
=======
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push $DOCKER_IMAGE:$DOCKER_TAG"
>>>>>>> 949af94 (Add Jenkinsfile)
                }
            }
        }
    }
<<<<<<< HEAD

    post {
        always {
            echo 'Limpieza del entorno'
            sh 'docker system prune -f || true'
        }
    }
=======
>>>>>>> 949af94 (Add Jenkinsfile)
}
