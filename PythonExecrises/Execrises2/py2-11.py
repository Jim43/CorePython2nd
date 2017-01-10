a=int(input('请选择如下功能(输入其功能编号)\n(1)取五个数之和\n(2)取五个数的平均值\n(3)Exit\n'))
if a==1:
    alist=[]
    print('请输入五个数字（用回车隔开）')
    for a in range(5):
        b=int(input())
        alist.append(b)
    a=0
    for c in alist:
        a+=c
    print(a)
elif a==2:
    alist=[]
    sum1=0
    print("请输入五个数（用回车隔开）")
    for a in range(5):
        b=int(input())
        alist.append(b)
    for a in alist:
        sum1+=a
    print(float(sum1)/5)
else:#注意到X不是数字所以int不能将其转换这里用3代替它
    exit
