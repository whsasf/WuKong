#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

def cassandra_cqlsh_fetch_messagebody(blobip,blobport,messageid,decryption_flag):
    """this function used to fetch message body"""
    
    from cassandra.cluster import Cluster
    import global_variables
    import basic_class
    import encryption_decryption_related    
    
    iv = global_variables.get_values('AES_iv')  #AES_iv
    # get passphrase value
    if decryption_flag != 0:
        if '128' in decryption_flag:
            passphrase = global_variables.get_values('ASE_key128')
        elif '192' in decryption_flag:
            passphrase = global_variables.get_values('ASE_key192')
        elif '256' in decryption_flag:
            passphrase = global_variables.get_values('ASE_key256')
        else:
            pass 
    else:
        pass       
    cluster = Cluster([blobip],port=blobport,connect_timeout=30)
    session = cluster.connect('KeyspaceBlobStore')
    #session.row_factory = dict_factory
    
    for i in range(0,20):
        target = 'select * from "CF_Message_{0}" where key=0x{1};'.format(i,messageid)
        basic_class.mylogger_record.debug('target:')
        basic_class.mylogger_recordnf.debug(target)
        
        raw_datas = session.execute(target,timeout=6000)                
        if raw_datas:
            
            basic_class.mylogger_record.debug('raw_datas stored in KeyspaceBlobStore.CF_Message_{0} is:'.format(i))
            basic_class.mylogger_recordnf.debug(raw_datas[:])  

            for raw_data in raw_datas:  
                if raw_data[1] == 101: # this calomn contains the message body data               
                    basic_class.mylogger_record.debug('raw message body is:')
                    basic_class.mylogger_recordnf.debug(raw_data[2])
                
                    if decryption_flag == 0:   # no need decryption first
                        basic_class.mylogger_record.info('mesage body is not encrypted')
                        plain_data = raw_data[2]
                    else:                      # need decrypt,raw_data[2] is contains the message body raw data                   
                        basic_class.mylogger_record.info('mesage body is encrypted, need decrypt first')
                        plain_data = encryption_decryption_related.decrypt_aes(decryption_flag,passphrase,iv,raw_data[2])                
            
            basic_class.mylogger_record.debug('plain message body data is:')
            basic_class.mylogger_recordnf.debug(plain_data)  
            data_format = plain_data.decode('utf-8','ignore')
            try:
                data_format = data_format[data_format.rindex('\x00'):]
            except ValueError:
                basic_class.mylogger_recordnf.warning('substring not found')    
            basic_class.mylogger_record.debug('message body is:')
            basic_class.mylogger_recordnf.debug(data_format)                
                             
    cluster.shutdown()
    return data_format