#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) imap login 10 accounts with correct credentials, the other 10 use wrong credentials
# (2) check and analyze imapserv.stat file .make sure the total attempts are 20 ,and half passed ,half failed

import basic_function
import basic_class
import imap_operations
import global_variables
import time
import remote_operations
import stat_statistics


#step 1
basic_class.mylogger_record.info('step1:imap auth_plain:10 account with correct passwd, the other 10 use wrong pssswd')

imap1_host_ip,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host_ip','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


for i in range(1,11): 
    mximap1 = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    try:
        mximap1.imap_authenticate(test_account_base+str(i),test_account_base+str(i)) # using correct passwd
        basic_class.mylogger_record.info('auth_plain success')
    except:
        basic_class.mylogger_record.error('auth_plain fail')
    mximap1.imap_select()
    mximap1.imap_logout()

for i in range(11,21): 
    mximap2 = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    try:
        mximap2.imap_authenticate(test_account_base+str(i),'password') # using wrong passwd :password here
    except:
        basic_class.mylogger_record.error('auth_plain fail')
    mximap2.imap_logout()
    
#step 2
basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('step2:check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatImapAuthCommand"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatImapAuthCommand',20)

