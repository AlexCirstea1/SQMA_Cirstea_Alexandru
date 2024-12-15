pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexCirstea1/SQMA_Cirstea_Alexandru.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    echo "Setting up Python environment"
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            parallel {
                stage('Test Case 1') {
                    steps {
                        sh '''
                            echo "Running Test Case 1"
                            source venv/bin/activate
                            python tests/test_case1.py
                        '''
                    }
                }
                stage('Test Case 2') {
                    steps {
                        sh '''
                            echo "Running Test Case 2"
                            source venv/bin/activate
                            python tests/test_case2.py
                        '''
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                    echo "Cleaning up environment"
                    rm -rf venv
                '''
            }
        }
    }

    post {
        always {
            junit 'test-reports/*.xml'
            archiveArtifacts artifacts: 'test-reports/*.xml', allowEmptyArchive: true
            echo 'Pipeline completed.'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed. Check the console output for details.'
        }
    }
}
