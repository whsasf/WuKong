#!/usr/bin/env python
from imaplib import IMAP4_SSL
import base64

ipv4 = IMAP4_SSL(host = '10.49.58.239',port = 20993)
#ipv4.imap_login('xx1','p')

#ipv4.imap_select('xx1','p')
#authobject = lambda x:"base64.b64encode(b'\x00{0}\x00{1}').decode('utf-8')".format('xx1','p')
def authobject():
    return "base64.b64encode(b'\x00xx1\x00p')"
ipv4.authenticate('PLAIN',eval(authobject()))
