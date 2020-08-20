import random
class Card:
    def __init__(self, color, value, prev_card=None, next_card=None):
        self.color = color
        self.value = value
        self.next_card = next_card
        self.prev_card = prev_card

    # getters
    def get_color(self):
        return self.color
    def get_value(self):
        return self.value
    def next_card(self):
        return self.next_card

    # setters
    def set_color(self, color):
        self.color = color
    def set_value(self, value):
        self.value = value
    def set_next(self, card):
        self.next_card = next_card
    # print
    def return_card(self):
        return f"{self.color}-{self.value}"

class Deck:
    def __init__(self,length, numOfCards=0):
        self.length = length
        self.numOfCards = numOfCards
        self.top = None
        self.isEmpty = True
    
    def push(self, card):
        if self.length == self.numOfCards:
            print("this operation exceeds limit of cards !")
        else:
            card.next_card = self.top
            self.top = card
            self.isEmpty = False
    
    def pop(self):
        if self.isEmpty:
            print("the deck is empty")
        else:
            poped_card = self.top
            self.top = poped_card.next_card
            self.numOfCards += 1
            return poped_card

    def peek(self):
        return self.top.return_card()

colors = ["Red", "Blue", "Green", "Yellow"]
numbers = [1,2,3,4,5,6,7,8,9]

# created a list all cards
cards = []
for i in colors:
    for c in numbers:
        card = Card(i, c)
        cards.append(card)

# create random nums
def suffle(num):
    rand_cards = []
    ran_nums = []
    i = 0
    while i < num:
        x = random.randint(0,len(cards)-1)
        if x not in ran_nums:
            rand_cards.append(cards[x])
            ran_nums.append(x)
        else:
            continue
        i += 1
    return rand_cards

# print(suffle(10))

# here we GO!
new_deck = Deck(20)
my_cards = suffle(20)

for i in my_cards:
    new_deck.push(i)


player_1_cards = []
player_2_cards = []

# print(new_deck.isEmpty)
i = 0
while i <= 5:
    player_1_cards.append(new_deck.pop())
    player_2_cards.append(new_deck.pop())
    i += 1


# print player 1
print("-"*20)
print("player 1 cards:")
print("-"*20)

i = 1 
while i < len(player_1_cards):
    print(f"{i}- {player_1_cards[i].return_card()}")
    i += 1
#  print player 2 
print("-"*20)
print("player 2 cards:")
print("-"*20)

i = 1 
while i < len(player_2_cards):
    print(f"{i}- {player_2_cards[i].return_card()}")
    i += 1

#  peek at cards 
print("-"*20)
print(f"First card in deck:{new_deck.peek()}")
print("-"*20)




# for i in player_1_cards:
#     print(f"{i.print_card()}")

# print("--"*20)
# for i in player_2_cards:
#     print(f"{i.print_card()}")