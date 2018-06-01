# -*- coding: utf-8 -*- 
# this module contains the IMAP operation related classes and functions

# import need moduels
from imaplib import IMAP4
import base64
import time
import basic_class

class IMAP_Ops(IMAP4):
    """this class defines all imap related methods"""    
    def __init__(self,imaphost,imapport,outcome = 0,logdata = '',imap4 = ''):
        """this init function will initiate target imap connection host and port
           example: instance = IMAP_Ops('10.49.58.239',20143)
        """        
        self.imaphost = imaphost
        self.imapport = imapport
        self.outcome = outcome    # outcome records the response code of each imap operation, like 200 means success
        self.logdata = logdata    # logdata is the data we got after executing the imap operation,usually used to verify if the operation success 
        self.imap4 = IMAP4(host = self.imaphost,port = self.imapport)  # instance of IMAP class
        #self.imap4_ssl = IMAP4_SSL(host = self.imaphost,port = self.imapport)  # instance of IMAP class
        
        
        
    def imap_login(self,loginuser,loginpass):
        """method imap_login will perform imap login operation
           example: instance.imap_login('xx1','p')
        """       
        self.loginuser = loginuser
        self.loginpass = loginpass
        self.outcome,self.logdata = self.imap4.login(self.loginuser,self.loginpass)
        basic_class.mylogger.info('<imap login '+self.loginuser+' '+self.loginpass+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]
        #self.imap4.logout()
    
    
    
    def imap_logout(self):
        """method imap_logout will perform imap logout operation
           example: instance.imap_logout()
        """
        self.outcome,self.logdata = self.imap4.logout()
        basic_class.mylogger.info('<imap logout>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]



    def imap_select(self,mailbox = 'INBOX',readonly = False):
        """method imap_select will perform imap select operation
           example: instance.imap_select() or instance.imap_select('SentMail',True) or instance.imap_select('SentMail')
        """
        self.mailbox = mailbox     # the folder that will be selected
        self.readonly = readonly   # If the readonly flag is set, modifications to the mailbox are not allowed
        self.outcome,self.logdata = self.imap4.select(mailbox = self.mailbox,readonly = self.readonly)
        basic_class.mylogger.info('<imap select '+self.mailbox+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]
        #self.imap4.logout()
   
    
    def imap_fetch(self,message_set, message_parts):
        """method imap_fetch will perform imap fetch operation
           example: instance.imap_fetch(1,'RFC822') or instance.imap_fetch(1:*,'body[text]')   
        """
    
        self.message_set = message_set
        self.message_parts = message_parts
        self.outcome,self.logdata = self.imap4.fetch(self.message_set, self.message_parts)
        basic_class.mylogger.info('<imap fetch '+self.message_set+' '+self.message_parts+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata[0] if self.outcome == 'OK']
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata if self.outcome == 'NO' ]
        #self.imap4.logout()
        
    
    def imap_authenticate(self,loginuser,loginpass,mechanism = 'PLAIN'):
        """method imap_authenticate will perform imap authenticate operation,commonly used for imap plain authentication
           example: instance.imap_authenticate('xx1','p')
        """
        self.loginuser = loginuser
        self.loginpass = loginpass
        self.mechanism = mechanism
        self.authobject = lambda authobject:'\x00{0}\x00{1}'.format(self.loginuser,self.loginpass)
        basic_class.mylogger.debug('mechanism = '+str(self.mechanism))
        basic_class.mylogger.debug('authobject = '+str(self.authobject))
        self.outcome,self.logdata = self.imap4.authenticate(self.mechanism,self.authobject)
        basic_class.mylogger.info('<imap authenticate plain>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]
        #self.imap4.logout()

    def imap_auth_crammd5(self,loginuser,loginpass):
        """method imap_auth_crammd5 will perform imap cram-md5 authentication
           example: instance.imap_auth_crammd5('xx1','p')
        """
        self.loginuser = loginuser
        self.loginpass = loginpass
        self.outcome,self.logdata = self.imap4.login_cram_md5(self.loginuser,self.loginpass)
        basic_class.mylogger.info('<imap authenticate cram-md5>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]
        #self.imap4.logout()
 

#def imap_login(imaphost,imapport,loginuser,loginpass):           # merge create instance and imap_login
#    """method imap_login will perform imap login operation
#       example: instance.imap_login('10.49.58.239',20143,'xx1','p')
#    """    
#    myimap = IMAP_Ops(imaphost,imapport)
#    myimap.imap_login(loginuser,loginpass)
#
#
#def imap_authenticate(imaphost,imapport,loginuser,loginpass):    # merge create instance and imap_authenticate
#    """method imap_authenticate will perform imap authenticate operation,commonly used for imap plain authentication
#       example: instance.imap_authenticate('10.49.58.239',20143,'xx1','p')
#    """    
#    myimap = IMAP_Ops(imaphost,imapport)
#    myimap.imap_authenticate(loginuser,loginpass)
#    
#    
#def imap_auth_crammd5(imaphost,imapport,loginuser,loginpass):   # merge create instance and imap_auth_crammd5
#    """method imap_auth_crammd5 will perform imap cram-md5 authentication
#       example: instance.imap_auth_crammd5('10.49.58.239',20143,'xx1','p')
#    """    
#    myimap = IMAP_Ops(imaphost,imapport)
#    myimap.imap_auth_crammd5(loginuser,loginpass)
#       
    
        