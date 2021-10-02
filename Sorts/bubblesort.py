a=[3,2,45,6,7,4,32]
N=len(a)
for i in range(N-1, 0, -1):
  for j in range(1, i+1):
     if a[j-1] > a[j]:
        b = a[j-1]
        a[j-1] = a[j]
        a[j] = b
print(a)