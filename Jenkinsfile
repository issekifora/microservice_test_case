pipeline {
  environment {
    registry = "registry.ifora.hse.ru/microservice_template"
    registryCredential = '2347b9bd-46aa-42ad-b775-758e40e83d80'
    dockerImageGit = ''
    dockerImageProd = ''
    GIT_TAG = "${BRANCH_NAME}"
  }
  agent any
  stages {
    stage('Установка зависимостей'){
    steps {
      withPythonEnv('/usr/bin/python3.5') {
        sh 'pip3 install -U tox'
        sh 'pip3 install -U tox-docker==1.2.1'
      }
    }
  }
   

  stage('Запуск unit тестов'){
    steps {
      withPythonEnv('/usr/bin/python3.5') {
        sh 'tox --skip-missing-interpreter -e basic'
      }
    }
  }


  stage('Сборка docker образа для prod'){
    when{buildingTag()}
    steps{
        script {
          dockerImageGit = docker.build registry + ":$GIT_TAG"
          dockerImageProd = docker.build registry + ":prod"        

      }
    }
  }

 stage('Подтвердить деплой на prod') {
   when {
    buildingTag()
   }
   steps {
    script {
     timeout(time: 15, unit: 'MINUTES') {
      input(id: "Deploy Gate", message: "Задеплоить на prod?", ok: 'Deploy')
     }
    }
   }
  }

 stage('Push docker образа prod в registry'){
     when{buildingTag()}
    steps{
        script {
          docker.withRegistry('https://registry.ifora.hse.ru', registryCredential ) {
          dockerImageGit.push()
          dockerImageProd.push()
       }
     }
    }
  }



stage('Деплой на prod службы api_template'){
    when{buildingTag()}
    steps{
       sshagent(credentials : ["25c5446e-05fc-400c-a7ad-e9bd4b3a26be"]) {
            sh 'ssh -o StrictHostKeyChecking=no jenkinsaccess@172.18.207.29 uptime'
             sh 'ssh -v jenkinsaccess@172.18.207.29 "docker service update --force  --with-registry-auth --image registry.ifora.hse.ru/microservice_template:prod api_template"'
       }
    }
  }


}
}


