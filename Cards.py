colors = ["hearts", "diamonds", "spades", "clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ] #TODO joker
import random

class Card:

    def __init__(self, value, color):

        self.value = value #1-14
        self.color = color #Hearts Diamonds Spades Clubs

    def __repr__(self):
        return "{} of {}".format(self.value,self.color)

    def __eq__(self, other): # we gaan kleur negeren anders krijgen we raar gedrag

        if self.value == other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if values.index(self.value)>values.index(other.value):
            return True

        return False

    def __lt__(self, other):
        if values.index(self.value)<values.index(other.value):
            return True

        return False

    def __getitem__(self, item):
        if item == 0:
            return self.value
        elif item == 1:
            return self.color

    def isRed(self):
        if self.color in colors[:-2]:
            return True
        else:
            return False

    def isBlack(self):
        return not self.isRed()

    def fullEqual(self,other):
        if self.value == other.value and self.color == other.color:
            return True
        else:
            return False




class Deck:

    def __init__(self,cards = []):

        self.cards = cards
        if self.cards == []:
            self.generate()
        self.colors = []

    def generate(self,):
       for value in values:
            for color in colors:
                self.cards += [Card(value,color)]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def add(self,card):
        self.cards += [card]

    def sort(self,method = "values"):
        if method == "colors":
            self.cards.sort()
            self.cards.sort(key=lambda card: colors.index(card[1]))
        elif method == "values":
            self.cards.sort()

    def __getitem__(self, item):
        print(item)
        return self.cards[item]

    def __repr__(self):
        return str(self.cards)


if __name__ == "__main__":


    d = Deck()

    d.generate()
    print(d[1]==d[2])
    d.shuffle()
    d.sort("values")
    print(d.cards)