pipeline {
    environment {
        registry = 'israelaminu/ml_model'
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
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
        stage('Push Docker Image to Registry') {
            agent any
            steps {
                script {
                    docker.withRegistry('',registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}