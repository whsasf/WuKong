#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##steps:
# (1) imap login 125 accounts with correct credentials, the other 125 use wrong credentials
# (2) check imapserv.stats .make sure the total attempts are 250 ,and half passed ,half failed

import basic_function
import basic_class
import imap_operations
import global_variables

#myimap = imap_operations.IMAP_Ops('imap1host,imap1port)
#myimap.imap_login('xx1','p')
#myimap.imap_logout()