#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
import imap_operations
import basic_class

print('5-run')

#for i in range(1,3):
#    myimap = imap_operations.IMAP_Ops('10.49.58.239',20143)
#   #myimap.imap_login('xx1','pp')
#    try:
#        myimap.imap_authenticate('xx1','p')
#    except:
#        print('some error happened, but will pass')
#        pass
#   #myimap.imap_login('xx1','pp')
#   #myimap.imap_select()
#   #myimap.imap_fetch('1:6','rfc822')
#    myimap.imap_logout()

mylogger=basic_class.Loggger('WuKong','WARNING')

mylogger.debug('debug2')
mylogger.info('info2')
mylogger.warning('warning2')
mylogger.error('error2')
mylogger.critical('critical2')

