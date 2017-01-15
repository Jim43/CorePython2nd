#inPython3,there is no maxint in module sys
def numinfo():
    import sys
    maxlong=sys.maxsize
    minlong=-maxlong
    maxfloat=sys.float_info.max
    minfloat=-maxfloat
    print('maxlong,minlong,maxfloat,minfloat is\n',maxlong,minlong,maxfloat,minfloat)

numinfo()
