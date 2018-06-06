#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) delete each alias for 10 accounts
# (2) delete accounts :testuser1@openwave.com - testuser10@openwave.com
# (3) restore the config keys:
#               /*/common/perfStatThresholds:[]
#               /*/common/reportParamsInterval: [60]        # default 60
#               /*/common/badPasswordDelay: [1]             # nodelay ,default 1
#               /*/common/maxBadPasswordDelay: [90]         # no delay,default 90 
#               /*/common/loginAliases: [false]             # false by default
#               /*/popserv/allowAPOP: [false]               # disable apop ,default false
#               /*/mxos/defaultPasswordStoreType: [sha512]  # default is sha512, must use clear for apop 
#               /*/mxos/trustedClient: [false]              # to avoid use full account name(with domain) in apop auth,default is false

import basic_function
import basic_class
import imap_operations
import global_variables
import remote_operations

pop1_host,pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('pop1_host','pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')

basic_class.mylogger_record.info('step1:delete alias accounts for 10 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=10;i++));do imdbcontrol DeleteAlias u$i {2};done\''.format(mx_account,test_account_base,default_domain),0)

basic_class.mylogger_record.info('step2:delete 10 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=10;i++));do account-delete {1}$i@{2};done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Deleted Successfully',10)

basic_class.mylogger_record.info('step3:restore config keys')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=\";imconfcontrol -install -key \"/*/common/reportParamsInterval=60\";imconfcontrol -install -key \"/*/common/badPasswordDelay=1\";imconfcontrol -install -key \"/*/common/maxBadPasswordDelay=90\";imconfcontrol -install -key \"/*/common/loginAliases=false\";imconfcontrol -install -key \"/*/popserv/allowAPOP=false\";imconfcontrol -install -key \"/*/mxos/defaultPasswordStoreType=sha512\";imconfcontrol -install -key \"/*/mxos/trustedClient=false\"\''.format(mx_account),0)

