def generateN (numN,numn):
    import random
    Nlist=[]
    FinalList=[]#what we want in final
    i=0

    for i in range(numN):
        Nlist.append(random.randint(0,numn))#generate the list

    selectNum=random.randint(0,numN)#select how many numbers from above list

    #print(Nlist)#test the Nilst
    #print(selectNum)

    i=0

    while i < selectNum:
        randomChoice=random.randint(0,numN-1)
        randNum=randomChoice
        randomChoice=random.randint(0,numN-1)#minimun the repeat num
        if randomChoice !=  randNum:
            FinalList.append(Nlist[randomChoice])
            i+=1
        else:
            randomChoice=random.randint(0,numN-1)
    return FinalList

List=generateN(100,2**31-1)

for num in List:
    print(num,'\n')
