#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

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
    sys.path.append(initialpath+'/lib/testcase_specified')    # append lib/perl  folder to sys.path
    sys.path.append(initialpath)   # 
    #print(sys.path)
    return initialpath