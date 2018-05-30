#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) imap login 125 accounts with correct credentials, the other 125 use wrong credentials
# (2) check and analyze imapserv.stat file .make sure the total attempts are 250 ,and half passed ,half failed

import basic_function
import basic_class
import imap_operations
import global_variables
import time
import remote_operations
#import stat_statistics

#step 1
basic_class.mylogger.info('step1:imap login:125 account with correct passwd, the other 125 use wrong pssswd')

imap1_host_ip,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host_ip','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


for i in range(1,2): 
    mximap1 = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    mximap1.imap_login(test_account_base+str(i),test_account_base+str(i)) # using correct passwd
    mximap1.imap_logout()

for i in range(2,3): 
    mximap2 = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    try:
        mximap2.imap_login(test_account_base+str(i),'password') # using wrong passwd :password here
    except:
        print('login failed')
    mximap2.imap_logout()
    
#step 2
print('fetching imapserv.stat ...')
time.sleep (150)
basic_class.mylogger.info('step2:check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatImapAuthCommand"'.format(mx_account),0)
print(imapserv_stat_content)
print(type(imapserv_stat_content))
#stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatImapAuthCommand')

