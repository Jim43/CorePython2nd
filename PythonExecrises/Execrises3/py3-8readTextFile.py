#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter file name: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:#这里推荐使用关键字as而使用，而且，在python3好像不能这样用 这个e是一个错误实类
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print (eachLine)
    fobj.close()
