#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) imap login 125 accounts with correct credentials, the other 125 use wrong credentials
# (2) check and analyze imapserv.stat file .make sure the total attempts are 250 ,and half passed ,half failed

import basic_function
import basic_class
import imap_operations
import global_variables

#step 1
basic_class.mylogger.info('step1:imap login:125 account with correct passwd, the other 125 use wrong pssswd')

imap1_host,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


for i in range(1,126): 
    imap_inst_name = 'mximap'+str(i)
    imap_inst_name = imap_operations.IMAP_Ops('imap1_host,imap1_port)
    imap_inst_name.imap_login(test_account_base+str(i),test_account_base+str(i)) # using correct passwd
    imap_inst_name.imap_logout()

for i in range(126,251): 
    imap_inst_name = 'mximap'+str(i)
    imap_inst_name = imap_operations.IMAP_Ops('imap1_host,imap1_port)
    imap_inst_name.imap_login(test_account_base+str(i),'password') # using wrong passwd :password here
    imap_inst_name.imap_logout()
    
#step 2
basic_class.mylogger.info('step2:check and analyze imapserv.stat file')

