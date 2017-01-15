def payment(startmoney,monthout):
    size=float(startmoney)/monthout
    if int(size)==0:
        size+=1
    size=int(size)
    #comfirm the maxnum
    sapp=3-(len(str(startmoney))-len(str(int(startmoney))))
    mapp=3-(len(str(monthout))-len(str(int(monthout))))

    slen=str(len(str(startmoney))+sapp)
    mlen=str(len(str(monthout))+mapp)

    L1,L2,L3=len(str(size)),int(mlen)+1,int(slen)+1

    if L1<5:
        L1=5
    print('Amount Remaing')
    print('Pymt#'.center(L1),'\t','Paid'.center(L2),'\t','Balance'.center(L3))
    print('-'*L1,'-'*L2,'-'*L3)
    string=str(0)+'\t$'+mlen+str(0.00)+'\t$'+slen+str(startmoney)
    print(string)
    for i in range(1,size+1):
        if startmoney>=monthout:
            startmoney-=monthout
        else:
            monthout=startmoney
            startmoney=0
        string=str(i)+'\t$'+mlen+str(monthout)+'\t$'+slen+str(startmoney)
        print(string)

payment(100,16.13)
