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
        """Send user command, response should indicate that a password is required."""
        
        import basic_class
        
        self.username = username
        basic_class.mylogger.info('<user '+self.username+'>')        
        self.resp = self.pop3.user(self.username)
        [basic_class.mylogger.debug(self.resp.decode())]
        
     
    def pop_pass(self,passwd):
        """Send password, response includes message count and mailbox size. Note: the mailbox on the server is locked until quit() is called."""
        
        import basic_class
        
        self.passwd = passwd
        basic_class.mylogger.info('<pass '+self.passwd+'>')        
        self.resp = self.pop3.pass_(self.passwd)
        [basic_class.mylogger.debug(self.resp.decode())]
        #self.pop.quit()                
        
        
    def pop_login(self,username,passwd):
        """this function will run pop_user and pop_pass"""  
        
        #import pop_user
        #import pop_pass
        
        self.username = username
        self.passwd = passwd
        self.pop_user(self.username)
        self.pop_pass(self.passwd)
        #self.pop.quit() 
        
    def pop_set_debuglevel(self):
        """Set the instances debugging level. This controls the amount of debugging output printed. The default, 0
           A value of 1 produces a moderate amount of debugging output, generally a single line per request. 
           A value of 2 or higher produces the maximum amount of debugging output, 
           logging each line sent and received on the control connection.
        """
                              
        pop_debuglevel = global_variables.get_value('pop_debuglevel')
        basic_class.mylogger.debug('<set_debuglevel '+str(pop_debuglevel)+'>') 
        self.pop3.set_debuglevel(int(pop_debuglevel))
        #self.pop.quit()
        
        
    def pop_apop(self,username,passwd):
        """Use the more secure APOP authentication to log into the POP3 server."""
        
        self.username = username
        self.passwd = passwd
        self.outcome,self.logdata = self.pop3.apop(self.username,self.passwd)
        basic_class.mylogger.info('<apop '+self.username+' xxxx>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit()          

    
    def pop_stat(self):
        """Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size)."""
        
        basic_class.mylogger.info('<stat>')
        self.resp= self.pop3.stat()
        [basic_class.mylogger.debug(self.resp.encode())]       
        #self.pop.quit()    
        
                
    def pop_list(self,which = ''):
        """Request message list, result is in the form (response, ['mesg_num octets', ...], octets). If which is set, it is the message to list"""                
        
        self.which = which
        self.resp = self.pop3.list(self.which)
        basic_class.mylogger.info('<list '+str(self.which)+'>')
        [basic_class.mylogger.debug(list(self.resp).decode())]       
        #self.pop.quit()    

        
    def pop_retr(self,which):
        """Retrieve whole message number which, and set its seen flag. Result is in form (response, ['line', ...], octets)."""
        
        self.which = which
        #m = self.pop3.retr(self.which)
        #print('m=',m.decode())
        self.resp, self.items, self.octets = self.pop3.retr(self.which)
        #basic_class.mylogger.info('<retr '+str(self.which)+'>')
        #[basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit()    
        
        
    def pop_dele(self,which):
        """Flag message number which for deletion. On most servers deletions are not actually performed until QUIT (the major exception is Eudora QPOP, which deliberately violates the RFCs by doing pending deletes on any disconnect)."""    
        
        self.which = which
        self.outcome,self.logdata = self.pop3.dele(self.which)
        basic_class.mylogger.info('<dele '+str(self.which)+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit()   
        
    def pop_rset(self):
        """Remove any deletion marks for the mailbox."""
         
        self.outcome,self.logdata = self.pop3.reset()
        basic_class.mylogger.info('<rset>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit() 

        
    def pop_noop(self):
        """Do nothing. Might be used as a keep-alive."""

        self.outcome,self.logdata = self.pop3.noop()
        basic_class.mylogger.info('<noop>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit() 

                
    def pop_top(self,which,howmuch):
        """Retrieves the message header plus howmuch lines of the message after the header of message number which
           Result is in form (response, ['line', ...], octets).
           The POP3 TOP command this method uses, unlike the RETR command, doesnt set the messages seen flag; 
           unfortunately, TOP is poorly specified in the RFCs and is frequently broken in off-brand servers. 
           Test this method by hand against the POP3 servers you will use before trusting it.
        """
        
        self.which = which
        self.howmuch = howmuch
        self.outcome,self.logdata = self.pop3.top(self.which,self.howmuch)
        basic_class.mylogger.info('<top >'+str(self.which)+' '+str(self.howmuch)+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit() 

        
    def pop_uidl(self,which=None):
        """Return message digest (unique id) list. If which is specified, result contains the unique id for that message in the form 'response mesgnum uid, otherwise result is list (response, ['mesgnum uid', ...], octets)."""    
        
        self.which = which
        self.outcome,self.logdata = self.pop3.uidl(self.which)
        basic_class.mylogger.info('<uidl '+str(self.which)+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit()         
        
        
    def pop_stls(self,context=None):
        """Start a TLS session on the active connection as specified in RFC 2595. This is only allowed before user authentication"""
        
        self.context = context
        self.outcome,self.logdata = self.pop3.stls(self.context)
        basic_class.mylogger.info('<stls '+str(self.context)+'>')
        [basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]       
        #self.pop.quit()     
               

                                    
    def pop_quit(self):
        """Signoff: commit changes, unlock mailbox, drop connection."""
        
        d=self.pop3.quit()
        print('d=',d)
        #self.resp, self.items, self.octets = self.pop3.quit()
        #self.outcome,self.logdata = self.pop3.quit()
        #basic_class.mylogger.debug('<quit>')
        #[basic_class.mylogger.debug(line.decode('utf-8')) for line in self.logdata]

        