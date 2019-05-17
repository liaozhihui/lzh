# coding=utf-8


alist = [3,8,2,9,13,0,5,7]


def quicksort(arr,start,end):
    if start<end:
        stard=arr[start]
        low=start
        high=end
        while low<high:
            while low<high and arr[high]>=stard:
                high-=1
            arr[low]=arr[high]
            while low<high and arr[low]<=stard:
                low+=1
            arr[high]=arr[low]
        arr[high]=stard
        quicksort(arr,0,low)
        quicksort(arr,low+1,end)

quicksort(alist,0,len(alist)-1)
print(alist)
