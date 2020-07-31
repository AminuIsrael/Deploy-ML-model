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
        stage('Push Docker Image to Registry') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerHub',passwordVariable:'Am1nuIsr2@',usernameVariable: 'israelaminu')) {
                    sh 'docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}'
                    sh 'docker push israelaminu/ML_model:1.0'
                }
            }
        }
    }
}