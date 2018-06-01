# -*- coding: utf-8 -*- 
# this module contains the IMAP operation related classes and functions

# import need moduels
from poplib import POP3
import global_variables
import basic_class

        
class POP_Ops(POP3):
    """this class defines all pop3 related methods"""  
      
    def __init__(self,pophost,popport,resp = '',items = '',octets = '',pop3 = ''):
        """this init function will initiate target pop connection host and port
           example: instance = POP_Ops('10.49.58.239',20110)
        """        
        self.pophost = pophost
        self.popport = popport
        self.resp = resp    # outcome records the response code of each imap operation, like 200 means success
        self.items = items    # logdata is the data we got after executing the imap operation,usually used to verify if the operation success 
        self.octets = octets       
        self.pop3 = POP3(host = self.pophost,port = self.popport)  # instance of IMAP class
        #self.imap4_ssl = IMAP4_SSL(host = self.imaphost,port = self.imapport)  # instance of IMAP class


        
    def pop_user(self,username):
        """Send user command, response should indicate that a password is required.
           example: instance.pop_user('xx1')
        """
        
        import basic_class
        
        self.username = username
        basic_class.mylogger.info('<user '+self.username+'>')        
        self.resp = self.pop3.user(self.username)
        [basic_class.mylogger.debug(self.resp.decode())]
        
     
    def pop_pass(self,passwd):
        """Send password, response includes message count and mailbox size. Note: the mailbox on the server is locked until quit() is called.
           example: instance.pop_pass('p')
        """
        
        import basic_class
        
        self.passwd = passwd
        basic_class.mylogger.info('<pass '+self.passwd+'>')        
        try:
            self.resp = self.pop3.pass_(self.passwd)
        finally:    
            [basic_class.mylogger.debug(self.resp.decode())]
        #self.pop.quit()                
        
        
    def pop_login(self,username,passwd):
        """this function will run pop_user and pop_pass
           example: instance.pop_login('xx1','p')
        """  
        
        #import pop_user
        #import pop_pass
        
        self.username = username
        self.passwd = passwd
        self.pop_user(self.username)
        self.pop_pass(self.passwd)
        #self.pop.quit() 
        
    def pop_getwelcome(self):
        """Returns the greeting string sent by the POP3 server.
           seems not implemented in current mx
        """    
        
        basic_class.mylogger.info('<getwelcome>')        
        self.resp = self.pop3.pass_()
        [basic_class.mylogger.debug(self.resp.decode())]
        
    
    def pop_capa(self):
        """Query the servers capabilities as specified in RFC 2449. Returns a dictionary in the form {'name': ['param'...]}.
           example: instance.pop_capa()
        """    
        
        basic_class.mylogger.info('<capa>')        
        self.resp = self.pop3.capa()
        [basic_class.mylogger.debug(single_resp) for single_resp in self.resp]
        
        
    def pop_set_debuglevel(self):
        """Set the instances debugging level. This controls the amount of debugging output printed. The default, 0
           A value of 1 produces a moderate amount of debugging output, generally a single line per request. 
           A value of 2 or higher produces the maximum amount of debugging output, 
           logging each line sent and received on the control connection.
           example: instance.pop_set_debuglevel()   or instance.pop_set_debuglevel(1)
        """
                              
        pop_debuglevel = global_variables.get_value('pop_debuglevel')
        basic_class.mylogger.debug('<set_debuglevel '+str(pop_debuglevel)+'>') 
        self.pop3.set_debuglevel(int(pop_debuglevel))
        #self.pop.quit()
        
        
    def pop_apop(self,username,passwd):
        """Use the more secure APOP authentication to log into the POP3 server.
           example:instance.pop_apop('xx1','p')
        """
        
        self.username = username
        self.passwd = passwd
        basic_class.mylogger.info('<apop '+self.username+' xxxx>')        
        self.resp = self.pop3.apop(self.username,self.passwd)
        [basic_class.mylogger.debug(self.resp.decode())]       
        #self.pop.quit()          

    
    def pop_stat(self):
        """Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size).
           example:instance.pop_stat()
        """
        
        basic_class.mylogger.info('<stat>')
        self.resp, self.items = self.pop3.stat()
        [basic_class.mylogger.debug(self.resp)] 
        [basic_class.mylogger.debug(self.items)]       
        #self.pop.quit()    
        
                
    def pop_list(self,which = None):
        """Request message list, result is in the form (response, ['mesg_num octets', ...], octets). If which is set, it is the message to list
           example:instance.pop_list() or instance.pop_list(1) 
        """  
        
        self.which = which
        basic_class.mylogger.info('<list '+str(self.which)+'>')
        if self.which:
            self.resp = self.pop3.list(self.which)
            [basic_class.mylogger.debug(self.resp.decode())]     
        else:    
            self.resp,self.items,self.octets = self.pop3.list(self.which)
            [basic_class.mylogger.debug(item.decode()) for item in self.items]       
        #self.pop.quit()    

        
    def pop_retr(self,which):
        """Retrieve whole message number which, and set its seen flag. Result is in form (response, ['line', ...], octets).
           example:instance.pop_retr(1)
        """
        
        self.which = which
        basic_class.mylogger.info('<retr '+str(self.which)+'>')
        self.resp,self.items,self.octets = self.pop3.retr(self.which)
        [basic_class.mylogger.debug(item.decode()) for item in self.items]       
        #self.pop.quit()    
        
        
    def pop_dele(self,which):
        """Flag message number which for deletion. On most servers deletions are not actually performed until QUIT (the major exception is Eudora QPOP, which deliberately violates the RFCs by doing pending deletes on any disconnect).
           example:instance.pop_dele(1)
        """    
        
        self.which = which
        basic_class.mylogger.info('<dele '+str(self.which)+'>')        
        self.resp = self.pop3.dele(self.which)
        [basic_class.mylogger.debug(self.resp.decode())]       
        #self.pop.quit()   
        
    def pop_rset(self):
        """Remove any deletion marks for the mailbox.
           example:instance.pop_rset()
        """
        
        basic_class.mylogger.info('<rset>') 
        self.resp= self.pop3.rset()
        [basic_class.mylogger.debug(self.resp.decode())]       
        #self.pop.quit() 

        
    def pop_noop(self):
        """Do nothing. Might be used as a keep-alive.
           example:instance.pop_noop()
        """

        basic_class.mylogger.info('<noop>')        
        self.resp = self.pop3.noop()
        [basic_class.mylogger.debug(self.resp.decode())]       
        #self.pop.quit() 

                
    def pop_top(self,which,howmuch):
        """Retrieves the message header plus howmuch lines of the message after the header of message number which
           Result is in form (response, ['line', ...], octets).
           The POP3 TOP command this method uses, unlike the RETR command, doesnt set the messages seen flag; 
           unfortunately, TOP is poorly specified in the RFCs and is frequently broken in off-brand servers. 
           Test this method by hand against the POP3 servers you will use before trusting it.
           example:instance.pop_top(2,2)
        """
        
        self.which = which
        self.howmuch = howmuch
        basic_class.mylogger.info('<top >'+str(self.which)+' '+str(self.howmuch)+'>')        
        self.resp,self.items,self.octets = self.pop3.top(self.which,self.howmuch)
        [basic_class.mylogger.debug(item.decode()) for item in self.items]       
        #self.pop.quit() 

        
    def pop_uidl(self,which = None):
        """Return message digest (unique id) list. If which is specified, result contains the unique id for that message in the form 'response mesgnum uid, otherwise result is list (response, ['mesgnum uid', ...], octets).
            example:instance.pop_uidl()  or instance.pop_uidl(1) 
        """
        
        self.which = which
        basic_class.mylogger.info('<uidl '+str(self.which)+'>')   
        if self.which:
            self.resp = self.pop3.uidl(self.which)
            [basic_class.mylogger.debug(self.resp.decode())]             
        else:   
            self.resp,self.items,self.octets = self.pop3.uidl(self.which)
            [basic_class.mylogger.debug(item.decode()) for item in self.items]       
        #self.pop.quit()         
        
        
    def pop_stls(self,context=None):
        """Start a TLS session on the active connection as specified in RFC 2595. This is only allowed before user authentication"""
        
        self.context = context
        basic_class.mylogger.info('<stls '+str(self.context)+'>')        
        self.resp = self.pop3.stls(self.context)
        [basic_class.mylogger.debug(self.resp)]       
        #self.pop.quit()     
               

                                    
    def pop_quit(self):
        """Signoff: commit changes, unlock mailbox, drop connection.
           example:instance.pop_quit()
        """
        
        basic_class.mylogger.info('<quit>')
        self.resp = self.pop3.quit()
        [basic_class.mylogger.debug(self.resp.decode())]

        