def findOdd(Range):
    odd=[]
    for i in range(Range):
        if i%2!=0:
            odd.append(i)
    return odd

def findeven(Range):
    even=[]
    for i in range(Range):
        if i%2==0:
            even.append(i)
    return even

#判断一个函数是不是能被整除就是看取余的结果是不是0
def divOrNot(a,b):
    if a%b==0:
        return True
    elif a%b!=0:
        return False

Range=int(input('Please input a top range\n'))

odd=findOdd(Range)
even=findeven(Range)

for oddNum in odd:
    print(oddNum,end=' ')

print('\n')
for evenNum in even:
    print(evenNum,end=' ')
print('\n')

a=int(input('input the first number\n'))
b=int(input('input the second number\n'))

flag=divOrNot(a,b)

if flag:
    print('It can be divided')
else:
    print('It can not be divided')
