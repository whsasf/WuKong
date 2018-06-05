# -*- coding: utf-8 -*- 
# this module contains some functions that will used commenly


def welcome():
    """the welcome function used to print some welcome header when using this WuKong test suits
       also print headers in summary.log
    """
    
    import basic_class
    import global_variables
    
    basic_class.mylogger_recordnf.title('='*68)
    basic_class.mylogger_recordnf.title('='+"{:^66}".format('WuKong Test Suit')+'=')
    basic_class.mylogger_recordnf.title('='*68)
    
    summary_print_length = 100
    global_variables.set_value('summary_print_length',summary_print_length)
    
    owm_version = global_variables.get_value('owm_version')
    summary_title = ' MX TestCases Summary for '+owm_version+' '
    
    if len(summary_title) % 2 == 0:    #make sure summary_title has even length
        pass
    else:
        summary_title += ' '
    
    dummy_length1 = int((summary_print_length - len(summary_title)) /2)
    basic_class.mylogger_summary.yes('='*dummy_length1+summary_title+'='*dummy_length1+'\n')
    
    # below 3 variables will be used in summaryfunction and statistics function later to generate a summary
    total_testcases_num = 0
    passed_testcases_num = 0
    failed_testcases_num = 0
    
    global_variables.set_value('total_testcases_num',total_testcases_num)
    global_variables.set_value('passed_testcases_num',passed_testcases_num)
    global_variables.set_value('failed_testcases_num',failed_testcases_num)
    
    
def print_mx_version():
    """print mx_version get from basic_function.create_log_folders()"""
    
    import global_variables
    import basic_class
    
    owm_version = global_variables.get_value('owm_version') 
    basic_class.mylogger_record.info('owm_version = '+owm_version)
    
    
    
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
    import basic_class
    
    argvlist = global_variables.get_value('argvlist')           # get argvlist of arguments
    if argvlist.count('-v') > 1 or argvlist.count('-vv') > 1:   # determine the chloglevel (displayed to screen)
        basic_class.mylogger_record.error("multiple '-v' or '-vv' detected,please make sure only one entered!")
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

            
def parse_testcaselocation(testcaselocation):
    """this function will chelk if the testcaselocation is:
    
       (1)the default testcase location:TestCases folder
       (2)some (any) individual folders of some testcases
       (3)a file ,that contains the location of testcases"""       
    import os
    import basic_class
    
    # print(testcaselocation)   
    # print(len(testcaselocation))
    if len(testcaselocation) == 0 or  len(testcaselocation) == 1:
        if testcaselocation == [] or (testcaselocation[0] == 'test_cases' and testcaselocation[-1] == 'test_cases'):
            basic_class.mylogger_record.info('The testcase located in:'+str(['test_cases']))
            return (['test_cases'])
        elif os.path.isfile(testcaselocation[0]):
            with open(testcaselocation[0]) as file_obj:
                lines = file_obj.read().splitlines()
            basic_class.mylogger_record.info('The testcase located in:') 
            for line in lines:
                basic_class.mylogger_recordnf.title(line.strip())
            return lines
        else:
            basic_class.mylogger_record.info('The testcase located in:') 
            basic_class.mylogger_recordnf.title(testcaselocation[0])  
            testcaselocation
            return testcaselocation
    else:
        basic_class.mylogger_record.info('The testcase located in:') 
        for testcase in testcaselocation:
            basic_class.mylogger_recordnf.title(testcase)  
        return testcaselocation
        


