#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

# get filename
fname = input('Enter file name: ')
try:
    fjob=open(fname, 'r')
except IOError as e:
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
else:
   print('*** ERROR:' ,fname, 'already exists' )

#you can use s=os.getcwd() then print(s) to see where is your file
