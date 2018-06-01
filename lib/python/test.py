#!/usr/bin/env python3
from  pop_operations import POP_Ops

pop3 = POP_Ops('10.49.58.239',20110)
pop3.pop_set_debuglevel(5)
#pop3.pop_user('xx1')
#pop3.pop_pass('p')
pop3.pop_login('xx1','pp')
pop3.pop_list()
pop3.pop_retr(1)[1]
pop3.pop_quit()




#ipv4.imap_login('xx1','p')

#ipv4.imap_select('xx1','p')

#ipv4.imap_authenticate('xx1','p')
#ipv4.imap_auth_crammd5('xx1','p')
#ipv4.imap_select()
#ipv4.imap_logout()