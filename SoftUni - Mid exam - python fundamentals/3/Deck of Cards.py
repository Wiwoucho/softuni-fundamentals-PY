def add(card):
    global deck
    if card in deck:
        print("Card is already in the deck")
    else:
        deck.append(card)
        print("Card successfully added")


def remove(card):
    global deck
    if card not in deck:
        print("Card not found")
    else:
        deck.remove(card)
        print("Card successfully removed")


def remove_at_index(index):
    global deck
    if int(index) > len(deck):
        print("Index out of range")
    else:
        deck.pop(int(index))
        print("Card successfully removed")


def insert_index_card(index, card):
    global deck
    if int(index) > len(deck) or int(index) < 0:
        print("Index out of range")
    else:
        if card in deck:
            print("Card is already added")
        else:
            deck.insert(int(index), card)
            print("Card successfully added")


deck = input().split(", ")
shuffle = int(input())

for n in range(shuffle):
    command = input().split(", ")
    option = command[0]
    new_card = command[1]
    if option == "Add":
        add(new_card)
    elif option == "Remove":
        remove(new_card)
    elif option == "Remove At":
        index = command[1]
        remove_at_index(index)
    elif option == "Insert":
        index = command[1]
        card = command[2]
        insert_index_card(index, card)
print(f"{', '.join(deck)}")