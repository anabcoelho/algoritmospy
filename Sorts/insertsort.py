#Jeito 1
a1=[8,2,4,9,3,5,1]
for i in range(1,len(a1)):
   v = a1[i]
   j = i
   print(j)
   while (j > 0) and (a1[j-1] > v):
      a1[j] = a1[j-1]
      j = j - 1
   a1[j] = v
print(a1)

#jeito 2
a2=[3,1,2,5]
for i in range (len(a2)):
  x=a2[i]
  j=i-1
  for j in range(i-1,-1,-1):
    if (x<a2[j]):
      a2[j+1]=a2[j]
    else:
      break
    a2[j]=x
print(a2)