class Hash(object):
    head = [None] * 10

    def padraonumero(self, chave):
        if len(chave) == 0:
            return 0
        else:
            last = chave[-1]
            lastnumero = 0
            if last == "A":
                lastnumero = 1
            elif last == "C":
                lastnumero = 2
            elif last == "G":
                lastnumero = 3
            elif last == "T":
                lastnumero = 4
            prefixo = chave[0:-1]
            return self.padraonumero(prefixo) * 4 + lastnumero

    def insert(self, chave):
        i = self.padraonumero(chave)
        while len(self.head) <= i:
            self.head.append(None)
        self.head[i] = chave
        return chave

    def remove(self, chave):  # chave/none
        y = self.padraonumero(chave)
        del self.head[y]
        return ("del", chave)

    def search(self, chave):  # true/false
        z = len(self.head)
        print(z)
        w = z - 1
        print(w)
        q = 0
        while q < z:
            if chave == self.head[q]:
                return True
            q += 1
        return False


x = Hash()
print(x.insert("AA"))
print(x.insert("AC"))
print(x.insert("AGT"))
print(x.insert("AT"))

print(x.remove("AA"))
print(x.search("AA"))