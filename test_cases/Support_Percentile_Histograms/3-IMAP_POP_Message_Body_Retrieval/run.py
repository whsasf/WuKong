#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import basic_function
import basic_class
import imap_operations
import global_variables
import time
import remote_operations
import stat_statistics

basic_class.mylogger_record.debug('Preparing... get some variables needed for tests')                                                               
                                                                                                                                                    
mss1_host_ip,mss2_host_ip,imap1_host_ip,imap1_port,mta1_host_ip,mta1_port,pop1_host_ip,pop1_port,mx_account,mx1_host1_ip,root_account,root_passwd,test_account_base,default_domain = \
global_variables.get_values('mss1_host_ip','mss2_host_ip','imap1_host_ip','imap1_port','mta1_host_ip','mta1_port','pop1_host_ip','pop1_port','mx_account','mx1_host1_ip','root_account','root_passwd','test_account_base','default_domain')


# IMAP Message Body Retrieval--StatMSSRetrMsg
basic_class.mylogger_recordnf.title('IMAP Message Body Retrieval--StatMSSRetrMsg')
basic_class.mylogger_recordnf.title('StatMSSRetrMsg=200')
basic_class.mylogger_record.info('set keys:StatMSSRetrMsg=200')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=StatMSSRetrMsg 200\"\''.format(mx_account),0)
remote_operations.remote_operation(mss1_host_ip,root_account,root_passwd,'su - {0} -c "~/lib/imservctrl killStart mta"'.format(mx_account),0)

#1#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-11664:imap fetch INBOX 1:5 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1:5','rfc822')
    myimap.imap_fetch('1:5','rfc822.text')
    myimap.imap_fetch('1:5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',75)
basic_function.summary(result_lists,'MX-11664:imap fetch INBOX 1:5 body,for 10 accounts')


#2#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-11666:imap fetch INBOX 1,3,4,5 body for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1,3,4,5','rfc822')
    myimap.imap_fetch('1,3,4,5','rfc822.text')
    myimap.imap_fetch('1,3,4,5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',60)
basic_function.summary(result_lists,'MX-11666:imap fetch INBOX 1,3,4,5 body for 10 accounts')


#3#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12447:imap fetch INBOX 2 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('2','rfc822')
    myimap.imap_fetch('2','rfc822.text')
    myimap.imap_fetch('2','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12447:imap fetch INBOX 2 body ,for 10 accounts')


#4#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12567:imap fetch INBOX 1:* body ,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1:*','rfc822')
    myimap.imap_fetch('1:*','rfc822.text')
    myimap.imap_fetch('1:*','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',105)
basic_function.summary(result_lists,'MX-12567:imap fetch INBOX 1:* body ,for 10 accounts')



#5#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12568:imap fetch INBOX 7 body,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('7','rfc822')
    myimap.imap_fetch('7','rfc822.text')
    myimap.imap_fetch('7','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12568:imap fetch INBOX 7 body,for 10 accounts')



#6#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12587:imap fetch test 1:5 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1:5','rfc822')
    myimap.imap_fetch('1:5','rfc822.text')
    myimap.imap_fetch('1:5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',75)
basic_function.summary(result_lists,'MX-12587:imap fetch test 1:5 body ,for 10 accounts')



#7#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12588:imap fetch test 1,3,4,6 body for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1,3,4,6','rfc822')
    myimap.imap_fetch('1,3,4,6','rfc822.text')
    myimap.imap_fetch('1,3,4,6','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',60)
basic_function.summary(result_lists,'MX-12588:imap fetch test 1,3,4,6 body for 10 accounts')



#8#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase: MX-12589:imap fetch test 2 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('2','rfc822')
    myimap.imap_fetch('2','rfc822.text')
    myimap.imap_fetch('2','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,' MX-12589:imap fetch test 2 body ,for 10 accounts')



#9#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12590:imap fetch test 1:* body ,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1:*','rfc822')
    myimap.imap_fetch('1:*','rfc822.text')
    myimap.imap_fetch('1:*','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',120)
basic_function.summary(result_lists,'MX-12590:imap fetch test 1:* body ,for 10 accounts')



#10#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12591:imap fetch test 7 body,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('7','rfc822')
    myimap.imap_fetch('7','rfc822.text')
    myimap.imap_fetch('7','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12591:imap fetch test 7 body,for 10 accounts')


basic_class.mylogger_recordnf.title('StatMSSRetrMsg=0')
basic_class.mylogger_record.info('chang key to:StatMSSRetrMsg=0')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c \'imconfcontrol -install -key \"/*/common/perfStatThresholds=StatMSSRetrMsg 0\"\''.format(mx_account),0)
remote_operations.remote_operation(mss1_host_ip,root_account,root_passwd,'su - {0} -c "~/lib/imservctrl killStart mta"'.format(mx_account),0)

