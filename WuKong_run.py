#!/usr/bin/env python3
# -*- coding: utf-8 -*-      


""" 
This Python file is the main Python run script
Created on 2018/05/16
"""

initialpath = ''
def setlibpath():   
    """setlibpath function add lib folder to sys.path for modules search"""
    
    import os
    import sys
    global initialpath
    initialpath = os.getcwd()  #get initial path
    #print ('Current path is: ',cpath)
    sys.path.append(initialpath+'/lib/python')                # append lib/pthon folder to sys.path
    sys.path.append(initialpath+'/lib/shell')                 # append lib/shell folder to sys.path
    sys.path.append(initialpath+'/lib/perl')                  # append lib/perl  folder to sys.path
    sys.path.append(initialpath+'/lib/testcase_specified')   # append lib/perl  folder to sys.path
    sys.path.append(initialpath)   # 
    #print (sys.path)    
setlibpath() #all the other modules import should after this function call,otherwise can not find correct customized lib location

import global_variables
global_variables._init()
global_variables.set_value('initialpath',initialpath)
global_variables.set_value('num',1)
global_variables.import_variables_from_file([initialpath+'/etc/global.vars',initialpath+'/etc/user.vars'])# read all pre-defined vars

from basic_function import create_log_folders
create_log_folders()

from basic_function import welcome
welcome() #print welcome headers



#import imap_operations

import os
currentpath = os.getcwd()

import sys
import pprint
import basic_class
import basic_function


#global_variables.get_dict()

def main():
    """main function to active logging,testcase running"""    
    
    import global_variables

        
    testcaselocation = global_variables.get_value('argvlist')
    chloglevel = global_variables.get_value('chloglevel')   
    tclocation = basic_function.parse_testcaselocation(testcaselocation) # format testcase location in a list for given formats
    
    
    #initialpath = os.getcwd() #get initial path,will back here after each traverse
    print('==> The initial path is:',initialpath),print()
    global_variables.set_value('initialpath',initialpath)
    #print('testcaselocation=',testcaselocation)
    basic_function.execute(tclocation,initialpath) #executing testcases 
    
     #pprint.pprint(sys.modules)
     #mylogger=basic_class.Loggger('WuKong',chloglevel)
#    basic_class.mylogger.debug('debug')
#    basic_class.mylogger.info('info')
#    basic_class.mylogger.warning('warning')
#    basic_class.mylogger.error('error')
#    basic_class.mylogger.critical('critical')
    
  
    #import need modules
 
    #traverse
    
    #for i in range(1,3):
    #    myimap = imap_operations.IMAP_Ops('10.49.58.239',20143)
        #myimap.imap_login('xx1','pp')
    #    try:
    #        myimap.imap_authenticate('xx1','pp')
    #    except:
    #        print('some error happened, butwill pass')
    #        pass
        #myimap.imap_login('xx1','pp')
        #myimap.imap_select()
        #myimap.imap_fetch('1:6','rfc822')
    #    myimap.imap_logout()
    
    #myimap.imap_logout()
    #import remote_operations
    #myssh = remote_operations.Remote_Ops('10.49.58.239','root','letmein')
    #myssh.remote_operations('ls -al;cal',1,'.',61)
    #myssh.remote_operations('cal',1,'.',32)
    
    
    
if __name__ == '__main__':
    main()