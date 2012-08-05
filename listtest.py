#! /usr/bin/env python
#coding=utf-8

name = []

while True:
    flag = raw_input('Do you want to add person? yes/no:')
    if flag == 'yes':
        newitem = raw_input('so enter the new person:')
        name.append(newitem)
    else:
        break

print name
        