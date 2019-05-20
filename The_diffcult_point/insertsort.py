# coding=utf-8
alist = [3,8,2,9,13,0,5,7]

def InsertSort(alist):
    for i in range(1,len(alist)):
        #如果当前数字比前一个小
        if alist[i]<alist[i-1]:
            temp=alist[i]
            last=0
            for j in range(i-1,-1,-1):
                if alist[j]>temp:
                    alist[j+1]=alist[j]
                else:
                    last=j+1
                    break

            alist[last]=temp

InsertSort(alist)
print(alist)