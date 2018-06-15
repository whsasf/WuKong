#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def decrypt_aes(mode,key,iv,data_to_decrypt):
    """thsi function is used to decypt the data that encrypted using AES"""
    
    # decide which mode to use 
    if 'cbc' in mode.lower():
        decryption_mode = 'AES.MODE_CBC'
    elif 'ecb' in mode.lower():
        decryption_mode = 'AES.MODE_ECB'
    elif 'cfb' in mode.lower():
        decryption_mode = 'AES.MODE_CFB'
    elif 'ofb' in mode.lower():
        decryption_mode = 'AES.MODE_OFB'
    elif 'ctr' in mode.lower():
        decryption_mode = 'AES.MODE_CTR'
    else:
        pass
       
    cipher = AES.new(key,decryption_mode,iv);   
    data_after_decrypt = cipher.decrypt(a2b_hex(data_to_decrypt))
    