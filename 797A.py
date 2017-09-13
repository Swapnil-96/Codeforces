def primefac(n):
    list=[]
    while (n%2 == 0):
        list.append(2)
        n = n/2
    for i in range(3,int(n**0.5+1),2):
        while (n%i == 0):
            list.append(i)
            n = n/i
    if (n > 2):
        list.append(n)
    return list
n,k=map(int,raw_input().split(' '))
x=primefac(n)
ans=1
if len(x)<k:
    print("-1")
else:
    for j in range(0,k-1):
        print x[j],
    for j in range(k-1,len(x)):
        ans=ans*x[j]
    if ans!=1:
        print ans