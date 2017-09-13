a=map(int,raw_input().split(' '))
a=sorted(a)
count=0
if (a[2]==a[0]):
    count=0
elif (a[2]==a[1]):
    count=1
else:
    count=2
print (3*a[2]-count)-sum(a)
