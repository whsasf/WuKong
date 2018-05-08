#!/usr/bin/env python3
# -*- coding: utf-8 -*-      

""" 
This Python file is the main Python run script
Created on 2018/04/16
"""

def setpath():   
    """setpath function add lib folder to sys.path for modules search"""
    import os
    import sys
    cpath = os.getcwd()  #get current path
    #print ('Current path is: ',cpath)
    sys.path.append(cpath+'/lib') # append lib folder to sys.path
    #print (sys.path)
    
setpath() #all the other modules import should after this function call,otherwise can not find correct customized lib location

import basic_function
import basic_class
import imap_operations
import os

basic_function.welcome() #print welcome headers

def main():
    """main function to active logging,testcase running"""
    
    testcaselocation,chloglevel = basic_function.parse_args()  # parse the paramaters to find the chloglevel and testcaselocation
    print ("the testcase location paramaters are:\n",testcaselocation)
    print ("the chloglevel paramater is:\n",chloglevel) 

    tclocation = basic_function.parse_testcaselocation(testcaselocation) # format testcase location in a list for given formats
    print("The testcase located in:\n",tclocation)   
    #print (tclocation)
     
    initialpath = os.getcwd() #get initial path,will back here after each traverse
    print('initial path is:',initialpath)
    basic_function.execute(tclocation,initialpath) #executing testcases 
    
    #mylogger=basic_class.Loggger('WuKong',chloglevel)
    #mylogger.debug('debug')
    #mylogger.info('info')
    #mylogger.warning('warning')
    #mylogger.error('error')
    #mylogger.critical('critical')
    
  
    #import need modules
 
    #traverse
    
    #for i in range(1,2):
    #myimap = imap_operations.IMAP_Ops('10.49.58.239',20143)
    #myimap.imap_login('xx1','p')
    
    #myimap.imap_logout()

    
    #myssh = Remote_Ops('10.49.58.239','root','letmein')
    #myssh.remote_operations('ls -al',1,'.',61)
    
    #mytraverse = Directory()
    #mytraverse.traverse('Test_Cases')
    #pprint (sys.path)
    
    

    
    
if __name__ == '__main__':
    main()