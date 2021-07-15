#!/usr/bin/env python
# coding: utf-8

# In[164]:


# CARD
# SUIT,RANK,VALUE

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# In[165]:


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# In[166]:


three_of_clubs = Card("Clubs", "Three")

# In[167]:


three_of_clubs.value

# In[168]:


three_of_clubs.rank

# In[169]:


three_of_clubs.suit

# In[170]:


two_hearts = Card("Hearts", "Two")

# In[171]:


two_hearts

# In[172]:


print(two_hearts)

# In[173]:


values[two_hearts.rank]

# In[174]:


two_hearts.value < three_of_clubs.value


# In[175]:


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# In[176]:


new_deck = Deck()

# In[177]:


new_deck.shuffle()

# In[178]:


mycard = new_deck.deal_one()

# In[179]:


print(mycard)


# In[180]:


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[181]:


new_player = Player("Jose")

# In[182]:


print(new_player)

# In[183]:


new_player.add_cards(mycard)

# In[184]:


print(new_player)

# In[185]:


print(new_player.all_cards[0])

# In[186]:


new_player.add_cards([mycard, mycard, mycard])

# In[187]:


print(new_player)

# In[188]:


new_player.remove_one()

# In[189]:


print(new_player)

# In[221]:


# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# In[222]:


game_on = True

# In[223]:


round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at_war

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        if player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER One WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

# In[ ]:


# In[ ]:


# In[ ]:




