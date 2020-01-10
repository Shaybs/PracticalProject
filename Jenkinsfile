pipeline{
	environment
	{
		build_number = "${env.BUILD_NUMBER}"
	}
	agent any
	stages{
		stage("Update git repository") {
			steps{sh '''ssh 35.204.238.159 << EOF
                sudo su - jenkins
                alias docker-compose="/usr/local/bin/docker-compose"
				cd PracticalProject
                git checkout development-test
                git pull'''
			}
		}
		stage("Deploy") {
			steps{sh '''ssh 35.204.238.159 << EOF
                sudo su - jenkins
                alias docker-compose="/usr/local/bin/docker-compose"
				cd PracticalProject
                git checkout development-test

                export BUILD_NUMBER='${build_number}'
                docker-compose build
                '''
			}
		}
	}
}