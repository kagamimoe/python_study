#! /usr/bin/env python
#coding=utf-8
# list method

# append : use for add new item in the end
lst = [1,2,3]
lst.append(4)
print lst

# count: : count for the item
print ['1','2','2','3'].count('2')
x = [[1,2],1,1,[2,1,[1,2]]]
print x.count(1)
print x.count([1,2])

# extend : use for join 
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print a

# index: find index of item
a = [1,2,3,4,5,6]
print 'index of 3 is '+ str(a.index(3))

# insert: insert a item into list
num = [1,2,3,4,5,6]
num.insert(3,123)
print num

# pop: del the last item in list and return it
num = [1,2,3,4,5]
print num.pop()
print num

# remove: remove a item from list
x = [1,2,3,4,5,6]
x.remove(3)
print x

# reverse: make the list reverse
x = [1,2,3]
x.reverse()
print x

# sort: sort the list
x = [1,5,7,3,2,6]
#x.sort()
print x
# not y = x
y = sorted(x)
#y = x[:]
y.sort()
print y
print x