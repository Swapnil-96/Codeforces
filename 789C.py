n=int(raw_input())
a=map(int,raw_input().split(' '))
b=[]
for i in range(0,n-1):
    b.append(abs(a[i]-a[i+1]))
max=0
for j in range(0,n-1):
    sum=0
    for k in range(j,n-1):
        sum+=b[k]*((-1)**(k-j))
        if sum>max:
            max=sum
print max
        
    
    