#11#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12595:imap fetch INBOX 1:5 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1:5','rfc822')
    myimap.imap_fetch('1:5','rfc822.text')
    myimap.imap_fetch('1:5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',75)
basic_function.summary(result_lists,'MX-12595:imap fetch INBOX 1:5 body ,for 10 accounts')


#12#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12596:imap fetch INBOX 1,3,4,5 body for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1,3,4,5','rfc822')
    myimap.imap_fetch('1,3,4,5','rfc822.text')
    myimap.imap_fetch('1,3,4,5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',60)
basic_function.summary(result_lists,'MX-12596:imap fetch INBOX 1,3,4,5 body for 10 accounts')


#13#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12597:imap fetch INBOX 2 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('2','rfc822')
    myimap.imap_fetch('2','rfc822.text')
    myimap.imap_fetch('2','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12597:imap fetch INBOX 2 body ,for 10 accounts')


#14#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12598:imap fetch INBOX 1:* body ,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('1:*','rfc822')
    myimap.imap_fetch('1:*','rfc822.text')
    myimap.imap_fetch('1:*','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',105)
basic_function.summary(result_lists,'MX-12598:imap fetch INBOX 1:* body ,for 10 accounts')



#15#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12599:imap fetch INBOX 7 body,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select()
    myimap.imap_fetch('7','rfc822')
    myimap.imap_fetch('7','rfc822.text')
    myimap.imap_fetch('7','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12599:imap fetch INBOX 7 body,for 10 accounts')



#16#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12600:imap fetch test 1:5 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1:5','rfc822')
    myimap.imap_fetch('1:5','rfc822.text')
    myimap.imap_fetch('1:5','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',75)
basic_function.summary(result_lists,'MX-12600:imap fetch test 1:5 body ,for 10 accounts')



#17#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12601:imap fetch test 1,3,4,6 body for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1,3,4,6','rfc822')
    myimap.imap_fetch('1,3,4,6','rfc822.text')
    myimap.imap_fetch('1,3,4,6','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',60)
basic_function.summary(result_lists,'MX-12601:imap fetch test 1,3,4,6 body for 10 accounts')



#18#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase: MX-12602:imap fetch test 2 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('2','rfc822')
    myimap.imap_fetch('2','rfc822.text')
    myimap.imap_fetch('2','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,' MX-12602:imap fetch test 2 body ,for 10 accounts')



#19#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12603:imap fetch test 1:* body ,for 10 accounts:expect fail')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('1:*','rfc822')
    myimap.imap_fetch('1:*','rfc822.text')
    myimap.imap_fetch('1:*','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',120)
basic_function.summary(result_lists,'MX-12603:imap fetch test 1:* body ,for 10 accounts')



#20#########################################################################################################################
basic_class.mylogger_recordnf.title('running testcase:MX-12604:imap fetch INBOX 1:5 body ,for 10 accounts:expect success')
basic_class.mylogger_record.info('clear current imapserv.stat file')
remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "> log/imapserv.stat"'.format(mx_account),0)

for i in range(1,6):
    myimap = imap_operations.IMAP_Ops(imap1_host_ip,imap1_port)
    myimap.imap_login(test_account_base+str(i),test_account_base+str(i))
    myimap.imap_select('test')
    myimap.imap_fetch('7','rfc822')
    myimap.imap_fetch('7','rfc822.text')
    myimap.imap_fetch('7','body[text]')
    myimap.imap_logout()

basic_class.mylogger_record.info('fetching imapserv.stat ...')
time.sleep (50)
basic_class.mylogger_record.info('check and analyze imapserv.stat file ...')
imapserv_stat_content = remote_operations.remote_operation(mx1_host1_ip,root_account,root_passwd,'su - {0} -c "cat log/imapserv.stat|grep StatMSSRetrMsg"'.format(mx_account),0)
result_lists = stat_statistics.stat_statistic(imapserv_stat_content,'[200]','StatMSSRetrMsg',15)
basic_function.summary(result_lists,'MX-12604:imap fetch test 7 body,for 10 accounts')








