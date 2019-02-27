node('rh6') {
    checkout scm

    withEnv(["CONAN_USER_HOME=${env.WORKSPACE}"]) {
        stage('Install Conan on Linux') {
            sh 'scl enable rh-python36 .jenkins/install.sh'
        }
        stage('Build packages on Linux') {
            sh 'conan/bin/python build.py'
        }
    }
}

node('windows') {
    checkout scm

    withEnv(["CONAN_USER_HOME=${env.WORKSPACE}"]) {
        stage('Install Conan on Windows') {
            bat '.jenkins\install.bat'
        }
        stage('Build packages on Windows') {
            bat 'conan\Scripts\python build.py'
        }
    }
}
