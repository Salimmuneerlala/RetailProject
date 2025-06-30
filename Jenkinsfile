pipeline {
    agent any

    environment {
        JAVA_HOME = '/opt/bitnami/java'  // Set your JAVA_HOME path
        PATH = "${env.JAVA_HOME}/bin:${env.PATH}"
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')  // Access Key ID
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')  // Secret Access Key
        AWS_DEFAULT_REGION = 'ap-south-1'  // Set your AWS region
        S3_BUCKET_NAME = 'general-iamdave-mumbai' // Set your S3 bucket name
    }
    
    
    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv retail_pipeline_venv'
                    sh './retail_pipeline_venv/bin/pip install --upgrade pip'
                    sh './retail_pipeline_venv/bin/pip install pipenv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install project dependencies
                    sh './retail_pipeline_venv/bin/pipenv install'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh './retail_pipeline_venv/bin/pipenv run pytest'
                }
            }
        }
        stage('Package') {
            steps {
                script {
                    // Create the zip file excluding the venv directory
                    sh 'zip -r retailproject.zip . -x "retail_pipeline_venv/*"'
                }
            }
        }
        stage('Deploy to S3') {
            steps {
                script {
                    // Deploy to Amazon S3
                    sh ''' 
                    aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
                    aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
                    aws configure set default.region ${AWS_DEFAULT_REGION}
                    '''

                    // Copy the zip file to the specified S3 bucket
                    sh "aws s3 cp retailproject.zip s3://${env.S3_BUCKET_NAME}/"
                }
            }
        }
    }
}
