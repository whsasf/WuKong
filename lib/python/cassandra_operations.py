#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import basic_class
def cassandra_cqlsh_fetch_messagebody(blobip,blobport,messageid):
    """this function used to fetch message body"""
    
    from cassandra.cluster import Cluster
    
    cluster = Cluster([blobip],port=blobport,connect_timeout=30)
    session = cluster.connect('KeyspaceBlobStore')
    #session.row_factory = dict_factory
    
    for i in range(0,20):
        target = 'select * from "CF_Message_{0}" where key=0x{1} and column1 >=101;'.format(i,messageid)
        basic_class.mylogger_record.debug('target:')
        basic_class.mylogger_recordnf.debug(target)
        rows = session.execute(target,timeout=6000)     
        if rows:
            for row in rows:
                tmp = row[2].decode('utf-8','ignore')
                tmp = tmp[tmp.rindex('\x00'):]
            basic_class.mylogger_record.debug('message body is:')
            basic_class.mylogger_recordnf.debug(tmp)                
        #        print(row)                              
    cluster.shutdown()
    return tmp