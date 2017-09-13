n=int(raw_input())
count=0
for i in range(0,n):
    s=raw_input()
    if s=="Tetrahedron":
        count+=4
    elif s=="Cube":
        count+=6
    elif s=="Octahedron":
        count+=8
    elif s=="Dodecahedron":
        count+=12
    else:
        count+=20
print count    