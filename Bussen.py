import Cards


def roodOfZwart(card):
    while True:
        inp = input("Is de kaart Rood of Zwart?").lower()
        if inp == "rood" or inp == "zwart":
            break

    if inp == "rood":
        if card.isRed():
            return True
        else:
            return False
    if inp == "zwart":
        if card.isBlack():
            return True
        else:
            return False

def hogerOfLager(firstCard, secondCard):
    while True:
        inp = input("Is de volgende kaart Hoger of Lager dan je eerste kaart?").lower()
        if inp == "hoger" or inp == "lager":
            break

    if inp == "hoger":
        if secondCard > firstCard:
            return True
        else:
            return False
    if inp == "lager":
        if secondCard < firstCard:
            return True
        else:
            return False

def binnenOfBuiten(firstCard,secondCard,ThirdCard):
    while True:
        inp = input("Ligt de waarde van de volgende kaart binnen of buiten de waarde van de kaarten die je al hebt?").lower()
        if inp == "binnen" or inp == "buiten":
            break


    cardvalues = [firstCard.value,secondCard.value]

    if ThirdCard.value in cardvalues: #als de nieuwe kaart gelijk is aan een van de andere kaarten ben je sws genaaid
        return False


    cards = [firstCard,secondCard,ThirdCard]
    cards.sort()
    print(cards.index(ThirdCard))
    if cards.index(ThirdCard) == 1: # want [0] [1] [2] --> [1] is de middelse
        result = "binnen"
    else:
        result = "buiten"

    if result == inp:
        return True
    else:
        return False

def hebJeHemAl(hand): #TODO disco, also saau by dus misschien ff aanpassen
    while True:
        inp = input("Heb je de kleur van de volgende kaart op dit moment al in je hand?").lower()
        if inp == "ja" or inp == "nee":
            break

    colors = []
    for card in hand[:-1]:
        colors+=[card.color]

    if hand[3].color in colors:
        result = "ja"
    else:
        result = "nee"

    if result == inp:
        return True
    else:
        return False

def bussen(length = 5): #Todo wat do als het deck op is
    deck = Cards.Deck()
    deck.shuffle()

    bus = [deck.draw() for card in range(length) ]

    position = length-1
    while position>=0:


        for card in bus:
            if bus[position].fullEqual(card):
                print(">", end="")
            print("| {} | ".format(card), end=" ")
        print()
        while True:
            inp = input("Is de kaart die getrokken wordt Hoger of Lager dan {}?".format(bus[position])).lower()
            if inp == "hoger" or inp == "lager":
                break
        newCard = deck.draw()
        if newCard > bus[position]:
            result = "hoger"
        elif newCard < bus[position]:
            result = "lager"
        else:
            result = "gelijk"


        print("Het was: {}".format(newCard))
        bus[position] = newCard
        if result == inp:
            print("Correct! Nog {} kaart(en).".format(position))
            position-=1
        else:
            print("Helaas... {} slok(ken)!".format(length-position))
            position = length-1

    print("Gefeliciteerd! Je hebt de bus uitgespeeld!")




if __name__ == "__main__":
    # deck = Cards.Deck()
    # deck.shuffle()
    # hand = []
    # hand += [deck.draw()]
    # print(roodOfZwart(hand[0]),hand[0])
    # hand += [deck.draw()]
    # print((hogerOfLager(hand[0],hand[1])),hand)
    # hand += [deck.draw()]
    # print(binnenOfBuiten(hand[0],hand[1],hand[2]),hand)
    # hand += [deck.draw()]
    # print(hand)
    # print(hebJeHemAl(hand),hand)
    #
    # #Piramidetijd
    # slokkendict = {}
    #
    # for layer in range(1,6):
    #     print()
    #     print(" " * (6 - layer), end="")
    #     for cardslot in range(layer):
    #         card = deck.draw()
    #         print("{}{}".format(card.value,card.color), end=" ")
    #         if card.value in [card.value for card in hand]:
    #             naam = input("Je mag {} slok(ken) uitdelen! Voer een naam in:".format(layer))
    #             if naam in slokkendict.keys():
    #                 slokkendict[naam] += layer
    #             else:
    #                 slokkendict[naam] = layer
    #
    # print(slokkendict)
    bussen()
