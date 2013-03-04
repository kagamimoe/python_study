#!/usr/bin/python
# Filename: using_file.py

import os

poem = '''\
acgskdfjksd
sdfsdf
sdf 
        sdfsdf
'''

f = file('poem.txt', 'w')  # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = file('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,
f.close()

e = file('sql.txt')
while True:
    line = e.readline()
    if len(line) == 0:
        break
    print line,
e.close()

s = 'o2YPUrRZr6z3COflRjvdWGlIeWa?/ziuq/moc.oaboat.deu//:ptthWqeRTe1'
rstr = s[::-1]
print rstr

print os.name