def Func(a,num):
    a.sort()
    p=[]
    mid=num//2
    for x in range(len(a)):
        if a[x]>mid:
            break
    i=x-1
    while num-a[i]<=a[-1]:
        if num-a[i] in a[i+1:len(a)]:
            p.append((a[i],num-a[i]))
        i=i-1
            
    print(p)
Func([1,2,3,4,6,12,9],18)