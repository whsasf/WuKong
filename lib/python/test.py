#!/usr/bin/env python3
from  imap_operations import IMAP_Ops

ipv4 = IMAP_Ops('10.49.58.239',20143)
#ipv4.imap_login('xx1','p')

#ipv4.imap_select('xx1','p')

ipv4.imap_authenticate('xx1','p')
#ipv4.imap_auth_crammd5('xx1','p')
ipv4.imap_select()
ipv4.imap_logout()