# -*- coding:utf-8 -*-
import os
import os.path


print 'hello world'
print r'\t\r'
print '\t\r'
print '\\t\\r'
#print os.system('dir')

#!/usr/bin/env python

# -*- coding:utf-8 -*-
#! /usr/bin/python

#
def show(arg, dirname, filenames):
	print 'dirname:' + dirname
	for f in filenames:
		if os.path.isfile(dirname+'\\'+f):
			print '-' + f 

os.path.walk('D:\\test', show, None)
print '############'

#rootdir = r'D:\\test' # 指明被遍历的文件夹
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#输出文件夹信息
#for parent,dirnames,filenames in os.walk(rootdir):
#	for dirname in  dirnames:
#		print "parent is:" + parent
#		print  "dirname is:" + dirname
#	for filename in filenames:
#		print "parent is:" + parent
#		print "filename is:" + filename
#		print "the full name of the file is:" + os.path.join(parent,filename) 

n = int(raw_input('Please enter the number: '))
#len = len(str(n))
print n

def addx(n):
	temp = 0
	while n > 0:
		temp = temp + 9*(10**(n-2))*(n-1)
		n = n - 1
	print n
	return temp 

print int(addx(3))

x = (n - (10**(len-1)-1)*len) + int(addx(len))
print x



