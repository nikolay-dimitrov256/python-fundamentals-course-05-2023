deck_of_cards = input().split(" ")
number_of_shuffles = int(input())

middle_of_deck = len(deck_of_cards) // 2

for shuffle in range(number_of_shuffles):
    new_deck = []
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]

    for card in range(middle_of_deck):
        new_deck.append(left_part[card])
        new_deck.append(right_part[card])

    deck_of_cards = new_deck

print(deck_of_cards)
