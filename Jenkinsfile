pipeline {
  agent {
    docker {
      image 'python:3.12.3'
    }
  }

  stages {
    stage ('Test') {
      steps {
        sh 'python --version'
      }
    }
  }
}