class Node:  # Nó da lista (local de inserção de um valor em uma lista)
    key = 0
    next = None

    def __init__(self, k):
        self.key = k
        self.next = None


class List:  # Cria uma lista
    head = None
    count = 0

    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, v):  # Função para a adição de um valor de uma lista
        n = self.head
        while n.next != None:
            n = n.next  # Pula para o valor do próximo nó da lista
        a = Node(v)  # valor do nó
        n.next = a

    def __str__(self):  # Função para o print a lista
        n = self.head
        l = ""  # String vazia
        while n.next != None:
            l = l + str(n.key) + ","  # Concatenação entre a string vazia e o valor do nó
            n = n.next
        l = l + str(n.key)  # Concatenação do último nó
        return (l)

    def get(self, v):  # Função que retorna a posição de um certo elemento
        i = 0
        g = self.head
        while g.next != None:
            if g.key == v:
                return (i)
                g = g.next
            i = i + 1
        return (-1)


x = Node(6)  # valor de k da função __init__

y = List()
y.head = x

y.add(7)
y.add(9)  # valor de v da função add
y.add(4)

print(y.get(9))

print(y)  # print da lista