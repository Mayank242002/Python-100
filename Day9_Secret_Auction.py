def find_largest_bidder(bid):
    largest=0
    largest_bid=""
    for key in bid:
        if (bid[key]>largest):
            largest=bid[key]
            largest_bid=key

    print(largest_bid,"with ",largest,"Won the bid!!Hurray")

bid={}
choice="yes"
print("Welcome to the Secret Auction Program")


while (choice=="yes"):
    name=input("what is your name?:")
    amount=int(input("what's your bid?:"))
    bid[name]=amount

    choice=input("Are there any other bidder?Type 'yes' or 'no'.")

find_largest_bidder(bid)



