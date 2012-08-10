#! /usr/bin/env python
#coding=utf-8

# list Function
print list ('Hello')

#change item
x = [1,1,1]
x[1] = 2 
print x

#del item
names = ['Alice','Ball','Cecil','Daa','Ez']
del names[2]
print names

#Slice assignment --important
name = list('Perl')
print name 
name[2:] = list('ar')
print name

name = list('Perl')
name[1:] = list('ython')
print name 

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers
print numbers[0:5:2]

numbers[0:5:2] = [2,2,2]
print numbers

