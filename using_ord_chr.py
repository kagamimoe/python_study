#!/usr/bin/env python
#coding = utf-8

#ת����Сд��ĸ
def UCaseChar(ch):
    if ord(ch) in range(97,122):       
        ch = chr(ord(ch) - 32)
    return ch

#ת���ɴ�д��ĸ
def LCaseChar(ch):
    if ord(ch) in range(65,91):
        ch = chr(ord(ch) + 32)
    return ch

def UCase(str):
    return "".join(map(UCaseChar,str))

def LCase(str):
    return "".join(map(LCaseChar,str))

print UCase('ACSvsdf')
print LCase('ACDsdfs')

