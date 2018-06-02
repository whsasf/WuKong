#!/usr/bin/env python3
# -*- coding: utf-8 -*-      

 # green logging.error('\033[1;32msdfsdf\033[0m')    pass/
 # red   logging.error('\033[1;31msdfsdf\033[0m')    failed/warning/error/criticle
 # blue   logging.error('\033[1;34msdfsdf\033[0m')   title
 
""" This Python file is the main Python run script.Created on 2018/05/16"""

initialpath = ''
import setlibpath
initialpath = setlibpath.setlibpath() #all the other modules import should after this function call,otherwise can not find correct customized lib location

import global_variables
global_variables._init()
global_variables.set_value('initialpath',initialpath)
global_variables.set_value('num',1)
global_variables.import_variables_from_file([initialpath+'/etc/global.vars',initialpath+'/etc/user.vars'])# read all pre-defined vars

from basic_function import create_log_folders
create_log_folders()

from basic_function import welcome
welcome()             #print welcome headers

import sys
import basic_class
import basic_function

#global_variables.get_dict()
basic_function.print_mx_version()
def main():
    """main function to active logging,testcase running"""    
    
    import global_variables
            
    testcaselocation = global_variables.get_value('argvlist')
    chloglevel = global_variables.get_value('chloglevel')   
    tclocation = basic_function.parse_testcaselocation(testcaselocation) # format testcase location in a list for given formats
    
    
    #initialpath = os.getcwd() #get initial path,will back here after each traverse
    basic_class.mylogger.info('The initial path is:'+initialpath)
    global_variables.set_value('initialpath',initialpath)
    #print('testcaselocation=',testcaselocation)
    #basic_function.execute(tclocation,initialpath) #executing testcases 
    
    basic_class.mylogger.info('11111111111111')
    basic_class.mylogger_summary.summary('zfxfdsfdsf')
    basic_class.mylogger_title.title('hihihiih')
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
    pop1_host_ip = global_variables.get_value('pop1_host_ip')
    pop1_port = global_variables.get_value('pop1_port')
    pop1_sslport = global_variables.get_value('pop1_sslport')
    
    import pop_operations
    from  pop_operations import POP_Ops , POPSSL_Ops
    
   #pop3 = POP_Ops(pop1_host_ip,pop1_port)
   ##pop3.pop_stls()
   #pop3.pop_set_debuglevel()
   ##pop3.pop_user('xx1')
   ##pop3.pop_pass('p')
   ##pop3.pop_login('xx1','p')
   ##pop3.pop_apop('xx1','p')
   #pop3.pop_auth_plain('xx1','p')
   #pop3.pop_stat()
   #pop3.pop_capa()
   #pop3.pop_list()
   #pop3.pop_retr(2)
   #pop3.pop_dele(1)  
   #pop3.pop_rset() 
   #pop3.pop_list()
   #pop3.pop_list(1)
   #pop3.pop_noop()  
   #pop3.pop_uidl(1) 
   #pop3.pop_uidl()  
   #pop3.pop_top(2,2)
   #pop3.pop_quit()
    
    
    pop3ssl = POPSSL_Ops(pop1_host_ip,pop1_sslport)
    #pop3.pop_stls()
    pop3ssl.pop_set_debuglevel()
    #pop3.pop_user('xx1')
    #pop3.pop_pass('p')
    #pop3.pop_login('xx1','p')
    #pop3ssl.pop_apop('xx1','p')
    pop3ssl.pop_auth_plain('xx1','p')
    pop3ssl.pop_stat()
    pop3ssl.pop_capa()
    pop3ssl.pop_list()
    pop3ssl.pop_retr(2)
    pop3ssl.pop_dele(1)  
    pop3ssl.pop_rset() 
    pop3ssl.pop_list()
    pop3ssl.pop_list(1)
    pop3ssl.pop_noop()  
    pop3ssl.pop_uidl(1) 
    pop3ssl.pop_uidl()  
    pop3ssl.pop_top(2,2)
    pop3ssl.pop_quit()
    
if __name__ == '__main__':
    main()