def traverse_judge(casename,currentlists):
    """decide import or reload testcase file"""
    
    import os
    import sys
    import global_variables
    import time
    import basic_class
    
    num = global_variables.get_value('num') 
    oldcasename = casename+'.py'
    
    if  oldcasename in currentlists:
    	  
    	  # print part test case names :setup or run or teardown 
        if 'setup' in casename.lower():
            basic_class.mylogger_recordnf.title('[-->Executing setup.py ...]') 
        elif 'run' in casename.lower():
            basic_class.mylogger_recordnf.title('[-->Executing run.py ...]')     
        elif 'teardown' in casename.lower():
            basic_class.mylogger_recordnf.title('[-->Executing teardown.py ...]')    
        else:
            basic_class.mylogger_record.warning('Please make sure testcases names are among:setup,run,teardowm!')
            exit (1)

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
    import basic_class
    import global_variables 
    
    os.chdir(Path)                 # switch to current Path
    
    currentlists = os.listdir('.') # get current folder and file names in current path
    for list in currentlists:      # delete the hiden files and folders
        if list.startswith('.'):
            currentlists.remove(list)
    for list in currentlists:      # delete the '__pycache__/' folderss
        if '__pycache__' in list:
            currentlists.remove(list)
    
    # print test case title if this is a final testcase folder ,means no sub folders
    bottom_flag = [os.path.isfile(list) for list in currentlists]
    if bottom_flag.count(True) == len(bottom_flag):    # has no sub folders,is a testcase folder 
        testcase_name = os.getcwd().split('/')[-1]
        #basic_class.mylogger_recordnf.title('\n'+'-'*(17+len(testcase_name)))
        basic_class.mylogger_recordnf.title('\n---Testcase: '+testcase_name+' ---')
        #basic_class.mylogger_recordnf.title('-'*(17+len(testcase_name)))
        global_variables.set_value('testcase_name',testcase_name)
    else: 
        folder_name = os.getcwd().split('/')[-1]                                             # has sub folders ,is a test suits folder
        #basic_class.mylogger_recordnf.title('\n'+'='*(17+len(folder_name)))
        basic_class.mylogger_recordnf.title('\n===Testsuit: '+folder_name+' ===') 
        #basic_class.mylogger_recordnf.title('='*(17+len(folder_name))) 
            
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
    import basic_class
    
    # print title to indicate begin running all testcases
    basic_class.mylogger_recordnf.title('###################################################################')
    basic_class.mylogger_recordnf.title('+               Executing all testcases as required               +')
    basic_class.mylogger_recordnf.title('###################################################################')
    
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
    global_variables.set_value('owm_version',owm_version)
    #print("Some error seems happened:\n"+out)
    initialpath = global_variables.get_value('initialpath')
    currenttime = time.strftime("%Y-%m-%d-%H-%M")
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
    


def summary(result_lists,tc_name = ''):
    """this function will analyze the test outcome,determin if tests successfully or not,and record results to summary.log"""
    
    import basic_class
    import global_variables
    
    total_testcases_num = global_variables.get_value('total_testcases_num')
    passed_testcases_num = global_variables.get_value('passed_testcases_num')
    failed_testcases_num = global_variables.get_value('failed_testcases_num')
    
    success_flag = 0                   # use to accumulate the 'success' number,from 0
    target = len(result_lists)         # for result_lists=['threshold success', 'count success'] ,target wil be 2 (success)
                                       # if  result_lists=['threshold success', 'count faile'],target still be 2, but will failed
    if tc_name != '':                  # will use customer input testcase name to print 
        testcase_name = tc_name
    else:                              # will use default testcase name got from 'os.getcwd().split('/')[-1]'
        testcase_name = global_variables.get_value('testcase_name')           	
    
    summary_print_length = int(global_variables.get_value('summary_print_length'))
    for result in result_lists:
        if 'success' in result.lower():
            success_flag += 1
    
    dummy_length2 = int(summary_print_length - len(testcase_name) -7)
    if success_flag == target:
        basic_class.mylogger_record.yes('All test steps passed.') 
        basic_class.mylogger_summary.yes(testcase_name+' '+'.'*dummy_length2+' [PASS]') 
        passed_testcases_num += 1
        global_variables.set_value('passed_testcases_num',passed_testcases_num)   # update passed_testcases_num
    else:
        basic_class.mylogger_record.no('Not all test steps passed.') 
        basic_class.mylogger_summary.no(testcase_name+' '+'.'*dummy_length2+' [FAIL]') 
        failed_testcases_num += 1
        global_variables.set_value('failed_testcases_num',failed_testcases_num)   # update total_testcases_num
        
    total_testcases_num += 1
    global_variables.set_value('total_testcases_num',total_testcases_num)         # update total_testcases_num



def statistics():
    """thid function used to statistic total tetscases numbers ,and passed numbers ,and failed numbers"""
    
    import basic_class
    import global_variables

    total_testcases_num = global_variables.get_value('total_testcases_num')
    passed_testcases_num = global_variables.get_value('passed_testcases_num')
    failed_testcases_num = global_variables.get_value('failed_testcases_num')
        
    basic_class.mylogger_summary.yes('Total number of Test Cases: '+str(total_testcases_num))
    basic_class.mylogger_summary.yes('PASS:                       '+str(passed_testcases_num))
    basic_class.mylogger_summary.yes('FAIL:                       '+str(failed_testcases_num))
    
    
     
            	