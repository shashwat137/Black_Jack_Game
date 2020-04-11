'''
Black Jack Game Project
Only Hit and Stand operations have been implemented here. and Split etc have not been included.
Only includes one Player and a Computer as Dealer in this case.
'''

import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11}

playing = True

class Card():

    '''
    Will instantiate each card with a suit and a rank
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

class Deck():

    '''
    Instantiate 52 unique cards and add them to a list. Also perform shuffle and deal operations.
    '''

    def __init__(self):
        self.deck = []          #Start with an empty deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(str(Card(suit, rank)))

    def __str__(self):
        return '{}'.format(self.deck)       #Just to help troubleshoot. Delete later

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()      #Return top value of deck and remove the same from the deck

class Hand():

    '''
    Will Hold the cards. May also Calculate Values of Cards from the dictionary. Also can adjust for ace value.
    '''

    def __init__(self):
        self.cards = []     #Start with empty list as with deck
        self.value = 0      #Start with zero value
        self.aces = 0       #Add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)                 #Will add the new card to hand. first deal the card in a function and then add same dealt card to hand.
        card_value = card.split()               #Will split the card name to get the value string.
        self.value += values[card_value[0]]     #Will add the card value from the dictionary.

    def adjust_for_ace(self, card):             #Run this in function when value of hand exceeds 21, else do not call.
        if card[:3] == 'Ace':                   #Aces adjusted by taking best possible value for them.
            self.aces += 1
        if self.aces > 1 or self.value > 21:
            while self.aces > 0:
                self.value -= 10
                self.aces -= 1
                if self.value <= 21:
                    break

class Chips():

    '''
    Keeps track of Players chips, bets and ongoing winnings.
    '''
    def __init__(self, total, bet):
        self.total = total
        self.bet = bet                   #bet amount per game of the match. check in the function where called if the bet amount is permitted.

    def __str__(self):                   #will give how much money does the player have. Used to find if the player can bet further
        return '{}'.format(self.total)

    def win_bet(self):
        self.total += self.bet          #Winner wins bet amount

    def lose_bet(self):
        self.total -= self.bet          #Loser loses te bet amount

#Now list of functions for repititive actions

def take_bet(total):        #Take a one-time total amount of player

    '''
    Take player's bets.
    '''

    while True:                 #Will keep asking for a valid input else it will move to next functionality
        bet = input("Please give a bet value to begin")
        try:
            bet = int(bet)
            break
        except:                 #In case of random input
            print('Please give a valid Integer Value')

    player = Chips(total, bet)

    return player           #Instance of Chips object is returned to called variable

def hit(deck, hand):

    '''
    Players can take hits until they bust. To be called everytime a player requests a hit, or if Dealer's hand is less than 17.
    Take Deck and Hand objects as arguments. Deal one card from the Deck and add it to Hand object. Also Checks for Aces if Hand Value exceeds 21.
    Does not return anything as function only changes objects.
    '''

    card = deck.deal()              #will return card on top of Deck as a string. Also the same card will be removed from the Deck
    hand.add_card(card)             #Will add the top card to Hand object.
    hand.adjust_for_ace(card)       #Will add Ace count if any, also will adjust Ace value when and however required.

    return

def hit_or_stand(deck, hand):

    '''
    Function Accepts Deck and Hand objects as arguments.
    If Player Hits, employ the hit() function.
    If Player Stands, set the global playing variable to false. This will stop the while loop running the game
    '''

    global playing
    while True:
        decision = input('Enter whether to "Hit" or to "Stand"\n')
        decision = decision.upper()
        if decision == 'HIT':
            hit(deck, hand)
            return decision
        elif decision == 'STAND':
            playing = False          #Will stop the game of given player
            return decision
        else:                               #Incase of random input
            print('Enter a valid input\nYou may Enter either "Hit" or "Stand"')
            continue

#Functions to display cards

def show_some(player, dealer):

    '''
    Player and Dealer will be hnd objects
    Dealer's first card is hidden and all cards of Player are visible.
    '''

    print("Player's cards are -")
    for card in player.cards:
        print('\t', card)

    print()
    print("Dealer's cards are -")
    for card in dealer.cards:
        print('\t', card)
    print()
    return

def show_all(player, dealer):

    '''
    Player and Dealer will be hand objects.
    At the end of hand, all cards are shown and each hand's total value is shown
    Must append hidden card to dealer's hand
    '''

    print("Player's cards are -")
    for card in player.cards:
        print('\t', card)
    print()
    print("Player's score is {}".format(player.value))
    print()
    print("Dealer's cards are -")
    for card in dealer.cards:
        print('\t', card)
    print()
    print("Dealer's score is {}".format(dealer.value))
    print()

    return

#Functions to handle end of game scenarios.

#Will ahve to initally check for blackjack for first two cards. Ace and ten. Check for both players. If dealer does not have a blackjack player wins, else its a push.

def player_busts(player_chips):

    '''
    If player exceeds 21 score, dealer automatically wins and no need for dealer to hit.
    Takes Player's Chips object as argument.
    '''

    print("Player has bust, Dealer wins")
    print("Player loses {} money\n".format(player_chips.bet))
    player_chips.lose_bet()

    return

def player_wins(player_chips):

    '''
    If player score exceeds dealer final score.
    Takes Player's Chips object as argument.
    '''

    print("Player has won. Player receives {} money\n".format(player_chips.bet))
    player_chips.win_bet()

    return

def dealer_busts(player_chips):

    '''
    If dealer exceeds 21, Player automatically wins irrespective of player score
    Takes Player's Chips object as argument.
    '''

    print('Dealer has bust, Player wins')
    print('Player has won. Player wins {} money\n'.format(player_chips.bet))
    player_chips.win_bet()

    return

def dealer_wins(player_chips):

    '''
    If dealer score exceeds player final score.
    Takes Player's chips object as argument.
    '''

    print("Player has lost, Dealer wins. Player loses {} money\n".format(player_chips.bet))
    player_chips.lose_bet()

    return

def push():

    '''
    No one wins as both have same sum and neither have busted.
    '''
    pass
    print("No one wins. It is a push\n")
    #No operation on bet since no one wins or loses.

    return

#Running of the game
print('\n\n')
print("Welcome to blackjack. One player may play with a computer dealer.\n")

while True:
    playing = True
    total = input('Please Enter your total amount\n')
    try:
        total = int(total)
        break
    except:
        print('Please enter a valid integer\n')
        continue

while True:

    #Create Deck and shuffle the cards
    deck = Deck()
    deck.shuffle()

    #Deal two cards to player and Dealer. Keep one card of Dealer hidden.
    player = Hand()
    dealer = Hand()

    card1 = deck.deal()
    player.add_card(card1)
    player.adjust_for_ace(card1)
    card2 = deck.deal()
    player.add_card(card2)
    player.adjust_for_ace(card2)

    card1 = deck.deal()
    dealer.add_card(card1)
    dealer.adjust_for_ace(card1)
    hidden_card = deck.deal()

    #Setup Player's chips.
    while True:
        bet = input('Please Enter your bet amount for the game\n')
        try:
            bet = int(bet)
            if bet > total:
                print("\nBet amount cannot exceed total money of player\nPlease enter a valid bet amount\n")
                continue
            else:
                print()
                break
        except:
            print('\nPlease enter a valid integer\n')
            continue
    player_chips = Chips(total, bet)

    #Show cards. But keep one dealer card hidden.
    show_some(player, dealer)

    #Check if black Jack has taken place. In that case, Game has ended, only check for winner.
    black = False
    jack = False
    for card in player.cards:
        card_value = card.split()
        if card_value[:3] == 'Ace':
            black = True
        elif card_value[:3] == 'Ten':
            jack = True
        else:
            pass
    if black and jack:
        card = dealer.cards[0]
        card_value = card.split()
        if card_value[:3] == 'Ace' or card_value[:3] == 'Ten':
            dealer.add_card(hidden_card)
            dealer.adjust_for_ace(hidden_card)
            d1 = False
            d2 = False
            for card in dealer.cards:
                ### Check if we have combinatiion of blackjack even in dealer.
                card_value = card.split()
                if card_value[:3] == 'Ace':
                    d1 = True
                elif card_value[:3] == 'Ten':
                    d2 = True
                else:
                    pass
            if d1 and d2:
                push()
            else:
                player_wins(player_chips)
                print('Player has got a Blackjack\n')
            playing = False
        else:
            player_wins(player_chips)
            print('Player got a Blackjack\n')
            playing = False

        #Now ask if you want to play again.
        while True:
            game = input("Enter 'y' if you want to play again, else enter 'n'\n")
            game = game.lower()
            if game == 'y' or game == 'n':
                break
            else:
                print("\nEnter a valid 'y' or 'n' only\n")
                continue
        if game == 'y':
            playing = True
            continue
        else:
            break

    #For player only. Not dealer
    bust = False
    while playing:

        while player.value <= 21 and playing:
            #Prompt for player to hit or stand
            decision = hit_or_stand(deck, player)

            if decision == 'HIT' :
                #Show cards but keep one dealer card hidden
                show_some(player, dealer)

        #If player's hand exceeds 21, run player_busts() and exit out of loop.
        if player.value > 21:
            player_busts(player_chips)
            bust = True
            break

    #If player hasn't been busted, play Dealer's Hand until Dealer reaches 17.
    if not bust:
        print('Dealer is taking hits\n')
        dealer.add_card(hidden_card)
        dealer.adjust_for_ace(hidden_card)
        while dealer.value < 17:
            hit(deck, dealer)

        #Show all cards.
        show_all(player, dealer)

        #Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player_chips)
        elif player.value > dealer.value:
            player_wins(player_chips)
        elif player.value < dealer.value:
            dealer_wins(player_chips)
        else:
            push()


    #Inform player of their chips total.
    print('{} is the total chips now held by player\n'.format(str(player_chips)))

    #Ask to play again.
    while True:
        game = input("Enter 'y' if you want to play again, else enter 'n'\n")
        game = game.lower()
        if game == 'y' or game == 'n':
            break
        else:
            print("\nEnter a valid 'y' or 'n' only\n")
            continue
    if game == 'y' and player_chips.total > 0:
        playing = True
        total = player_chips.total
        continue
    elif game == 'n':
        print("See you Later")
        break
    else:
        print("Not enough funds to continue playing\n")
        print("Better Luck Next Time")
        break
