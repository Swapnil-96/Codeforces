n,m,k=raw_input().split(' ')
n,m,k=int(n),int(m),int(k)
m=m-1
a=map(int,raw_input().split(' '))
min=n
new=0
for i in range(0,n):
    if a[i]!=0 and a[i]<=k:
        new=abs(m-i)
        if new<min:
            min=10*new
print min
