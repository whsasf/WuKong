# -*- coding: utf-8 -*- 
# this module contains the IMAP operation related classes and functions

# import need moduels

from smtplib import SMTP
import global_variables
import basic_class

class SMTP_OPs(SMTP):
    """define a SMTP class and related functions"""
    
    def __init__(self,smtphost, smtpport, local_hostname=None,source_address=None,rspcode='',rspdata=''):
        """initial class"""
    
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.local_hostname = local_hostname
        self.source_address = source_address
        self.rspcode = rspcode
        self.rspdata = rspdata
        
        basic_class.mylogger_record.info('<init SMTP instance:smtp against >'+self.smtphost+':'+self.smtpport)
        self.smtp = SMTP(host=self.smtphost,port=self.smtpport,local_hostname=self.local_hostname,source_address=self.source_address)
    
    def smtp_connect(self,smtphost,smtpport):
        """Connect to a host on a given port and host"""
        
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.rspcode,self.rspdata = self.smtp.connect(self.smtphost,self.smtpport)
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]          
        
    def smtp_set_debuglevel(self):
        """Set the debug output level. A value of 1 or True for level results in debug messages 
        for connection and for all messages sent to and received from the server.
        A value of 2 for level results in these messages being timestamped
        smtp_debuglevel defined in etc global.vars
        """
        
        smtp_debuglevel = global_variables.get_value('smtp_debuglevel')
        basic_class.mylogger_record.debug('command:<set_debuglevel '+str(smtp_debuglevel)+'>') 
        self.smtp.set_debuglevel(int(smtp_debuglevel))
        #[basic_class.mylogger_record.debug(self.rspcode)]
        #[basic_class.mylogger_record.debug(self.rspdata.decode())]


    def smtp_helo(self):
        """Identify yourself to the SMTP server using HELO."""
        
        basic_class.mylogger_record.info('command:<helo>')
        self.rspcode,self.rspdata = self.smtp.helo()
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]       



    def smtp_ehlo(self):
        """Identify yourself to the SMTP server using EHLO."""
        
        basic_class.mylogger_record.info('command:<ehlo>')
        self.rspcode,self.rspdata = self.smtp.ehlo()
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]    
        

    def smtp_ehlo_or_helo_if_needed(self):  
        """This method call ehlo() and or helo() if there has been no 
        previous EHLO or HELO command this session. 
        It tries ESMTP EHLO first
        
        """
        
        basic_class.mylogger_record.info('command:<ehlo_or_helo_if_needed>')
        self.rspcode,self.rspdata = self.smtp.ehlo_or_helo_if_needed()
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]   
        
                        
    def smtp_starttls(self,keyfile=None, certfile=None, context=None):
        """Put the SMTP connection in TLS (Transport Layer Security) mode"""               
        
        self.keyfile = keyfile
        self.certfile = certfile
        self.context = context
        
        basic_class.mylogger_record.info('command:<starttls>')
        self.rspcode,self.rspdata = self.smtp.starttls(self.keyfile,self.certfile,self.context)
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]  
        
                
        
    def smtp_login(self,user,password,initial_response_ok=True):
        """Log in on an SMTP server that requires authentication."""
        
        self.user = user
        self.password = password
        self.initial_response_ok = initial_response_ok
        basic_class.mylogger_record.info('command:<auth login '+self.user+' '+self.password+'>')
        self.rspcode,self.rspdata = self.smtp.login(self.user,self.password,initial_response_ok=self.initial_response_ok)
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]       
        
    def smtp_auth_login(self,user,password):
        """auth login command"""
        
        self.user = user
        self.password = password
        #self.initial_response_ok = initial_response_ok

        basic_class.mylogger_record.info('command:<auth login '+self.user+' '+self.password+'>')
        self.rspcode,self.rspdata = self.smtp.auth_login(self.user,self.password)
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())]   
        
        
                
    def smtp_auth(self,user,password,mechanism,authobject,initial_response_ok=True):
        """Log in on an SMTP server that requires authentication."""
        
        self.user = user
        self.password = password
        self.mechanism = mechanism
        self.authobject = authobject
        self.initial_response_ok = initial_response_ok
        
        basic_class.mylogger_record.info('command:<auth login '+self.user+' '+self.password+'>')
        self.rspcode,self.rspdata = self.smtp.login(self.user,self.password,initial_response_ok=self.initial_response_ok)
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())] 
                
            
    def smtp_quit(self):
        """Terminate the SMTP session and close the connection"""
        
        basic_class.mylogger_record.info('command:<quit>')
        self.rspcode,self.rspdata = self.smtp.quit()
        [basic_class.mylogger_record.debug(self.rspcode)]
        [basic_class.mylogger_record.debug(self.rspdata.decode())] 
        #[basic_class.mylogger_record.debug(self.resp.decode())]