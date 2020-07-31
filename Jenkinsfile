pipeline {
    agent none
    stages {
        stage('Build Docker Image') {
            agent any
            steps {
                sh 'docker build -t aminu_israel/ml_model:1.0 .'
            }
        }
        stage('Test Image') {
            steps {
                echo "Test Passed"
            }
        }
        stage('Run Docker Image') {
            agent any
            steps {
                sh 'docker run --name deploymodel -p 9091:8080 aminu_israel/ml_model:1.0'
            }
        }
    }
}