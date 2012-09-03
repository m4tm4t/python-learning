# -*-coding:utf-8 -*

#
# Roulette game
##

from random import randrange
from math import ceil

playing = True
money   = 1000

while playing:
  choosed_number = -1

  while choosed_number < 0 or choosed_number > 49:
    try:
      choosed_number = int(raw_input("Please, enter a number between 0 and 49 : "))
    except ValueError:
      print("Wrong number")

    if choosed_number < 0 or choosed_number > 49:
      print("> Error: %i is not a number between 0 and 49 !!! " % choosed_number)

  bid_amount = 0

  while bid_amount <= 0 or bid_amount > money:
    try:
      bid_amount = int(raw_input("Now, choose the amount of your bet : "))
    except ValueError:
      print("Wrong amount")

    if bid_amount <= 0:
      print("The amount should greater than « 0 »")
    if bid_amount > money:
      print("You can't bet more than %i" % money)

  random_number = randrange(0,49)
  print("The roulette rotates... and the number is... « %i » !" % random_number)

  if random_number == choosed_number:
    amount_win = bid_amount*3
    money += amount_win
    print("Congrats, you win %i$ !" % amount_win)
  elif random_number%2 == choosed_number%2:
    amount_win = ceil(bid_amount*0.5)
    money += amount_win
    print("Good, the number has same color, you win %i$ !" % amount_win)
  else:
    money -= bid_amount
    print("Sorry, you loses %i$" % bid_amount)

  if money <= 0:
    playing = False
    print("Sorry, you have no enough money, go see the cashier plzkthx")
  else:
    play_again = raw_input("Want to make another bet ? (y)es / (n)o : ")
    if play_again == "n":
      playing = False
      print("Goodbye, you leaves the table with %i$ !" % money)