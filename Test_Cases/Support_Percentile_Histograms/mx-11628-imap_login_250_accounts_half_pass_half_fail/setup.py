#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) set keys:
#               /*/common/perfStatThresholds:[StatImapAuthCommand 200]
#               /*/common/reportParamsInterval: [120]
# (2) create 250 accounts:testuser1@openwave.com -test250@openwave.com
# (3) clear current imapserv.stat file

import basic_function
import basic_class
import imap_operations
import global_variables
import remote_operations

#print (global_variables.get_value('initialpath'))

basic_class.mylogger.info('-->Runing setup testcase:mx-11628-imap_login_250_accounts_half_pass_half_fail--->')
basic_class.mylogger.info('Preparing... get some variables needed for tests')

imap1_host = global_variables.get_value('imap1_host')
imap1_port = global_variables.get_value('imap1_port')
mx_account = global_variables.get_value('mx_account')     # imail by default
mx1_host1 = global_variables.get_value('mx1_host1')
root_account = global_variables.get_value('root_account') # root by default
root_passwd = global_variables.get_value('root_passwd')   # 
test_account_base = global_variables.get_value('test_account_base')
default_domain = global_variables.get_value('default_domain')

basic_class.mylogger.debug('	imap1_host='+imap1_host)
basic_class.mylogger.debug('	imap1_port='+imap1_port)
basic_class.mylogger.debug('	mx_account='+mx_account)
basic_class.mylogger.debug('	mx1_host1='+mx1_host1)
basic_class.mylogger.debug('	root_account='+root_account)
basic_class.mylogger.debug('	root_passwd='+root_passwd)
basic_class.mylogger.debug('	test_account_base='+test_account_base)
basic_class.mylogger.debug('	default_domain='+default_domain)

#myssh = Remote_Ops('10.49.58.239','root','letmein')

#basic_class.mylogger.info('step1:set keys')
#remote_operations.remote_operation('su - mx_account -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=StatImapAuthCommand 200\";imconfcontrol -install -key \"/*/common/reportParamsInterval= 120\"\'',mx1_host1,root_account,root_passwd,0)

#basic_class.mylogger.info('step2:create 250 accounts')
#remote_operations.remote_operation('su - mx_account -c \'for ((i=1;i<=250;i++));do account-create test_account_base\$i@default_domain   test_account_base\$i default;done\'',mx1_host1,root_account,root_passwd,1,'Mailbox Deleted Successfully',250)

#basic_class.mylogger.info('step3: clear current imapserv.stat file')
#remote_operation('su - mx_account -c "> log/imapserv.stat"',mx1_host1,root_account,root_passwd,0)




