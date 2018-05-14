# -*- coding: utf-8 -*- 
# this module contains the clacces used commenly

# import need moduels
import os      # import listdir,getcwd,chdir,system,path #used in class Directory
import logging # import StreamHandler,FileHandler,Formatter,getLogger,info,debug,warning,error,critical #used in class Loggger
import global_variables

class Discovery():
    """class Discovery used to traverse the testcases and run them"""   
    #def __init__(self):
    
    def traverse(self,Path):
        """ this function is used to traverse all folders and files under target path,an run specific scripts"""        
        self.Path = Path
        os.chdir(self.Path)        
        currentlists = os.listdir('.') # get current folder and file names in current path
        for list in currentlists:      # delete the hiden files and folders
            if list.startswith('.'):
                currentlists.remove(list)
        #print (currentlists)        
        if 'setup' in currentlists:            # run setup
            os.system('chmod +x setup;./setup')            
        if 'run' in currentlists:              # run run
            os.system('chmod +x run;./run')           
        for list in currentlists:
            if os.path.isdir(list):
                self.traverse(list)
                #os.chdir(list)
                #print (os.getcwd())
        if 'teardown' in currentlists:         # run teardown 
            os.system('chmod +x teardown;./teardown')
        os.chdir('..')
        
        
        
        
        
class Loggger():
    """this is a class for logging part"""
    
    def __init__(self,loggername,chloglevel):    	
        """ definition of some"""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.chloglevel = chloglevel        
        self.ch = logging.StreamHandler()
        #get chloglevel from outside
        if 'WARNING' in self.chloglevel:
            self.ch.setLevel(logging.WARNING)
        elif 'DEBUG' in self.chloglevel:
            self.ch.setLevel(logging.DEBUG)
        else:
            self.ch.setLevel(logging.ERROR)
        #self.ch.setLevel(logging.ERROR)        
        currentpath = global_variables.get_value('currentpath')
        self.fh = logging.FileHandler(currentpath+'/logs/Alltestcases.log')
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(levelname)s]- %(message)s')
        self.ch.setFormatter(self.formatter)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)
        
    def debug(self,debugmessages='this is debug message'):   
        self.logger.debug(debugmessages)
        
    def info(self,infomessages='this is info message'):
        self.logger.info(infomessages)

    def warning(self,warnmessages='this is warn message'):
        self.logger.warn(warnmessages)

    def error(self,errormessages='this is error message'):    
        self.logger.error(errormessages)

    def critical(self,criticalmessages='this is critical message'):    
        self.logger.critical(criticalmessages)
     