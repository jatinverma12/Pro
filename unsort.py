def Func(arr):
    f=0
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            f=1
            break
    Max=max(arr[i+1:])
    Min=min(arr[i+1:])
    if f==0:
        print("list is sorted")
    else:
        
        print("Smallest number which is unsorted {}".format(Min))
        print("Maximum number which is unsorted {}".format(Max))
        arr.sort()
        print("their actual position {}".format(arr.index(Min)),arr.index(Max))



a=list(map(int, input("enter numbers").strip().split()))
Func(a)