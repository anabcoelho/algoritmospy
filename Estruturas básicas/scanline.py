x=[1, 4, -3, -3, 1, -2, 3, -1, 4, -1, -4, -3, 0, 1]
d=0
m=0
l=0
for i in range(len(x)):
   d=d+x[i]
   if d<=0:
     d=0
     l=l+1
   elif d>m:
     m=d
     f=i+1
     l=l+1
print (m,l,f)