#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import basic_class
import requests

def create_and_fetch_passphrase(mxos_ip,mxos_port,uid,cipherName,encryptionKey):
    """this function is used to create and fetch passphrase for messagebody encryption feycntion,
        mxos API:messageBodyEncryption
    """
    
    basic_class.mylogger_record.info('create encryptin passphrase')
    create_passphrase_result = requests.post('http://{0}:{1}/mxos/encryption/v2/messageBodyEncryption'.format(mxos_ip,mxos_port), data = {'currentKey':'{}:{}:{}'.format(uid,cipherName,encryptionKey)})
    basic_class.mylogger_record.info('create_passphrase_result:')
    basic_class.mylogger_recordnf.debug(str(create_passphrase_result)+'\n'+str(create_passphrase_result.text))
    
    basic_class.mylogger_record.info('fetch encryptin passphrase')
    fetch_passphrase_result = requests.get('http://{0}:{1}/mxos/encryption/v2/messageBodyEncryption'.format(mxos_ip,mxos_port))
    basic_class.mylogger_record.info('fetch_passphrase_result:')
    basic_class.mylogger_recordnf.debug(str(fetch_passphrase_result)+'\n'+str(fetch_passphrase_result.text))
    
    target_count = fetch_passphrase_result.text.count(uid)
    basic_class.mylogger_record.debug('target_count= '+str(target_count))
    if target_count == 2:
        return('create encryptin passphrase successfully')
    else:
        return('create encryptin passphrase unsuccessfully')
