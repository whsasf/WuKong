# -*- coding: utf-8 -*- 
# this module contains some functions that will used commenly


def welcome():
    """the welcome function used to print some welcome header when using this WuKOng test suits"""
    
    print('#'*100)
    print('#'*13,end=''),print("{:^74}".format('This is WuKong test suit, welcome!'),end=''),print('#'*13)
    print('#'*100,end='\n\n')
    


def parse_args():
    """this function used to parse the arguements providded,help determine the testcase location,logging levels,etc"""
     
    import sys
    import global_variables
    
    argvnum = len(sys.argv) # number of total argements,the real arguements number is 
    argvlist = sys.argv[1:] # total real arguments(shell name excludded)
    global_variables.set_value('argvnum',argvnum)   # store length of arguments into dict 
    global_variables.set_value('argvlist',argvlist) # store arguments into dict



def parse_chloglevel():
    """this function gte the chloglevel of this test"""
    
    parse_args()   # get all args            
    import global_variables
    
    argvlist = global_variables.get_value('argvlist')           # get argvlist of arguments
    if argvlist.count('-v') > 1 or argvlist.count('-vv') > 1:   # determine the chloglevel (displayed to screen)
        print("multiple '-v' or '-vv' detected,please make sure only one entered!")
        exit()
    elif argvlist.count('-v') == 1 or argvlist.count('-vv') == 1:
        if '-v' in argvlist:
            chloglevel = 'WARNING'
            argvlist.remove('-v')
        else:
            chloglevel = 'DEBUG'
            argvlist.remove('-vv')
    else:
        chloglevel = 'ERROR'
    global_variables.set_value('chloglevel',chloglevel) # store chloglevel into dict
    return chloglevel


    
#def log_all_args():
#    """This function used to log all arguments"""
#    
#    import basic_class
#    import global_variables
#    global_variables.get_value('argvlist',argvlist)
#    basic_class.mylogger.info('The testcase location paramaters are:'+str(argvlist))
#    basic_class.mylogger.info('The chloglevel is:'+str(argvlist))
    
#    print ("==> The testcase location paramaters are:\n",'    '+str(argvlist)), print()
#    print ("==> The chloglevel paramater is:\n",'    '+chloglevel), print()
#    return argvlist,chloglevel
    
    

            
def parse_testcaselocation(testcaselocation):
    """this function will chelk if the testcaselocation is:
    
       (1)the default testcase location:TestCases folder
       (2)some (any) individual folders of some testcases
       (3)a file ,that contains the location of testcases"""       
    import os
    # print(testcaselocation)   
    # print(len(testcaselocation))
    if len(testcaselocation) == 0 or  len(testcaselocation) == 1:
        if testcaselocation == [] or (testcaselocation[0] == 'Test_Cases' and testcaselocation[-1] == 'Test_Cases'):
            print("==> The testcase located in:\n",['Test_Cases']),print()            
            return (['Test_Cases'])
        elif os.path.isfile(testcaselocation[0]):
            with open(testcaselocation[0]) as file_obj:
                lines = file_obj.read().splitlines()
            print('==> The testcase located in:'),print()  
            for line in lines:
                print('    '+line.strip())
            return lines
        else:
            print("==> The testcase located in:\n",'    '+testcaselocation[0]),print()  
            testcaselocation
            return testcaselocation
    else:
        print('==> The testcase located in:')
        for testcase in testcaselocation:
            print('    '+testcase)
        return testcaselocation
        


def traverse_judge(casename,currentlists):
    """decide import or reload testcase file"""
    
    import os
    import sys
    import global_variables
    import time

    num = global_variables.get_value('num') 
    oldcasename = casename+'.py'
    
    if  oldcasename in currentlists:
        newcase = casename+str(num)
        newcasename = newcase+'.py'
        os.rename(oldcasename,newcasename)
        path = os.getcwd()
        #print(path)
        sys.path.append(path)
        
        try:
            __import__ (newcase)
            num += 1
            global_variables.set_value('num',num)
            time.sleep(0.01) #without this sleep, next "os.rename" command may failed

        finally:
            os.rename(newcasename,oldcasename) # must reverse name change anyway 
            del sys.modules[newcase]
        #os.remove(newcasename) 


                          
def traverse(Path):
    """traverse testcases under give Path,normal first execute setup,then run,last teardown for each testcase"""
    
    import os
    import sys

    os.chdir(Path)                 # switch to current Path
    
    currentlists = os.listdir('.') # get current folder and file names in current path
    for list in currentlists:      # delete the hiden files and folders
        if list.startswith('.'):
            currentlists.remove(list)
    for list in currentlists:      # delete the '__pycache__/' folderss
        if '__pycache__' in list:
            currentlists.remove(list)
            
    #print('currentlists:',currentlists)
    
    traverse_judge('setup',currentlists)      # run setup if exists
    traverse_judge('run',currentlists)        # run run if exists                
    for list in currentlists:
        if os.path.isdir(list):
            traverse(list)
            #os.chdir(list)
            #print (os.getcwd())        
    traverse_judge('teardown',currentlists)   # run teardown if exists 
    #os.system('chmod +x setup.py;./setup.py')      
    os.chdir('..')        



def execute(Paths,initialpath):
    """this function is used to traverse all folders and files under target path,and run specific scripts"""
    
    import os 
    for Path in Paths:         # traverse each Path in Paths
        os.chdir(initialpath)  # switch to initialpath ,initialze
        traverse(Path)         # execute testcases under Path


def create_log_folders():
    """this function will fetch mx version and create log and summary folders based on mx_version"""
    import remote_operations
    import global_variables
    #import basic_class
    import time
    import os
    
    mx1_host1_ip = global_variables.get_value('mx1_host1_ip')
    root_account = global_variables.get_value('root_account') # root by default
    root_passwd = global_variables.get_value('root_passwd')   # 
    sshport = global_variables.get_value('sshport')
    
    #owm_common_version = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'rpm -qa|grep owm|grep owm-common',1,'owm-common-',1)
    import paramiko
    ssh0 = paramiko.SSHClient()
    ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh0.connect(hostname = mx1_host1_ip, port = sshport, username = root_account, password = root_passwd)
    cmds = 'rpm -qa|grep owm|grep owm-common' 
    stdin, stdout, stderr = ssh0.exec_command(cmds)
    okout = stdout.read()
    errout = stderr.read()    
    ssh0.close()
    if len(errout) == 0:  
        out=str(okout,'utf-8')
    else:
        out=str(errout,'utf-8')
        print("Some error seems happened:\n"+out)
        exit(1)
    
    owm_version = out.split('owm-common-')[1].strip()
    print('owm_version='+owm_version)
    
    initialpath = global_variables.get_value('initialpath')
    currenttime = time.strftime("%Y\%m\%d-%H:%M")
    foldername = owm_version+'-'+'{}'.format(currenttime)
    if os.path.exists('logs/'+foldername):
        try:
            os.remove('logs/'+foldername+'/alltestcases.log')
        except FileNotFoundError:
            pass
    else:
        os.makedirs('logs/'+foldername)
    if os.path.exists('summary/'+foldername):
        try:
            os.remove('summary/'+foldername+'/summary.log')
        except FileNotFoundError:
            pass
    else:
        os.makedirs('summary/'+foldername)
    
    global_variables.set_value('logpath',initialpath+'/logs/'+foldername)
    global_variables.set_value('summarypath',initialpath+'/summary/'+foldername)
    
    
    
    


    