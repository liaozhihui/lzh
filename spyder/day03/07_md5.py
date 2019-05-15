# coding=utf-8
from hashlib import md5
from hashlib import sha1
s = md5()
s.update("hello".encode())
result1=s.hexdigest()
print(result1)

s = sha1()
s.update("hello".encode())
result2=s.hexdigest()
print(result2)