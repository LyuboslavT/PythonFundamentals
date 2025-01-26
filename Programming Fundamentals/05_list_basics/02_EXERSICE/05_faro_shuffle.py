deck = input().split()
shuffle = int(input())

for current_shuffle in range(shuffle):
    mid_deck = len(deck) // 2
    left_part = deck[:mid_deck]
    right_part = deck[mid_deck:]
    shuffled_deck = []

    for card_index in range(len(right_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])
    deck = shuffled_deck.copy()

print(deck)