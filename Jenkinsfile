pipeline {
    agent any
    stages{
        stage('Git CheckOut'){
            steps{
                git 'https://github.com/vidyanathreddy/pytest'
            }
        }

        stage('Build Image'){
            steps{
                
                
                sh 'docker rmi $(docker images -q)'
                sh 'docker build -t devopsvidya/app2 .'
            }
        }
        stage('Push Image'){
            steps{
                withCredentials([string(credentialsId: 'dock-pwd', variable: 'DHP')]){
                sh 'docker login -u devopsvidya -p ${DHP}'
                }
                sh 'docker push devopsvidya/app2'
            }
        }
        stage('Deploy to K8s'){
                steps{
                        sh "scp pods.yml services.yml ubuntu@13.126.236.224:~"
                        script{
                            try{


                                sh "ssh ubuntu@13.126.236.224 kubectl apply -f ."



                            }
                            catch(error){

                                sh "ssh ubuntu@13.126.236.224 kubectl create -f ."
                            }
                        }
                }
        }


    }
}

