node{
   stage('SCM Checkout'){
       git 'https://github.com/vidyanathreddy/pytest'
   }
   
   stage('Build Docker Image'){
     sh 'docker build -t devopsvidya/app2 .'
   }
   stage('Push Docker Image'){
     withCredentials([string(credentialsId: 'dock-pwd', variable: 'DHP')]) {
        sh "docker login -u devopsvidya -p ${DHP}"
     }
     sh 'docker push devopsvidya/app2'
   }
   stage('Run Container'){
     sh 'docker run -it -p84:80 -d devopsvidya/app2'
     
   }
}
