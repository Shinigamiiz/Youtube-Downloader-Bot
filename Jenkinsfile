pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/DevOlabodeM/pytest-intro-vs-M']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/DevOlabodeM/pytest-intro-vs-M'
                sh 'rm .env'
                sh 'touch .env'
                sh 'echo "TOKEN=6029591492:AAGpbHWKlTCYegMipoNqBHkfi6YhCWo2UYQ" >> .env'
                sh 'echo "ADMIN=664884438" >> .env'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python3 main.py > logfile.log &2>&1 &'
            }
        }
        stage('Run') {
            steps {
                sh 'nohup python3 main.py > logfile.log &2>&1 &'
            }
        }
    }
}
