#!/usr/bin/python
# -*- coding: utf-8 -*-
# 每个英文字母对应一个七位二进制数（加密传统，也可按长度推测）
# 异或加密（Enigma中一定映射为更原来不一样的字母的思想）
def decode(str_bin,str_key):
	gap=len(str_bin)/len(str_key)
	print gap
	cipher_str=[]
	for i in xrange(len(str_key)):
		cipher_str.append(str_bin[gap*i:gap*i+gap])
		plain=''
	for i in xrange(len(str_key)):
		plain+= chr(int(cipher_str[i],2) ^ ord(str_key[i]))
	return plain
#注意粘贴完全
cipher='0000011000000000101010110111001011000101100000111001100100111100111001'
key='helloworld'
result=decode(cipher,key)
print result