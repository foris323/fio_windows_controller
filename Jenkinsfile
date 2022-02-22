def remote = [:]
remote.name = 'node-1'
remote.host = params.client
remote.user = 'administrator'
remote.allowAnyHosts = true
currentBuild.description = env.Description

node {
    withCredentials(
            [
                sshUserPrivateKey(
                    credentialsId: 'ubuntu_clinet',
                    keyFileVariable: 'identity',
                    passphraseVariable: '',
                    usernameVariable: 'userName',
                    passwordVariable: 'PASSWORD'
                )
            ]
    ) {
        remote.user = userName
        remote.password  = PASSWORD
        stage('Env Preparing') {
            sshCommand remote: remote, command: 'taskkill /f /T /IM fio.exe'
        }

        stage('FIO random read') {
            command = "fio -filename=${env.drive}:\\fio -direct=1 -iodepth 1" +
            ' -thread -rw=randread -ioengine=windowsaio' +
            " -bs=16k -size=${env.TestSize} -numjobs=30 -runtime=1000 -group_reporting" +
            ' -name=randread --output=randread.log --output-format=json'
            sshCommand remote: remote, command: command
        }
        // stage("FIO sequential read") {
        //     command = "sudo fio -filename=${env.drive} -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=16k -size=${env.TestSize}G -numjobs=30 -runtime=1000 -group_reporting -name=read>read.log"
        //     sshCommand remote: remote, command: command
        // }
        // stage("FIO random write") {
        //     command = "sudo fio -filename=${env.drive} -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=16k -size=${env.TestSize}G -numjobs=30 -runtime=1000 -group_reporting -name=randwrite>randwrite.log"
        //     sshCommand remote: remote, command: command
        // }
        // stage("FIO sequential write") {
        //     command = "sudo fio -filename=${env.drive} -direct=1 -iodepth 1 -thread -rw=write -ioengine=psync -bs=16k -size=${env.TestSize}G -numjobs=30 -runtime=1000 -group_reporting -name=write>write.log"
        //     sshCommand remote: remote, command: command
        // }
        stage('collect data') {
            sshGet remote: remote, from: 'randread.log', into: 'randread.log', override: true
            // sshGet remote: remote, from: 'write.log', into: 'write.log', override: true
            // sshGet remote: remote, from: 'randwrite.log', into: 'randwrite.log', override: true
            // sshGet remote: remote, from: 'read.log', into: 'read.log', override: true
            sh 'cat randread.log'
        // sh "cat read.log"
        // sh "cat write.log"
        // sh "cat randwrite.log"
        }
    //     stage("plot"){
    //         plot csvSeries: [[
    //                         file: 'data.csv',
    //                         exclusionValues: '',
    //                         displayTableFlag: false,
    //                         inclusionFlag: 'OFF',
    //                         url: '']],
    //         csvFileName: "plot-iops.csv",
    //         group: 'Plot Group',
    //         title: 'FIO test',
    //         style: 'line',
    //         exclZero: false,
    //         keepRecords: false,
    //         logarithmic: false,
    //         numBuilds: '10',
    //         useDescr: true,
    //         yaxis: 'iops',
    //         yaxisMaximum: '',
    //         yaxisMinimum: ''
    //         }
    }
}
