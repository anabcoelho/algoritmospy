# double end queue
class deck:
    def __init__(self):
        self.deck = []
        self.lendeck = 0

    # pushs
    def pushfrist(self, e):
        self.deck.insert(0, e)
        self.lendeck += 1

    def pushend(self, e):
        self.deck.append(e)
        self.lendeck += 1

    # Pops
    def popend(self):
        if not self.lendeck == 0:
            self.deck.pop(-1)
            self.lendeck -= 1

    def popfrist(self):
        if not self.lendeck == 0:
            self.deck.pop(0)
            self.lendeck -= 1

    def empty(self):
        if self.lendeck == 0:
            return True
        return False

    def lengh(self):
        return self.lendeck

    def alldeck(self):
        return self.deck


d = deck()
d.pushfrist(10)
d.pushfrist(8)
d.pushend(2)
d.popfrist()
print(d.alldeck())

