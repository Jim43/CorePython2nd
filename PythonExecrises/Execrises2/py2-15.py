a=int(input('请输入第1个数\n'))
b=int(input('请输入第2个数\n'))
c=int(input('请输入第3个数\n'))
d=max(a,b,c)
e=min(a,b,c)
if a!=d and a!=e:
    f=a
elif b!=d and b!=e:
    f=b
else:
    f=c
print(e,f,d)
print(d,f,e)
