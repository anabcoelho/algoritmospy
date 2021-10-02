def pot(base,exp):
  if (exp==0):
    return 1
  else:
    return base * pot (base,exp-1)
print pot(2,3)   