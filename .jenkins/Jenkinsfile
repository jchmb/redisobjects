pipeline {
    agent {
        docker {
            image 'python:3.6-alpine3.9'
        }
    }

    triggers {
        pollSCM('*/5 * * * 1-5')
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python setup.py install'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
