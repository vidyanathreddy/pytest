pipeline {
    agent any
    stages{
        stage('Git CheckOut'){
            steps{
                git 'https://github.com/vidyanathreddy/pytest'
            }
        }
    }

    stages{
    	stage('Build Image'){
    		steps{
    			sh "docker stop $(docker ps -aq)"
     			sh "docker rm $(docker ps -aq)"
     			sh "docker rmi $(docker images -q)"
     			sh "docker build -t devopsvidya/app2 ."
			}
		}
    	stage('Push Image'){
    		steps{
    			withCredentials([string(credentialsId: 'dock-pwd', variable: 'DHP')]){
    				sh "docker login -u devopsvidya -p ${DHP}"
				}

				sh "docker push devopsvidya/app2"
			}
		}
    	stage('Run Cont'){
    		steps{
    			sh "docker run -it -p84:80 -d devopsvidya/app2"
    		}
    	}
    }
}
    
