#!/usr/bin/python
# -*- coding: utf-8 -*-
# 大家来解密
from Crypto.Cipher import AES
import hashlib
from binascii import b2a_hex,a2b_hex
import base64

def md5ToHex(text,bit):
    hash=hashlib.md5(text).hexdigest()
    print hash
    print hash[(32-bit)/2:32-(32-bit)/2]
    return hash[(32-bit)/2:32-(32-bit)/2]

#密钥长度必须为16（AES-128)、24（AES-192）或32（AES-256）位,IV必须为16位（课程PPT中指明使用AES-128）
#首先用md5算法对原有key和IV进行处理
given_key='venusCTF-hex'
given_iv='123-MD5'
obj=AES.new(md5ToHex(given_key,16),AES.MODE_CBC,md5ToHex(given_iv,16))
cipher='a80d5eb43508e549f83e2e254c0a0f0644be58f453baced4af4777c4cd1b7575'
plainText=obj.decrypt(cipher)
print plainText
print b2a_hex(plainText)
print str(base64.b64encode(plainText))
