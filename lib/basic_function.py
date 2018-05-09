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
    argvnum = len(sys.argv) # number of total argements,the real arguements number is 
    argvlist = sys.argv[1:] # total real arguments(shell name excludded)
    # print(argvnum)
    # print(argvlist)
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
    print ("==> The testcase location paramaters are:\n",'    '+str(argvlist)), print()
    print ("==> The chloglevel paramater is:\n",'    '+chloglevel), print()
    return argvlist,chloglevel
    
        
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
    from imp import reload         # reload setup.py ,run.py ,teardown.py  in each traverse
    import global_variables
    import pprint
    
    num = global_variables.get_value('num')
    tmp = global_variables.get_value('tmp')
    realcasename = casename+'.py'
    if  realcasename in currentlists:  # run setup
        casepath = os.getcwd()
        #print(casepath)
        sys.path.append(casepath)
        #print(casepath)
        #print(casename)
        __import__ (casename)
        del sys.modules[casename]
        
            
    	
                           
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
    #print(currentlists)
    
    traverse_judge('setup',currentlists)      # run setup
    traverse_judge('run',currentlists)        # run run                    
    for list in currentlists:
        if os.path.isdir(list):
            traverse(list)
            #os.chdir(list)
            #print (os.getcwd())        
    traverse_judge('teardown',currentlists)   # run teardown 
    #os.system('chmod +x setup.py;./setup.py')      
    os.chdir('..')        
        

def execute(Paths,initialpath):
    """this function is used to traverse all folders and files under target path,and run specific scripts"""
    
    import os 
    for Path in Paths:         # traverse each Path in Paths
        os.chdir(initialpath)  # switch to initialpath ,initialze
        traverse(Path)         # execute testcases under Path
