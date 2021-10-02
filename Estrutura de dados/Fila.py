# First in First out
# Push=add pop=del
class fila:
  def __init__ (self):
    self.fila= []
    self.lenfila= 0
  def push (self, e):
    self.fila.append (e)
    self.lenfila +=1
  def pop (self):
    if not self.vazia():
      self.fila.pop(0)
      self.lenfila-=1
  def vazia (self):
    if self.lenfila==0:
      return True
    else:
      return False
  def length (self):
    return self.lenfila
  def frist(self):
    if not self.empty():
      return self.fila[0]
  def all (self):
    return self.fila

q=fila()
q.push (1)
q.push (10)
print(q.vazia())
print (q.all())