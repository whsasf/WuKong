#!/usr/bin/env python3
# -*- coding: utf-8 -*-      

 # green logging.error('\033[1;32msdfsdf\033[0m')    pass/
 # red   logging.error('\033[1;31msdfsdf\033[0m')    failed/warning/error/criticle
 # blue  logging.error('\033[1;34msdfsdf\033[0m')   title
 
""" This Python file is the main Python run script.Created on 2018/05/16"""

initialpath = ''
import setlibpath
initialpath = setlibpath.setlibpath() #all the other modules import should after this function call,otherwise can not find correct customized lib location  
#print(initialpath)

import global_variables
global_variables._init()
global_variables.set_value('initialpath',initialpath)
global_variables.set_value('num',1)
global_variables.import_variables_from_file([initialpath+'/etc/global.vars',initialpath+'/etc/user.vars'])# read all pre-defined vars

from basic_function import create_log_folders
create_log_folders()




import sys
import basic_class
import basic_function

#global_variables.get_dict()
basic_function.print_mx_version()  

from basic_function import welcome           
welcome()             #print welcome headers 


def main():
    """main function to active logging,testcase running"""    
    
    import global_variables
            
    testcaselocation = global_variables.get_value('argvlist')
    chloglevel = global_variables.get_value('chloglevel')   
    tclocation = basic_function.parse_testcaselocation(testcaselocation) # format testcase location in a list for given formats
    
    
    #initialpath = os.getcwd() #get initial path,will back here after each traverse
    basic_class.mylogger_record.debug('The initial path is:'+initialpath)
    global_variables.set_value('initialpath',initialpath)
    #print('testcaselocation=',testcaselocation)
    basic_function.execute(tclocation,initialpath) #executing testcases 
    
    basic_function.statistics()
    #basic_class.mylogger_record.info('11111111111111')   
    #basic_class.mylogger_recordnf.info('11111111111111')
    #basic_class.mylogger_summary.yes('yesyesyesyesyes')  
    #basic_class.mylogger_summary.no('nonononono')
    #basic_class.mylogger_recordnf.title('hihihiih')
     #pprint.pprint(sys.modules)
     #mylogger=basic_class.Loggger('WuKong',chloglevel)
#    basic_class.mylogger_record.debug('debug')
#    basic_class.mylogger_record.info('info')
#    basic_class.mylogger_record.warning('warning')
#    basic_class.mylogger_record.error('error')
#    basic_class.mylogger_record.critical('critical')
    
  
    #import need modules
 
    #traverse
    
    #for i in range(1,3):
    #import imap_operations
    #myimap = imap_operations.IMAP_Ops('10.49.58.239',20143)
    #myimap.imap_login('xx2','p')
    #a = myimap.imap_select()
    #print(a)
    #print(type(a))
    #if int(a) == 2:
    #    print('hi')
    #myimap.imap_fetch('1:2','uid')
    #myimap.imap_append(message=b"From:tom\nTo:lucy\nSubject:haha\n\nffffffffffffffffffff",mailbox='INBOX')
    #myimap.imap_append(message=b"From:tom\nTo:lucy\nSubject:haha\n\nffffffffffffffffffff",mailbox='INBOX')
    #myimap.imap_select()
    #myimap.imap_create('haha2')
    #myimap.imap_create('haha2/haha3')
    #myimap.imap_create('haha2/haha3/haha4')
    ##myimap.imap_list(pattern='%')
    ##myimap.imap_list(directory='haha2')
    ##myimap.imap_select('Trash')
    #myimap.imap_copy('1,2','haha2')
    ##myimap.imap_copy('1,2','INBOX')
    ##myimap.imap_select()
    #myimap.imap_move('1,2','haha2/haha3/haha4')
    #myimap.imap_select()
    #myimap.imap_select('haha2/haha3/haha4')
    #myimap.imap_logout()
    
    
    #    try:
    #        myimap.imap_authenticate('xx1','pp')
    #    except:
    #        print('some error happened, butwill pass')
    #        pass
        #myimap.imap_login('xx1','pp')
    
        #myimap.imap_fetch('1:6','rfc822')
    #    myimap.imap_logout()
    
    #myimap.imap_logout()
    #import remote_operations
    #myssh = remote_operations.Remote_Ops('10.49.58.239','root','letmein')
    #myssh.remote_operations('ls -al;cal',1,'.',61)
    #myssh.remote_operations('cal',1,'.',32)
    
    #mx1_pop1_host_ip = global_variables.get_value('mx1_pop1_host_ip')
    #mx1_pop1_port = global_variables.get_value('mx1_pop1_port')
    #pop1_sslport = global_variables.get_value('pop1_sslport')
    #
    #import pop_operations
    #from  pop_operations import POP_Ops , POPSSL_Ops
    
   #pop3 = POP_Ops(mx1_pop1_host_ip,mx1_pop1_port)
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
    
    
    #pop3ssl = POPSSL_Ops(mx1_pop1_host_ip,pop1_sslport)
    ##pop3.pop_stls()
    #pop3ssl.pop_set_debuglevel()
    #pop3.pop_user('xx1')
    #pop3.pop_pass('p')
    #pop3.pop_login('xx1','p')
    #pop3ssl.pop_apop('xx1','p')
    #pop3ssl.pop_auth_plain('xx1','p')
    #pop3ssl.pop_stat()
    #pop3ssl.pop_capa()
    #pop3ssl.pop_list()
    #pop3ssl.pop_retr(2)
    #pop3ssl.pop_dele(1)  
    #pop3ssl.pop_rset() 
    #pop3ssl.pop_list()
    #pop3ssl.pop_list(1)
    #pop3ssl.pop_noop()  
    #pop3ssl.pop_uidl(1) 
    #pop3ssl.pop_uidl()  
    #pop3ssl.pop_top(2,2)
    #pop3ssl.pop_quit()
    
if __name__ == '__main__':
    main()