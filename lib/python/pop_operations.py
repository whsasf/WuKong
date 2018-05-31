# -*- coding: utf-8 -*- 
# this module contains the IMAP operation related classes and functions

# import need moduels
from poplib import POP3

class POP_Ops(POP3):
    """this class defines all pop3 related methods"""  
      
    def __init__(self,pophost,popport,outcome = 0,logdata = '',pop3 = ''):
        """this init function will initiate target pop connection host and port
           example: instance = POP_Ops('10.49.58.239',20110)
        """        
        self.pophost = pophost
        self.popport = popport
        self.outcome = outcome    # outcome records the response code of each imap operation, like 200 means success
        self.logdata = logdata    # logdata is the data we got after executing the imap operation,usually used to verify if the operation success 
        self.pop3 = POP3(host = self.pophost,port = self.popport)  # instance of IMAP class
        #self.imap4_ssl = IMAP4_SSL(host = self.imaphost,port = self.imapport)  # instance of IMAP class