#! /usr/bin/env python
#coding=utf-8
# some common methods of string 
# find : use to find a short string in string
print 'I am a dog'.find("dog")
title = 'I must study python for my job'
print title.find('must')
print title.find('I')
print title.find('sdf')

# join: to add item into string
seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)
dirs = '','usr','bin','env'
print '/'.join(dirs)
print 'C:' + '\\'.join(dirs)

# split: to spilt string 
print '1+2+3+4+5'.split('+')
print 'I am a dog'.split()

# lower: translate the A to a
print 'Later'.lower()

# replace: replace a part of the string to another string 
print 'This is a pig'.replace('pig','dog')

# strip: delete the blank of the end and first of string
print '           This is a pig       '.strip()

