class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:

            # cria o novo nÃ³
            node = Node(label)

            # verifica se a lista estÃ¡ vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # inserÃ§Ã£o no inÃ­cio
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserÃ§Ã£o ao final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserÃ§Ã£o no meio
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:

                        if curr_index == index:
                            # seta o curr_node como o prÃ³ximo do nÃ³
                            node.setNext(curr_node)
                            # seta o node como o prÃ³ximo do prev_nodes
                            prev_node.setNext(node)

                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):

        if not self.empty() and index >= 0 and index < self.len_list:

            flag_remove = False

            if self.first.getNext() == None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do inÃ­cio, mas possui mais de 1 elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                '''
                    Se chegou aqui Ã© porque a lista possui mais
                    de 1 elemento e a remoÃ§Ã£o nÃ£o Ã© no inÃ­cio
                '''

                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:

                    if index == curr_index:
                        # o prÃ³ximo do anterior aponta para o prÃ³ximo do nÃ³ corrente
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list -= 1

    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):

        curr_node = self.first

        while curr_node != None:
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNext()
        print('')


lista = LinkedList()

# teste inserÃ§Ã£o
lista.push('Marcos', 0)  # inserÃ§Ã£o no inÃ­cio
lista.show()
lista.push('Maria', 1)  # inserÃ§Ã£o no final
lista.show()
lista.push('Yankee', 0)  # inserÃ§Ã£o no inÃ­cio
lista.show()
lista.push('Catarina', 2)  # inserÃ§Ã£o no meio
lista.show()
lista.push('Lilica', 4)  # inserÃ§Ã£o no final
lista.show()
lista.push('Sara', 2)  # inserÃ§Ã£o no meio
lista.show()
print('Tamanho da lista: %d\n' % lista.length())

# teste remoÃ§Ã£o
lista.pop(0)  # remoÃ§Ã£o do inÃ­cio
lista.show()
lista.pop(2)  # remoÃ§Ã£o do meio
lista.show()
lista.pop(3)  # remoÃ§Ã£o do final
lista.show()
print('Tamanho da lista: %d\n' % lista.length())