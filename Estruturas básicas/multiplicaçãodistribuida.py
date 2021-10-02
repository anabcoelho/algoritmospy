p=(4,2,0,-1)
q=(2,-1,2,0)
r=[]
N=len(p)
for i in range (2*N-1):
  r.append(0)
print(r)
for i in range(N):
  for j in range(N):
     r[i+j]= r[i+j] + p[i] * q[j]
print(r)