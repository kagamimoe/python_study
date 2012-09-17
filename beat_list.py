#! /usr/bin/env python
#coding=utf-8
score = [12,34,56,78,90]
newscore = int(raw_input('Please enter your score:'))
score.append(newscore)
score.sort()
print score
index = score.index(newscore)
print 'you are in ' + str(index)
indexpercert = float(float((len(score))-float((index+2)))/float(len(score)-1)*100)
print 'You beat ' + str(indexpercert) + '% people'