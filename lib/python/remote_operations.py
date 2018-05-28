# -*- coding: utf-8 -*- 

def remote_operation(sshhost,username,passwd,cmds,\
    confirmflag = 1,\
    confirmobj = '',\
    confirmobjcount = 1,\
    sshport = 22,\
    outlog ='sshout.log',\
    errorlog ='ssherror.log',\
    paramikologenable = 0 \
    ):     
    
    """This function will used to do remote operations through ssh"""

    import paramiko                   # third party libs needs for ssh authentication

    sshhost = sshhost                 # ssh destination hosts,can be IP or resolvable hostnames
    username = username                       # account-name used to establish ssh connection
    passwd = passwd                   # account-password used to establish ssh connection
    cmds = cmds                       # the commands going to run via ssh
    confirmflag = confirmflag         # if need check the outcome to confirm operation success or failed,default 1
    confirmobj = confirmobj           # the target need to to compared or searched or confirmed,default empty
    confirmobjcount = confirmobjcount # the accurance of confirmobj,default 1
    sshport = sshport                     # defaule ssh connection port ,22 by default
    outlog = outlog                       # normal ssh log file
    errorlog = errorlog                   # error ssh log file
    paramikologenable = paramikologenable # by default, paramikologdisabled ,set to 1 to enable            

    
    if paramikologenable == 1:
        paramiko.util.log_to_file('ssh.log') #set up paramiko logging,disbale by default
            
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = sshhost, port = sshport, username = username, password = passwd)

    stdin, stdout, stderr = ssh.exec_command(cmds)
    okout = stdout.read()
    errout = stderr.read()
    #print ('err:'+str(errout,'utf-8'))
    #print ('ok:'+str(okout,'utf-8'))
    if confirmflag == 1:
        if len(okout) == 0:  
            out=str(errout,'utf-8')
            print(out,end = '')
            
            #write error log to file
            with open(errorlog,'a') as file_object_err:
                file_object_err.write(out)
            print (out.count(confirmobj))
            if out.count(confirmobj) == confirmobjcount:
                print('\033[1;32m  Operation success\033[0m')
            else:
                print ('\033[1;31m  Operation failed,no need to continue,please check'+errorlog+'!\033[0m')
        else:
            out=str(okout,'utf-8')
            print(out,end = '')
            
            #write out log to file
            with open(outlog,'a') as file_object_ok:
                file_object_ok.write(out)
            print (out.count(confirmobj))
            if out.count(confirmobj) == confirmobjcount:

                print('\033[1;32m  Operation success\033[0m')
            else:
                print('\033[1;31m  Operation failed\033[0m')
    else:
        print ('\033[1;32m  Operation success\033[0m')
    ssh.close()