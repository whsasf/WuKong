#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) delete accounts :testuser1@openwave.com - testuser250@openwave.com
# (2) restore the config keys:
#               /*/common/perfStatThresholds:[]
#               /*/common/reportParamsInterval: []

import basic_function
import basic_class
import imap_operations
import global_variables
import remote_operations


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

basic_class.mylogger.info('step1:delete 250 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=2;i++));do account-delete {1}$i@{2};done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Deleted Successfully',2)

basic_class.mylogger.info('step2:restore config keys')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=\";imconfcontrol -install -key \"/*/common/reportParamsInterval=60\"\''.format(mx_account),0)
