#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import cassandra
from cassandra.cluster import Cluster

cluster = Cluster(['10.49.58.240'],port=9043)
session = cluster.connect('KeyspaceBlobStore')

for i in range(0,20):
    target = 'select * from "KeyspaceBlobStore"."CF_Message_{}" where key=0xe61a14066e0f11e8bd5fbe29141ea2c6;'.format(i)
    print(target)
    rows = session.execute(target)     
    print(list(rows))

                                  
session.execute('exit')