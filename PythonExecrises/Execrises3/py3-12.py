#!usr/bin/env python

import os

while True:
    select=int(input('1.makeTextFile\n2.readTextFile\n3.quit\n'))
    if select==1:
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
    elif select==2:
                     # get filename
                    fname = input('Enter file name: ')
                    print()

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
    elif select==3:
                     break
    else:
                     print('Try Again')
