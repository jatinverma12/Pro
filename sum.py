
def Func(a,num):
    a.sort()
    p=[]
    mid=num//2
    for x in range(len(a)):
        if a[x]>mid:
            break
    i=x-1
    while num-a[i]<=a[-1] and i>=0:
        if num-a[i] in a[i+1:len(a)]:
            p.append((a[i],num-a[i]))
        i=i-1
    
    if(len(p)):
        print(p)
    else:
        print("sum is not available")

    
b=list(map(int, input("Enter the numbers").strip().split()))
n=int(input("Enter the desired sum"))
Func(b,n)