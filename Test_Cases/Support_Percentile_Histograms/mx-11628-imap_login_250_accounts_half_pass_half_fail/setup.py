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
basic_class.mylogger.debug('Preparing... get some variables needed for tests')

imap1_host,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')

basic_class.mylogger.debug(' imap1_host='+imap1_host)
basic_class.mylogger.debug(' imap1_port='+imap1_port)
basic_class.mylogger.debug(' mx_account='+mx_account)
basic_class.mylogger.debug(' mx1_host1_ip='+mx1_host1_ip)
basic_class.mylogger.debug(' root_account='+root_account)
basic_class.mylogger.debug(' root_passwd='+root_passwd)
basic_class.mylogger.debug(' test_account_base='+test_account_base)
basic_class.mylogger.debug(' default_domain='+default_domain)

basic_class.mylogger.info('step1:set keys')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=StatImapAuthCommand 200\";imconfcontrol -install -key \"/*/common/reportParamsInterval=120\"\''.format(mx_account),0)

basic_class.mylogger.info('step2:create 250 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=2;i++));do account-create {1}$i@{2}   {1}$i default;done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Created Successfully',2)

basic_class.mylogger.info('step3: clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)




