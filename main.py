############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import art

player1 = []
dealer = []
cards = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')

def score_count(hand):
  points = 0
  for card in hand:
    if card == ('A'):
      if points>10:
        points += 1
      else:
        points += 11
    elif card == ('J') or card == ('Q') or card == ('K'):
      points += 10
    else:
      points += int(card)
  return points

def get_card():
  return cards[random.randint(0,(len(cards)-1))]

def win_condition(score_p1, score_p2):
  if score_p2 <= 21 and score_p1 <= 21:
    if score_p1 > score_p2:
      if score_p1 == 21:
        print("You have hit Blackjack!\n You win!")
      else:
        print("You have the closer number.\nYou win!")
    elif score_p1 == score_p2:
      print("It's a draw!")
    else:
      if score_p2 == 21:
        print("Dealer has hit Blackjack!\nYou lose!")
      else:
        print("Dealer has a closer number.\nYou lose!")
  elif score_p2 <= 21 and score_p1 > 21:
    print("You went over 21!\nYou lose!")
  elif score_p2 > 21 and score_p1 <= 21:
    print("Dealer went over 21!\nYou win!")

def init_setup():
  player1.clear()
  dealer.clear()
  player1.append(get_card())
  player1.append(get_card())
  dealer.append(get_card())

def display_point():
  print("Player hand: ",player1,"\nscore: ", score_count(player1))
  print("Dealer's hand: ",dealer,"\nscore: ",score_count(dealer))

def draw_next_card(player):
  player.append(get_card())

print(art.logo)
print("Welcome to a game of BlackJack\nWould you like to play?")
game_state = True
# yes or no option
while game_state == True:
  play = input("Yes(y) or No(n): ").lower()
  if play == 'y':
    #while play is true start game loop
    init_setup()
    while True:
      display_point()
      if score_count(player1) >=21 or score_count(dealer)>=21:
        break
      else:
        player_turn = input("Will you 'draw' or 'stand': ")
        if player_turn.lower() =='draw':
          draw_next_card(player1)
        else:
          break
    if score_count(player1) < 22:
      while score_count(dealer) < 17:
        draw_next_card(dealer)
    display_point()  
    win_condition(score_count(player1),score_count(dealer))
    print("Would you like to play another round?")
  elif play == 'n':
    break
  else:
    print("incorrect input")
  
