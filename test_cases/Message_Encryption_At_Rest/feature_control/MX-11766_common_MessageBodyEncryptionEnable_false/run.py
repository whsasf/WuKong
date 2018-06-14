#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import basic_function
import basic_class
import imap_operations
import smtp_operations
import global_variables
import remote_operations
from sendmails import send_mail
import time
import requests
import cassandra_operations

result_lists = []

basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')

mx1_blobstore_port,mx1_blobstore_host_ip,mx1_mxos2port,mx1_mxos2host_ip,mx1_mss2_host_ip,mx1_mss1_host_ip,mx1_pop1_host,mx1_pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('mx1_blobstore_port','mx1_blobstore_host_ip','mx1_mxos2port','mx1_mxos2host_ip','mx1_mss2_host_ip','mx1_mss1_host_ip','mx1_pop1_host','mx1_pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


basic_class.mylogger_record.debug('step1:fetching the latest message uuid')

basic_class.mylogger_record.debug('uuids:')
uuids=requests.get('http://{0}:{1}/mxos/mailbox/v2/testuser1@openwave.com/folders/inbox/messages/metadata/uuid/list'.format(mx1_mxos2host_ip,mx1_mxos2port))
basic_class.mylogger_recordnf.debug(uuids)

basic_class.mylogger_record.debug('uuid:')
uuid = (uuids.text.split('"')[-2]).replace('-','')
basic_class.mylogger_recordnf.debug(uuid)
basic_class.mylogger_record.debug('step2:fetch message body from cassandrablob directly')

messagebody = cassandra_operations.cassandra_cqlsh_fetch_messagebody(mx1_blobstore_host_ip,mx1_blobstore_port,uuid)

body_check_flag = messagebody.count(' we love world !!!!!!ucucucucucuc')
basic_class.mylogger_record.debug('body_check_flag= '+str(body_check_flag))

if body_check_flag >=1:
    result_lists.append('success')
else:
    result_lists.append('fail')    

basic_function.summary(result_lists)

