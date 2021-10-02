class pilha:
  def __init__(self):
    self.pilha=[]
    self.len_pilha=0
  def add (self, p):
    self.pilha.append(p)
    self.len_pilha+=1
  def remove (self):
    if not self.vazia():
      self.pilha.pop(self.len_pilha-1)
      len_pilha-=1
  def top(self):
    if not self.vazia():
      return self.pilha [-1]
    return None
  def vazia (self):
    if (self.len_pilha==0):
      return True
    return False
  def tamanho (self):
    return self.len_pilha
  def imprimir (self):
    return self.pilha

S=pilha()
S.add (1)
S.add (2)
S.add (3)
print (S.tamanho())
print(S.imprimir())