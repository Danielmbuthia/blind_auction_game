from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

continue_bidding = True

while continue_bidding:
    bids_dic = {}
    name = input("What your name: \n")
    bid = input("what your bid price: \n")
    bids_dic[name] = bid
    other = input("Type 'Yes' for other users to bid or 'No' if no other users: \n")
    
    if other.lower() == "yes": 
        continue_bidding = True
        clear()
    elif other.lower() == "no":
        continue_bidding = False
        maximum = 0
        clear()
        for name in bids_dic:
            if int(bids_dic[name]) > maximum:
                maximum = bids_dic[name]
        print(f" {name} won with the highest bid of {maximum}")
    else:
        print("Wrong input please use 'yes' or 'no'")
        other = input("Type Yes for other users to bid or No if no other users: \n")
    

   