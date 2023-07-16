pipeline {
    agent any
    environment {
        AWS_EC2_JENKINS_PRIVATE_KEY=credentials('AWS_EC2_JENKINS_PRIVATE_KEY') 
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }
    stages {
        stage('Deploy Python App') {
            steps {
                script {
                    // Set JENKINS_WORKSPACE_PATH using the Jenkins WORKSPACE variable
                    def JENKINS_WORKSPACE_PATH = "${WORKSPACE}"

                    // Execute Ansible playbook with the updated JENKINS_WORKSPACE_PATH
                    sh "ansible-playbook -i inventory playbook.yml --private-key=$AWS_EC2_JENKINS_PRIVATE_KEY --extra-vars=\"jenkins_workspace_path=${JENKINS_WORKSPACE_PATH} openai_api_key_value=${OPENAI_API_KEY}\""
                }
            }
        }
    }
}
