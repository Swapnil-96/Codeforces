a,b=raw_input().split(' ')
a,b=int(a),int(b)
a=int(str(a)[-1])
count=0
for i in range(1,10):
    if ((a*i%10==0) or ((a*i-b)%10==0)):
        print i
        break
    