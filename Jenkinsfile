pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop e-commerce-app || true'
                sh 'docker rm e-commerce-app || true'
                sh 'docker network create my-network || true'
                sh 'docker run -d -p 5000:5000 --name e-commerce-app --network my-network erenaltun/e-commerce-app:latest'
                sh 'sleep 5'  // Konteynerin başlaması için bekle
                sh 'docker exec heuristic_keller curl --fail http://10.30.3.43:5000 || exit 1'  // Sağlık kontrolü
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    Xvfb :99 -ac &  # Sanal ekran başlat
                    export DISPLAY=:99
                    pytest tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        export PATH=$PATH:/opt/sonar-scanner/bin
                        . venv/bin/activate && sonar-scanner -Dsonar.projectKey=e-commerce-app -Dsonar.host.url=http://10.30.3.43:9000 -Dsonar.login=sqp_00dc0840d8f43891d278f3a75badc3305c741502
                    '''
                }
            }
        }

        stage('UI Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    Xvfb :99 -ac &
                    export DISPLAY=:99
                    python tests/test_ui.py
                '''
            }
        }
    }

    post {
        success {
            slackSend channel: '#devops', message: "Build succeeded: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
        failure {
            slackSend channel: '#devops', message: "Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
