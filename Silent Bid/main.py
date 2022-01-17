from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

def find_winner(bidding_records):
  highest_bid =0
  winner = ""
  for bidders in bidding_records:
    bid_amt = bidding_records[bidders]
    if bid_amt > highest_bid:
      highest_bid = bid_amt
      winner = bidders
  print(f'\n\n   ||   Congratulations The Winner is {winner} with a total bid of $ {highest_bid}.    ||')

bids = {}
bidding_over = False

while not bidding_over:
  name = input('What is your Name ? -> ')
  price = int(input('What is your Bid ? -> $ '))
  bids[name] = price
  p = input("Are there any other bidders ? Type 'Yes' or 'No'. \n")
  if p == 'No':
    bidding_over = True
    find_winner(bids)
  elif p == 'Yes':
    clear()