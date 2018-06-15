#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import basic_class
import encryption_decryption_related
def cassandra_cqlsh_fetch_messagebody(blobip,blobport,messageid,decryption_flag):
    """this function used to fetch message body"""
    
    from cassandra.cluster import Cluster
    
    cluster = Cluster([blobip],port=blobport,connect_timeout=30)
    session = cluster.connect('KeyspaceBlobStore')
    #session.row_factory = dict_factory
    
    for i in range(0,20):
        target = 'select * from "CF_Message_{0}" where key=0x{1} and column1 >=101;'.format(i,messageid)
        basic_class.mylogger_record.debug('target:')
        basic_class.mylogger_recordnf.debug(target)
        datas = session.execute(target,timeout=6000)     
        if raw_datas:
            for raw_data in raw_datas:
                if decryption_flag == 1:   # need decryption first
                    encryption_decryption_related.decrypt_aes()
                else:
                    basic_class.mylogger_record.debug('mesage body is not encrypted')
                
                data = raw_data
                data_format = data[2].decode('utf-8','ignore')
                data_format = data_format[data_format.rindex('\x00'):]
            basic_class.mylogger_record.debug('message body is:')
            basic_class.mylogger_recordnf.debug(data_format)                
        #        print(data)                              
    cluster.shutdown()
    return data_format