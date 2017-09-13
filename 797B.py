n=int(raw_input())
a=map(int,raw_input().split(' '))
even=[]
podd=[]
nodd=[]
s=0
for i in range(0,n):
    if a[i]%2==0 and a[i]>0:
        even.append(a[i])
    elif a[i]%2!=0 and a[i]>0:
        podd.append(a[i])
    elif a[i]%2!=0 and a[i]<0:
        nodd.append(a[i])
s+=sum(even)
s+=sum(podd)
if len(podd)==0:
    s+=max(nodd)
elif len(podd)%2==0:
    if len(nodd)==0:
        s-=min(podd)
    else:
        x=max(nodd)
        y=min(podd)+x
        if y<0:
            s-=min(podd)
        else:
            s+=x
print int(s)
    
