pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/Vladikus004/cicd_with_docker', branch: 'main')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

    stage('build docker') {
      steps {
        sh 'sudo docker build -t pelanglene/test .'
      }
    }

  }
}