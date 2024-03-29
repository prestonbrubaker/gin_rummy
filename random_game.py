import random
import time

def create_shuffled_deck():
    # Initialize deck
    deck = []

    # Encode suits
    suits = {'hearts': '0,0', 
             'diamonds': '0,1', 
             'clubs': '1,0', 
             'spades': '1,1'}

    # Encode values
    values = {
        'ace': '0,0,0,1', 
        '2': '0,0,1,0', 
        '3': '0,0,1,1',
        '4': '0,1,0,0', 
        '5': '0,1,0,1', 
        '6': '0,1,1,0',
        '7': '0,1,1,1', 
        '8': '1,0,0,0', 
        '9': '1,0,0,1',
        '10': '1,0,1,0', 
        'jack': '1,0,1,1', 
        'queen': '1,1,0,0',
        'king': '1,1,0,1'
    }

    # Generate deck
    for suit, suit_code in suits.items():
        for value, value_code in values.items():
            deck.append([suit_code + ',' + value_code])

    # Shuffle deck
    random.shuffle(deck)

    return deck

def get_card_dictionary():
    # Reverse mapping
    suits = {'0,0': 'hearts', 
             '0,1': 'diamonds', 
             '1,0': 'clubs', 
             '1,1': 'spades'}
    values = {
        '0,0,0,1': 'ace', 
        '0,0,1,0': '2', 
        '0,0,1,1': '3',
        '0,1,0,0': '4', 
        '0,1,0,1': '5', 
        '0,1,1,0': '6',
        '0,1,1,1': '7', 
        '1,0,0,0': '8', 
        '1,0,0,1': '9',
        '1,0,1,0': '10', 
        '1,0,1,1': 'jack', 
        '1,1,0,0': 'queen',
        '1,1,0,1': 'king'
    }

    return suits, values


def card_to_string(card):
    suits, values = get_card_dictionary()
    
    # Split the encoded card to get suit and value codes
    encoded_card = card[0].split(',')
    suit_code = ','.join(encoded_card[:2])
    value_code = ','.join(encoded_card[2:])

    # Translate codes to readable suit and value
    suit = suits[suit_code]
    value = values[value_code]

    return f"{value} of {suit}"



def read_deck(deck):
    suits, values = get_card_dictionary()
    readable_deck = []

    for card in deck:
        encoded_card = card[0].split(',')
        suit_code = ','.join(encoded_card[:2])
        value_code = ','.join(encoded_card[2:])
        suit = suits[suit_code]
        value = values[value_code]
        readable_deck.append(f"{value} of {suit}")

    return readable_deck

# Create and read a shuffled deck
shuffled_deck = create_shuffled_deck()
readable_shuffled_deck = read_deck(shuffled_deck)
print("BINARY ENCODED SHUFFLED DECK: \n" + str(shuffled_deck) + "\n\n")
print("READABLE SHUFFLED DECK: \n" + str(readable_shuffled_deck) + "\n\n")

player_one_hand = []
player_two_hand = []

# Deal cards to each player
for i in range(20):
    if( i % 2 == 0):
        player_one_hand.append(shuffled_deck[i])
        print("Player 1 dealt " + card_to_string(shuffled_deck[i]))
    else:
        player_two_hand.append(shuffled_deck[i])
        print("Player 2 dealt " + card_to_string(shuffled_deck[i]))

# Remove dealt cards from the deck to create deck
deck = []


for i in range(len(shuffled_deck)):
    deck.append(shuffled_deck[i])


for i in range(19, -1, -1):
    deck.pop(i)

readable_deck = read_deck(deck)
print("\n\nDECK AFTER DEALING: \n" + str(readable_deck) + "\n\n")

# Print each player's hand

readable_p1_deck = read_deck(player_one_hand)
readable_p2_deck = read_deck(player_two_hand)
print("PLAYER 1s HAND: \n" + str(readable_p1_deck) + "\n\n")
print("PLAYER 2s HAND: \n" + str(readable_p2_deck) + "\n\n")

# Turn first card from the deck over
discard_pile = []
discard_pile.append(deck[0])
deck.pop(0)

readable_discard_pile = read_deck(discard_pile)
print("CARD IN DISCARD PILE TO START: \n" + str(readable_discard_pile) + "\n\n")

