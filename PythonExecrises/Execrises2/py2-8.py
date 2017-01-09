alist=[]
blist=[]
atuple=()
print('请输入五个数字')
for a in range(5):
    b=int(input())
    alist.append(b)#list.append是为list增加元素的方法
print('请再输入不一样的五个数字')
for a in range(5):
    b=int(input())
    blist.append(b)
atuple=tuple(blist)#tuple一旦被创造无法修改，这里采用转换的方法
a=0
b=0
Sum1=0
Sum2=0
#去掉下面6个注释就是通过while实现
#while a<len(alist):
    #Sum1+=alist[a]
    #a+=1
#while b<len(atuple):
    #Sum2+=atuple[b]
    #b+=1
for c in alist:
    a+=c
for d in atuple:
    b+=d
print(a,b)
