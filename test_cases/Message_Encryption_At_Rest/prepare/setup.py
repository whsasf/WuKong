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


import smtp_operations
import global_variables


#basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')

mx1_mta1_port,mx1_mta1_host_ip,mx1_mxos2_port,mx1_mxos2_host_ip,mx1_mss2_host_ip,mx1_mss1_host_ip,mx1_pop1_host,mx1_pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('mx1_mta1_port','mx1_mta1_host_ip','mx1_mxos2_port','mx1_mxos2_host_ip','mx1_mss2_host_ip','mx1_mss1_host_ip','mx1_pop1_host','mx1_pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


smtp_operations.fast_send_mail(mx1_mta1_host_ip,mx1_mta1_port,'xx2',['xx1'])
