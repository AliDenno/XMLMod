from binascii import *
raw_bytes = open('nodess046.xsf','rb').read()
i = 0
str_one = b2a_base64(raw_bytes) # 1
'''
str_list = b2a_base64(raw_bytes).split("\n") #2

bytesBackAll = a2b_base64(''.join(str_list)) #2
print bytesBackAll == raw_bytes #True #2
'''
bytesBackAll = a2b_base64(str_one) #1
print(bytesBackAll)
#print bytesBackAll == raw_bytes #True #1