import random

def create_shuffled_deck():
    # Initialize deck
    deck = []

    # Encode suits
    suits = {'hearts': '00', 'diamonds': '01', 'clubs': '10', 'spades': '11'}

    # Encode values
    values = {
        'ace': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110',
        '7': '0111', '8': '1000', '9': '1001',
        '10': '1010', 'jack': '1011', 'queen': '1100',
        'king': '1101'
    }

    # Generate deck
    for suit, suit_code in suits.items():
        for value, value_code in values.items():
            deck.append([suit_code, value_code])

    # Shuffle deck
    random.shuffle(deck)

    return deck

def get_card_dictionary():
    # Reverse mapping
    suits = {'00': 'hearts', '01': 'diamonds', '10': 'clubs', '11': 'spades'}
    values = {
        '0001': 'ace', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6',
        '0111': '7', '1000': '8', '1001': '9',
        '1010': '10', '1011': 'jack', '1100': 'queen',
        '1101': 'king'
    }

    return suits, values

def read_deck(deck):
    suits, values = get_card_dictionary()
    readable_deck = []

    for card in deck:
        suit_code, value_code = card
        suit = suits[suit_code]
        value = values[value_code]
        readable_deck.append(f"{value} of {suit}")

    return readable_deck

# Create and read a shuffled deck
shuffled_deck = create_shuffled_deck()
readable_shuffled_deck = read_deck(shuffled_deck)
