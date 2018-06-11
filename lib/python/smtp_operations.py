# -*- coding: utf-8 -*- 
# this module contains the IMAP operation related classes and functions

# import need moduels

from smtplib import SMTP

class SMTP_OPs(SMTP):
    """define a SMTP class and related functions"""
    
    def __init__(self,smtphost, smtpport, local_hostname=None,source_address=None)
    """initial class"""
    
    self.smtphost = smtphost
    self.smtpport = smtpport
    self.local_hostname = local_hostname
    self.source_address = source_address
    
    