readable_deck = read_deck(deck)
print("DECK AFTER FLIPPING: \n" + str(readable_deck) + "\n\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("\n\nLET'S BEGIN THE GAME!!!\n\n")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

game_in_progress = True
while game_in_progress:
    print("\nSTEP 1: WE MUST BE SURE TO REPLACE THE DECK WITH THE DISCARD PILE AND TURN ONE CARD OVER IF THE DECK IS EMPTY\n")
    if(len(deck) == 0):
        print("\nTHE DECK HAS BEEN FOUND TO BE EMPTY. THE DISCARD PILE WILL BE USED TO REPLACE THE DECK.\n")
        for i in range(len(discard_pile) - 1, -1, -1):
            deck.append(discard_pile[i])
            discard_pile.pop(i)
        # Add shuffling in the future here
        
        # Start the discard pile with the top card from the deck
        discard_pile.append(deck[0])
        deck.pop(0)
    else:
        print("\nTHE DECK IS NOT EMPTY. NO ACTION WILL BE TAKEN\n")
            

    
    print("\nSTEP 2: PLAYER 1 MUST CHOOSE TO PICK UP FROM DECK OR DISCARD\n")
    choice = random.randint(0,1)    # 0 -> deck, 1 -> discard
    if(choice == 0):
        print("\nPLAYER 1 HAS CHOSEN TO PICK UP FROM THE DECK")
        player_one_hand.append(deck[0])
        deck.pop(0)

        readable_p1_deck = read_deck(player_one_hand)
        print("PLAYER 1s HAND AFTER TAKING TOP CARD FROM DECK: \n" + str(readable_p1_deck) + "\n\n")
        
        readable_deck = read_deck(deck)
        print("DECK AFTER PLAYER TOOK TOP CARD: \n" + str(readable_deck) + "\n\n")

        
        
    else:
        print("\nPLAYER 1 HAS CHOSEN TO PICK UP FROM THE DISCARD PILE")
        player_one_hand.insert(0, discard_pile[0])
        discard_pile.pop(0)

        readable_p1_deck = read_deck(player_one_hand)
        print("PLAYER 1s HAND AFTER TAKING TOP CARD FROM DISCARD PILE: \n" + str(readable_p1_deck) + "\n\n")
        
        readable_discard_pile = read_deck(discard_pile)
        print("DISCARD PILE AFTER PLAYER TOOK TOP CARD: \n" + str(readable_discard_pile) + "\n\n")

        

    #time.sleep(1)

    print("\n\nSTEP 3: PLAYER 1 MUST CHOOSE WHICH CARD TO DISCARD\n\n")

    card_to_discard_index = random.randint(0, len(player_one_hand) - 1)

    print("PLAYER 1 HAS CHOSEN TO DISCARD " + card_to_string(player_one_hand[card_to_discard_index]) + "\n\n")

    discard_pile.insert(0, player_one_hand[card_to_discard_index])

    player_one_hand.pop(card_to_discard_index)

    readable_discard_pile = read_deck(discard_pile)
    print("DISCARD PILE AFTER PLAYER DISCARDED: \n" + str(readable_discard_pile) + "\n\n")

    readable_p1_deck = read_deck(player_one_hand)
    print("PLAYER 1s HAND AFTER DISCARDING TO DISCARD PILE: \n" + str(readable_p1_deck) + "\n\n")


    print("\nSTEP 4: WE MUST BE SURE TO REPLACE THE DECK WITH THE DISCARD PILE AND TURN ONE CARD OVER IF THE DECK IS EMPTY\n")
    if(len(deck) == 0):
        print("\nTHE DECK HAS BEEN FOUND TO BE EMPTY. THE DISCARD PILE WILL BE USED TO REPLACE THE DECK.\n")
        for i in range(len(discard_pile) - 1, -1, -1):
            deck.append(discard_pile[i])
            discard_pile.pop(i)
        # Add shuffling in the future here
        
        # Start the discard pile with the top card from the deck
        discard_pile.append(deck[0])
        deck.pop(0)
    else:
        print("\nTHE DECK IS NOT EMPTY. NO ACTION WILL BE TAKEN\n")
            

    
    print("\nSTEP 5: PLAYER 2 MUST CHOOSE TO PICK UP FROM DECK OR DISCARD\n")
    choice = random.randint(0,1)    # 0 -> deck, 1 -> discard
    if(choice == 0):
        print("\nPLAYER 2 HAS CHOSEN TO PICK UP FROM THE DECK")
        player_two_hand.append(deck[0])
        deck.pop(0)

        readable_p2_deck = read_deck(player_two_hand)
        print("PLAYER 2s HAND AFTER TAKING TOP CARD FROM DECK: \n" + str(readable_p2_deck) + "\n\n")
        
        readable_deck = read_deck(deck)
        print("DECK AFTER PLAYER TOOK TOP CARD: \n" + str(readable_deck) + "\n\n")

        
        
    else:
        print("\nPLAYER 2 HAS CHOSEN TO PICK UP FROM THE DISCARD PILE")
        player_two_hand.insert(0, discard_pile[0])
        discard_pile.pop(0)

        readable_p2_deck = read_deck(player_two_hand)
        print("PLAYER 2s HAND AFTER TAKING TOP CARD FROM DISCARD PILE: \n" + str(readable_p2_deck) + "\n\n")
        
        readable_discard_pile = read_deck(discard_pile)
        print("DISCARD PILE AFTER PLAYER TOOK TOP CARD: \n" + str(readable_discard_pile) + "\n\n")

        

    #time.sleep(1)

    print("\n\nSTEP 6: PLAYER 2 MUST CHOOSE WHICH CARD TO DISCARD\n\n")

    card_to_discard_index = random.randint(0, len(player_two_hand) - 1)

    print("PLAYER 2 HAS CHOSEN TO DISCARD " + card_to_string(player_two_hand[card_to_discard_index]) + "\n\n")

    discard_pile.insert(0, player_two_hand[card_to_discard_index])

    player_two_hand.pop(card_to_discard_index)

    readable_discard_pile = read_deck(discard_pile)
    print("DISCARD PILE AFTER PLAYER DISCARDED: \n" + str(readable_discard_pile) + "\n\n")

    readable_p2_deck = read_deck(player_two_hand)
    print("PLAYER 2s HAND AFTER DISCARDING TO DISCARD PILE: \n" + str(readable_p2_deck) + "\n\n")
    
    
        
        


