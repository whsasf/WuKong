#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) delete alias account for each account
# (2) delete accounts :testuser1@openwave.com - testuser20@openwave.com
# (3) restore the config keys:
#               /*/common/perfStatThresholds:[]
#               /*/common/reportParamsInterval: [60 ]      # default 60
#               /*/common/badPasswordDelay: [1]            # nodelay ,default 1
#               /*/common/maxBadPasswordDelay: [90]        # no delay,default 90 
#               /*/common/loginAliases: [false]            # false by default
#               /*/imapserv/allowCRAMMD5: [false]          # disable cram-md5 by default
#               /*/mxos/defaultPasswordStoreType: [sha512] # default is sha512

import basic_function
import basic_class
import imap_operations
import global_variables
import remote_operations

imap1_host,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')

basic_class.mylogger_record.info('step1:delete alias accounts for 20 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=20;i++));do imdbcontrol DeleteAlias u$i {2};done\''.format(mx_account,test_account_base,default_domain),0)

basic_class.mylogger_record.info('step2:delete 20 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=20;i++));do account-delete {1}$i@{2};done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Deleted Successfully',20)

basic_class.mylogger_record.info('step3:restore config keys')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=\";imconfcontrol -install -key \"/*/common/reportParamsInterval=60\";imconfcontrol -install -key \"/*/common/badPasswordDelay=1\";imconfcontrol -install -key \"/*/common/maxBadPasswordDelay=90\";imconfcontrol -install -key \"/*/common/loginAliases=false\";imconfcontrol -install -key \"/*/imapserv/allowCRAMMD5=false\";imconfcontrol -install -key \"/*/mxos/defaultPasswordStoreType=sha512\"\''.format(mx_account),0)

