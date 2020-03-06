def Func(arr):
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            break
    Max=max(arr[i+1:])
    Min=min(arr[i+1:])
    
    print("Smallest number which is unsorted {}".format(Min))
    print("Maximum number which is unsorted {}".format(Max))
    arr.sort()
    print("their actual position {}".format(arr.index(Min)),arr.index(Max))
Func([1,2,3,6,7,4,0])