# a, b, x, y, z são inteiros
def mul(a,b):
  x=a
  y=b
  z= 0
  print(x,y,z)
  while y > 0:
   if (y % 2) == 0:
      y= y / 2
      x= 2*x
   else:
      y= y - 1
      z= z + x
   print(x,y,z)
  return z
print (mul(13,5))