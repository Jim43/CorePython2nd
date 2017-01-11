#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

# get filename
while True:
    fname = input('Enter file name: ')
    if os.path.exists(fname):
        print('*** ERROR:' ,fname, 'already exists' )
    else:
        break

# get file content (text) lines
all = []
print ("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('sentence> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with NEWLINE line terminator
fobj = open(fname, 'w')
fobj.write('\n'.join(all))
fobj.close()
print ('DONE!')

#you can use s=os.getcwd() then print(s) to see where is your file
