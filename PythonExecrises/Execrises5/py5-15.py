def gcd(num1,num2):
    minNum=num1
    if num2<num1:
        num1=num2
        num2=minNum
    num1cd=[]
    for i in range(1,num1+1):
        if num1%i==0:
            num1cd.append(i)
    lens=len(num1cd)
    for j in range(lens):
        if num2%num1cd[(lens-j-1)]==0:
            num2cd=num1cd[(lens-j-1)]
            break
    return num2cd

def lcm(num1,num2):
    gcdNum=gcd(num1,num2)
    n1=num1/gcdNum
    n2=num2/gcdNum
    lcmNum=n1*n2*gcdNum
    return lcmNum

print("Find two number's gcd and lcm program\n")

num=[]

for i in range(2):
    number=input('Please input the number\n')
    num.append(number)
gcdNum=gcd(int(num[0]),int(num[1]))
lcmNum=lcm(int(num[0]),int(num[1]))

print('The gcd Number and lcm number of ',num[0],' and ',num[1],' are ',gcdNum,' ',lcmNum)
