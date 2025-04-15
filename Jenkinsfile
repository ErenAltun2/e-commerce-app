pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    // Sonar-scanner path'ini ekliyoruz
                    sh '''
                        export PATH=$PATH:/opt/sonar-scanner/bin
                        . venv/bin/activate && sonar-scanner -Dsonar.projectKey=e-commerce-app -Dsonar.host.url=http://10.25.155.206:9000 -Dsonar.login=sqp_00dc0840d8f43891d278f3a75badc3305c741502
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop e-commerce-app || true'
                sh 'docker rm e-commerce-app || true'
                sh 'docker run -d -p 5000:5000 --name e-commerce-app erenaltun/e-commerce-app:latest'
            }
        }
    }
}
