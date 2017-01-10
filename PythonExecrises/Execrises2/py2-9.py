alist=[]
sum1=0

print("请输入五个数（用回车隔开）")
for a in range(5):
    b=int(input())
    alist.append(b)

a=0

while a<len(alist):
    sum1+=alist[a]
    a+=1

#for a in alist:
    #sum1+=a

print(float(sum1)/5)
