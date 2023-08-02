tickets = input().split(', ')

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]

    for symbol in winning_symbols:
        match_found = False
        for count in range(10, 5, -1):
            current_sequence = symbol * count
            if current_sequence in left_part and current_sequence in right_part:
                if count == 10:
                    print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - {count}{symbol}')
                match_found = True
                break
        if match_found:
            break
    else:
        print(f'ticket "{ticket}" - no match')
