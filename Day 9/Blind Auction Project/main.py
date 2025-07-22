import art
print(art.logo)
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
next_player = True
current_price = 0

while next_player:
    name = input("What is your name?\n")
    price = int(input("What is your bid\n"))
    next = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    print("\n" * 20)

    if current_price < price:
        current_price = price
        auction_info = {
            name: price
        }
    if next == "no":
        next_player = False

print(auction_info)

# TODO-4: Compare bids in dictionary


