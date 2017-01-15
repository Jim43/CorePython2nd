def MoneyChange(money):
    Money=float(money)*100
    coin=[]#store coin nums

    cent4=Money//25#cent25
    coin.append(int(cent4))

    cent3=(Money-25*cent4)//10#cent10
    coin.append(int(cent3))

    cent2=(Money-25*cent4-10*cent3)//5#cent5
    coin.append(int(cent2))

    cent1=Money-25*cent4-10*cent3-5*cent2#cnet1
    coin.append(int(cent1))

    return coin

money=input('Please input a money(in dollar ) less than 1$\n')

coin=MoneyChange(money)

print('You will have ',coin[0],' 25cents ',coin[1],' 10cents ',coin[2],' 5cents ',coin[3],' cent\n')
