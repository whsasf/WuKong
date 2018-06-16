#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

##steps:
# (1) set keys:
#               /*/common/messageBodyEncryptionEnabled:[false]
#               /*/mss/compressionEnabled: [false]   # need mss retart
#               /*/mxos/ldapEncryptionDn: [cn=encryption,cn=config]
#               /*/mxos/ldapReadEncryptionFilter: [(&(objectclass=messageBodyEncryption)(cn=encryption))]
#               /*/mxos/loadRulesOrder:[encryption]
# (2) create passphrase

import basic_function
import basic_class
import imap_operations
import smtp_operations
import global_variables
import remote_operations
from sendmails import send_mail
import time
import requests


basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')

mx1_mta1_port,mx1_mta1_host_ip,mx1_mxos2_port,mx1_mxos2_host_ip,mx1_mss2_host_ip,mx1_mss1_host_ip,mx1_pop1_host,mx1_pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('mx1_mta1_port','mx1_mta1_host_ip','mx1_mxos2_port','mx1_mxos2_host_ip','mx1_mss2_host_ip','mx1_mss1_host_ip','mx1_pop1_host','mx1_pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


basic_class.mylogger_record.info('step1:set keys and restart services')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/messageBodyEncryptionEnabled=true\";imconfcontrol -install -key \"/*/mss/compressionEnabled=false\";imconfcontrol -install -key \"/*/mxos/ldapEncryptionDn=cn=encryption,cn=config\";imconfcontrol -install -key \"/*/mxos/ldapReadEncryptionFilter=(&(objectclass=messageBodyEncryption)(cn=encryption))\";imconfcontrol -install -key \"/*/mxos/loadRulesOrder=domain\nmailbox\ncos\nmessage\ncustom\nadminrealm\nlogging\naddressbook\nnotify\nsaml\ntasks\ndatastore\nmailinglist\nencryption\"\''.format(mx_account),0)
remote_operations.remote_operation(mx1_mss1_host_ip,root_account,root_passwd,'su - {0} -c \'~/lib/imservctrl killStart mss\''.format(mx_account),0)
remote_operations.remote_operation(mx1_mss2_host_ip,root_account,root_passwd,'su - {0} -c \'~/lib/imservctrl killStart mss mxos\''.format(mx_account),0)
remote_operations.remote_operation(mx1_mxos2_host_ip,root_account,root_passwd,'su - {0} -c \'~/lib/imservctrl killStart mxos\''.format(mx_account),0)

time.sleep(50)

basic_class.mylogger_record.info('step2:create encryptin passphrase')
create_passphrase_result = requests.post('http://{0}:{1}/mxos/encryption/v2/messageBodyEncryption'.format(mx1_mxos2_host_ip,mx1_mxos2_port), data = {'currentKey':'1001:aes-128-cbc:10011001'})
basic_class.mylogger_record.info('create_passphrase_result:')
basic_class.mylogger_recordnf.debug(create_passphrase_result+'\n'+create_passphrase_result.text)

basic_class.mylogger_record.info('step3:fetch encryptin passphrase')
fetch_passphrase_result = requests.get('http://{0}:{1}/mxos/encryption/v2/messageBodyEncryption'.format(mx1_mxos2_host_ip,mx1_mxos2_port))
basic_class.mylogger_record.info('fetch_passphrase_result:')
basic_class.mylogger_recordnf.debug(fetch_passphrase_result+'\n'+fetch_passphrase_result.text)
