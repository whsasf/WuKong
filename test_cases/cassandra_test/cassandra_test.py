#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import cassandra
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from cassandra.policies import RoundRobinPolicy

cluster = Cluster(['10.49.58.240'],port=9043,connect_timeout=30)
session = cluster.connect('KeyspaceBlobStore')
#session.row_factory = dict_factory

for i in range(0,20):
    target = 'select * from "CF_Message_{}" where key=0x787906706edf11e88486d3af9849e23b and column1 >=101;'.format(i)
    
    #print(target)
    rows = session.execute(target,timeout=6000)   
    if rows:
        print(list(rows))
        print('------------------------------------------------------------------------------')  
        for row in rows:
            tmp = row[2].decode('utf-8','ignore')
            tmp = tmp[tmp.rindex('\x00'):]
            print(tmp)
    #        print(row)                              
cluster.shutdown()
