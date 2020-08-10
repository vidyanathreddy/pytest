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
                        sh "scp deploy.yml deploy-services.yml ubuntu@13.127.234.22:~"
                        script{
                            try{


                                sh "ssh ubuntu@13.127.234.22 kubectl apply -f ."



                            }
                            catch(error){

                                sh "ssh ubuntu@13.127.234.22 kubectl create -f ."
                            }
                        }
                        
                }
        }
    }
}                                                      

