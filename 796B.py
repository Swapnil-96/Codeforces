n,m,k=raw_input().split(' ')
n,m,k=int(n),int(m),int(k)
h=map(int,raw_input().split(' '))
print h
h=set(h)
print h
b=1
flag=1
if 1 in h:
    for i in range(0,k):
        ui,vi=raw_input().split(' ')
else:
    for i in range(0,k):
        ui,vi=raw_input().split(' ')
        ui,vi=int(ui),int(vi)
        if flag==1:
            if ui==b:
                b=vi
                if b in h:
                    flag=0
            elif vi==b:
                b=ui
                if b in h:
                    flag=0
print b  
        