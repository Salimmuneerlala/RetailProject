pipeline {
    agent any
    environment {
        LABS = credentials('labcreds')
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        S3_BUCKET = 'your-s3-bucket-name' // Replace with your S3 bucket name.
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install --user pipenv'
                sh '/bitnami/jenkins/home/.local/bin/pipenv --rm || exit 0'
                sh '/bitnami/jenkins/home/.local/bin/pipenv install'
            }
        }
        stage('Test') {
            steps {
                sh '/bitnami/jenkins/home/.local/bin/pipenv run pytest'
            }
        }
        stage('Package') {
            steps {
                sh 'zip -r retailproject.zip .'
            }
        }
        stage('Deploy') {
            steps {
                // Configure AWS CLI
                sh 'aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID'
                sh 'aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY'
                sh 'aws configure set default.region us-east-1' // Set your AWS region here

                // Upload the zip file to S3
                sh 'aws s3 cp retailproject.zip s3://$S3_BUCKET/retailproject.zip'
            }
        }
    }
}
