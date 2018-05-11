#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import basic_function
import basic_class
import imap_operations
import global_variables

print (global_variables.get_value('initialpath'))


myimap = imap_operations.IMAP_Ops('10.49.58.239',20143)
myimap.imap_login('xx1','p')
myimap.imap_logout()
