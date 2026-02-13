pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "us-east-1"
        DOCKER_IMAGE = "vijayendra1/poc13-app"
    }

    stages {

        '''stage('Checkout') {
            steps {
                git branch: 'main',
                    url: git 'https://github.com/vijayendra-b/k8s-jenkins-terraform.git'
            }
        }'''

        stage('Terraform Init') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                dir('terraform') {
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh 'docker build -t $DOCKER_IMAGE:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }

        stage('Update kubeconfig') {
            steps {
                sh 'aws eks update-kubeconfig --region $AWS_DEFAULT_REGION --name poc13-eks-cluster'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
