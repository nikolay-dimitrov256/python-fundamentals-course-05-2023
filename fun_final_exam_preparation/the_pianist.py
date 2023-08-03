def add_piece(pieces_dict: dict, piece: str, composer: str, key: str) -> dict:
    if piece not in pieces_dict:
        pieces_dict[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")

    return pieces_dict


def remove_piece(pieces_dict: dict, piece: str) -> dict:
    if piece in pieces_dict:
        del pieces_dict[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return pieces_dict


def change_key(pieces_dict: dict, piece: str, key: str) -> dict:
    if piece in pieces_dict:
        pieces_dict[piece]['key'] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return pieces_dict


number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split('|')
    pieces[current_piece] = {'composer': current_composer, 'key': current_key}

while True:
    line = input()
    if line == 'Stop':
        break

    line = line.split('|')

    if line[0] == 'Add':
        piece, composer, key = line[1], line[2], line[3]
        pieces = add_piece(pieces, piece, composer, key)

    elif line[0] == 'Remove':
        piece = line[1]
        pieces = remove_piece(pieces, piece)

    elif line[0] == 'ChangeKey':
        piece, new_key = line[1], line[2]
        pieces = change_key(pieces, piece, new_key)

for k, v in pieces.items():
    piece = k
    composer = v['composer']
    key = v['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")
