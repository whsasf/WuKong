#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) imap login 10 accounts with correct credentials, the other 10 use wrong credentials
# (2) check and analyze imapserv.stat file .make sure the total attempts are 20 ,and half passed ,half failed

import basic_function
import basic_class
import pop_operations
import global_variables
import time
import remote_operations
import stat_statistics


#step 1
basic_class.mylogger_record.info('step1:imap login:10 account with correct passwd, the other 10 use wrong pssswd')

pop1_host_ip,pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('pop1_host_ip','pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


for i in range(1,11): 
    mxpop1 = pop_operations.POP_Ops(pop1_host_ip,pop1_port)
    try:
        mxpop1.pop_apop(test_account_base+str(i),test_account_base+str(i)) # using correct passwd
        basic_class.mylogger_record.info('apop auth success')
    except:
        basic_class.mylogger_record.error('apop auth fail')
    mxpop1.pop_stat()
    mxpop1.pop_quit()

for i in range(11,21): 
    mxpop2 = pop_operations.POP_Ops(pop1_host_ip,pop1_port)
    try:
        mxpop2.pop_apop(test_account_base+str(i),'password') # using wrong passwd :password here
    except:
        basic_class.mylogger_record.error('apop auth fail')
    mxpop2.pop_quit()
    
#step 2
basic_class.mylogger_record.info('fetching popserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('step2:check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/popserv.stat|grep StatPopPassCommand"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatPopPassCommand',20)

basic_function.summary(result_lists)