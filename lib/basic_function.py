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
            # print('Using default testcase location:Test_Cases')            
            return (['Test_Cases'])
        elif os.path.isfile(testcaselocation[0]):
            with open(testcaselocation[0]) as file_obj:
                lines = file_obj.read().splitlines()
            # print('The testcase contains in files are:')
            # for line in lines:
                # print(line.strip())
            return lines
        else:
            # print('Using customized testcase location:',testcaselocation[0])
            return testcaselocation
    else:
        # print('The testcase locations are:')
        # for testcase in testcaselocation:
        #    print(testcase)
        return testcaselocation
        
        
        
        
                 
def traverse(Path):
    """traverse testcases under give Path,normal first execute setup,then run,last teardown for each testcase"""
    
    import os    
    os.chdir(Path)                 # switch to current Path
    currentlists = os.listdir('.') # get current folder and file names in current path
    for list in currentlists:      # delete the hiden files and folders
        if list.startswith('.'):
            currentlists.remove(list)
    #print(currentlists)
    if 'setup' in currentlists:            # run setup
        import setup
        ./setup
        #os.system('chmod +x setup;./setup')            
    if 'run' in currentlists:              # run run
        import run
        ./run
        #os.system('chmod +x run;./run')           
    for list in currentlists:
        if os.path.isdir(list):
            traverse(list)
            #os.chdir(list)
            #print (os.getcwd())        
    if 'teardown' in currentlists:         # run teardown 
        import teardown
        ./teardownteardown
        #os.system('chmod +x teardown;./teardown')
    os.chdir('..')        
        




def execute(Paths,initialpath):
    """this function is used to traverse all folders and files under target path,and run specific scripts"""
    
    import os 
    for Path in Paths:         # traverse each Path in Paths
        os.chdir(initialpath)  # switch to initialpath ,initialze
        traverse(Path)         # execute testcases under Path
        
