#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import cassandra
from cassandra.cluster import Cluster

cluster = Cluster(['10.49.58.240'],port=9043)
session = cluster.connect('KeyspaceBlobStore')

for i in range(0,20):
    target = 'select * from "CF_Message_{}" where key=0x93ddff266e4711e8b61ea12237d9bced and column1>=101;'.format(i)
    print(target)
    rows = session.execute(target)     
    print(list(rows))

                                  
session.execute('exit')