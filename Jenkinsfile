pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from Git repository
                script {
                    git 'https://github.com/yourusername/yourrepository.git'
                }
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                // Build Docker image using Dockerfile
                script {
                    docker.build('your-docker-image-name:latest')
                }
                
                // Push Docker image to Docker registry
                script {
                    docker.withRegistry('https://your-docker-registry.com', 'your-docker-credentials-id') {
                        docker.image('your-docker-image-name:latest').push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Clean up workspace and resources
            deleteDir()
        }
    }
}
