#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

##steps:
# (1) set keys:
#               /*/common/messageBodyEncryptionEnabled:[false]
#               /*/mss/compressionEnabled: [false]   # need mss restart
# (2) create 6 accounts:testuser1@openwave.com -test6@openwave.com
# (3) clear current popserv.stat file

import basic_function
import basic_class
import imap_operations
import smtp_operations
import global_variables
import remote_operations
import time

basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')

mx1_mss2_host_ip,mx1_mss1_host_ip,mx1_pop1_host,mx1_pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('mx1_mss2_host_ip','mx1_mss1_host_ip','mx1_pop1_host','mx1_pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')

basic_class.mylogger_record.info('step1:set keys and restart services')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/messageBodyEncryptionEnabled=false\";imconfcontrol -install -key \"/*/mss/compressionEnabled\=false\"''.format(mx_account),0)
remote_operations.remote_operation(mx1_mss1_host_ip,root_account,root_passwd,'su - {0} -c \'~/lib/imservctrl killStart mss\''.format(mx_account),0)
remote_operations.remote_operation(mx1_mss2_host_ip,root_account,root_passwd,'su - {0} -c \'~/lib/imservctrl killStart mss\''.format(mx_account),0)


basic_class.mylogger_record.info('step2:create 6 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=6;i++));do account-create {1}$i@{2}   {1}$i default;done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Created Successfully',6)



