n,k=raw_input().split(' ')
n,k=int(n),int(k)
a=map(int,raw_input().split(' '))
b=a[:]
count=0
for i in range(0,n-1):
    sum=b[i]+b[i+1]
    if sum<k:
        b[i+1]=k-b[i]
        count+=b[i+1]-a[i+1]
print count
for i in range(0,n):
    print(b[i]),
