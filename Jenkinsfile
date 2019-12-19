pipeline{
	agent any
	stages{
		stage("Update git repository") {
			steps{sh '''ssh 35.242.162.81  << EOF
                sudo su - jenkins
                alias docker-compose="/usr/local/bin/docker-compose"
				cd PracticalProject
                git checkout development
                git pull'''
			}
		}
		stage("Deploy") {
			steps{sh '''ssh 35.242.162.81  << EOF
                sudo su - jenkins
                alias docker-compose="/usr/local/bin/docker-compose"
				cd PracticalProject
                git checkout development
                docker-compose up -d --build'''
			}
		}
	}
}