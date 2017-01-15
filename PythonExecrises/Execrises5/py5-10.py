def FtransformC(F):
    #F-Fahrenhrit C-Celsius
    F=float(F)
    C=(F-32)*(5/9)
    return C

F=input('Please input a Fahrenhrit temperature\n')
C=FtransformC(F)
print('The Celsius temperature is ',C)
