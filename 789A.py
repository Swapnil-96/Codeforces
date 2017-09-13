n,k=raw_input().split(' ')
a=1
n,k=int(n),int(k)
w=map(int,raw_input().split(' '))
ans=0
for i in range(0,n):
    if w[i]%k==0:
        ans+=w[i]/k
    else:
        ans+=w[i]/k+1
print (ans+1)/2