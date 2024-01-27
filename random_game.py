import random

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
print(str(shuffled_deck) + "\n\n\n")
print(str(readable_shuffled_deck))

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
    
    
