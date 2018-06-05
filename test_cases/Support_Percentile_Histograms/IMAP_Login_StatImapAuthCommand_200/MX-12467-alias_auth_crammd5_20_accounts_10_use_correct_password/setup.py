#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) set keys:
#               /*/common/perfStatThresholds:[StatImapAuthCommand 200]
#               /*/common/reportParamsInterval: [30]    # default 60
#               /*/common/badPasswordDelay: [0]         # nodelay ,default 1
#               /*/common/maxBadPasswordDelay: [0]      # no delay,default 90 
#               /*/common/loginAliases: [true]          # false by default
#               /*/imapserv/allowCRAMMD5: [true]        # enable cram-md5
# (2) create 20 accounts:testuser1@openwave.com -test20@openwave.com
# (3) create a alias name for each account testuser1 --> u1
# (4) calculate and set hamc value for each account
# (5) clear current imapserv.stat file

import basic_function
import basic_class
import imap_operations
import global_variables
import remote_operations
import time

#print (global_variables.get_value('initialpath'))

basic_class.mylogger_record.info('Runing setup testcase:mx-12467-alias_auth_crammd5_20_accounts_half_pass_half_fail')
basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')

imap1_host,imap1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('imap1_host','imap1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


basic_class.mylogger_record.info('step1:set keys')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=StatImapAuthCommand 200\";imconfcontrol -install -key \"/*/common/reportParamsInterval=30\";imconfcontrol -install -key \"/*/common/badPasswordDelay=0\";imconfcontrol -install -key \"/*/common/maxBadPasswordDelay=0\";imconfcontrol -install -key \"/*/common/loginAliases=true\";imconfcontrol -install -key \"/*/imapserv/allowCRAMMD5=true\"\''.format(mx_account),0)

basic_class.mylogger_record.info('step2:create 20 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=20;i++));do account-create {1}$i@{2}   {1}$i default;done\''.format(mx_account,test_account_base,default_domain),1,'Mailbox Created Successfully',20)

basic_class.mylogger_record.info('step3:create alias names for 20 accounts')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=20;i++));do imdbcontrol CreateAlias {1}$i u$i {2};done\''.format(mx_account,test_account_base,default_domain),0)

basic_class.mylogger_record.info('step4: set hmac for each account')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'for ((i=1;i<=20;i++));do hmac_value=$(imgenhmac {1}$i);echo $hmac_value; imdbcontrol sac {1}$i {2} mailpasswordhmac $hmac_value;done\''.format(mx_account,test_account_base,default_domain),0)

time.sleep(30) # to avoid last operations not expires
basic_class.mylogger_record.info('step5: clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)




