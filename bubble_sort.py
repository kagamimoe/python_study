#! /usr/bin/env python
#coding=utf-8
#bubble sort 

l = [1,9,4,88,35,26]

def bubblesort(list):
    for i in range(1,len(list)):
        for j in range(1,len(list)):
            if int(list[j-1])>int(list[j]):
                list[j-1],list[j] = list[j],list[j-1]
    return list

print  bubblesort(l)