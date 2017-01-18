def payment(startmoney,monthout):
    size=startmoney/monthout
    if int(size)==0:
        size+=1
    size=int(size)
    if startmoney%monthout==0:
        size+=1
    else:
        size+=2
    #comfirm the maxnum
    sapp=3-(len(str(startmoney))-len(str(int(startmoney))))
    mapp=3-(len(str(monthout))-len(str(int(monthout))))

    slen=len(str(startmoney))+sapp
    mlen=len(str(monthout))+mapp
    

    L1,L2,L3=len(str(size)),int(mlen)+1,int(slen)+1

    if L1<5:
        L1=5
    print('Amount Remaing')
    print('Pymt#','\t','Paid','\t','Balance')
    print('-'*L1,'-'*L2,'-'*L3)
    string=str(0)+'\t$'+str(0.00)+'\t$'+str(startmoney)
    print(string)
    for i in range(1,size):
        if startmoney>=monthout:
            startmoney-=monthout
        else:
            monthout=startmoney
            startmoney=0
        string=str(i)+'\t$'+str(round(monthout,2))+'\t$'+str(round(startmoney,2))
        print(string)

startmoney=float(input('Enter opening balance: '))
monthout=float(input('Enter monthly payment: '))
payment(startmoney,monthout)
