def Calculator(str1):
    operator=['+','-','*','/','%','**']
    s=[1]#make sure the length is 1 at first
    s1=[]
    i=0
    while len(s)==1:
        #print(operator[i])
        s=str1.split(operator[i])
        #print(s)
        i+=1
    i-=1
    for a in range(2):
        s1.append(float(s[a]))
    #print(s1)
    print(operator[i])
    if operator[i]=='+':
        result=s1[0]+s1[1]
    elif operator[i]=='-':
        result=s1[0]-s1[1]
    elif operator[i]=='*':
        result=s1[0]*s1[1]
    elif operator[i]=='/':
        result=s1[0]/s1[1]
    elif operator[i]=='%':
        result=s1[0]%s1[1]
    elif operator[i]=='**':
        result=s1[0]**s1[1]
    else:
        result=False
    return result

str1=input('Input what you want to calculate.eg:1+2(support with[+,-,*,/,%,**(pow)]\n')
result=Calculator(str1)
print('Result is ',str(result))
