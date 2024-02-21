import random
from black_jack_art import logo

rules =   """
  ############### Our Blackjack House Rules #####################

  ## The deck is unlimited in size. 
  ## There are no jokers. 
  ## The Jack/Queen/King all count as 10.
  ## The the Ace can count as 11 or 1.
  ## The cards have equal probability of being drawn.
  ## Cards are not removed from the deck as they are drawn.
  ## The computer is the dealer.
  ## If dealer has a score of 17 or less, they must draw another card.
  ## Ace for dealer is counted 11 always.
  ## If you have double Ace, even you want to count it as 1, it will be counted as 11 and the final score is 21 (for 2 Aces).

  ###############################################################
"""

# Define the deck of cards
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

# Define the values of the cards
cards_dict = {"Ace": 11, 
              "Two": 2, 
              "Three": 3, 
              "Four": 4, 
              "Five": 5, 
              "Six": 6, 
              "Seven": 7, 
              "Eight": 8, 
              "Nine": 9, 
              "Ten": 10, 
              "Jack": 10, 
              "Queen": 10, 
              "King": 10}

# Creat a function to start the game
def start_game():
  '''Staart the game'''
  
  print(logo)
  print("Welcome to Blackjack!")
  print(rules)
  
  answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

  # Check if the user wants to play
  if answer == "y":
    return True
  else:
    return False


# Creat a function to deal the cards
def deal_card():
  ''' Deal a random card'''
  return random.choice(cards)

# Creat a function to calculate the score
def calculate_score(hand, choice):
  '''Calculate the score of the hand'''
  
  score = 0
  # cheak whether we have 2 cards or not
  if len(hand) == 2:

    # 2 Aces is 21
    if hand[0] == "Ace" and hand[1] == "Ace":
      score = 21
      return score

    # 1 Ace depends on what choice user make
    elif hand[0] == "Ace" or hand[1] == "Ace":

      # If user choose to count Ace as 11
      if choice == "n":
        score = cards_dict[hand[0]] + cards_dict[hand[1]]

      # If user choose to count Ace as 1
      else:
        score = cards_dict[hand[0]] + cards_dict[hand[1]] - 10
        
      return score
    else:
      score = cards_dict[hand[0]] + cards_dict[hand[1]]
      return score 

  # If we have more than 2 cards
  else:
    for card in hand:

      # If user choose to count Ace as 1
      if choice == 'y' and card == "Ace":
        score += cards_dict[card] - 10

      # If user choose to count Ace as 11
      else:
        score += cards_dict[card]
        
    return score
    
# Creat a function to seperate the steps of the game
def step_seperator():
  '''seperate the steps from eachother'''
  print("\n############################################################\n")

# Main code
while start_game():
  # User and Dealr hands container
  user_hand = []
  dealer_hand = []

  # Deal the first 2 cards
  user_hand.append(deal_card())
  dealer_hand.append(deal_card())
  step_seperator()

  # Print the result of the first 2 cards
  print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand, 'n')}")
  print(f"Dealer's first card: ['{dealer_hand[0]}']' and that card score is {cards_dict[dealer_hand[0]]}")
  step_seperator()

  # Check if the user want to consider Ace as 1 or 11
  if "Ace" in user_hand:
    choice = input("You have an Ace. Do you want to use it as a 1 or 11? Type 'y' to count as '1' or 'n' to count as 11': ")
  else:
    choice = "n"
    
  # Check if the user want to get another card
  while calculate_score(user_hand, choice) < 21:
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if hit == "y":

      # Deal the dard again
      user_hand.append(deal_card())
      dealer_hand.append(deal_card())
      step_seperator()

      # Print the result of the 2 cards
      print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand, choice)}")
      print(f"Dealer's first card: ['{dealer_hand[0]}']' and that card score is {cards_dict[dealer_hand[0]]}")
      step_seperator()

    # If user wants to Stand
    else :
      break

  # Check if the user has lost of not
  if calculate_score(user_hand, choice) > 21:
    print("You went over 21. You lose 😭")

  # If User is Standing and not lost
  else:
    # Dealer's turn
    while calculate_score(dealer_hand, 'n') < 17 or len(dealer_hand) <= 2:
      dealer_hand.append(deal_card())
      step_seperator()

    # Print the dealer runs result
    print(f"Your final hand: {user_hand}, final score: {calculate_score(user_hand, choice)}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {calculate_score(dealer_hand, 'n')}")
    step_seperator()

    # Check if the dealer has lost
    if calculate_score(dealer_hand, 'n') > 21:
      print("Dealer went over 21. You win 😁")

    # Check if the user has won
    elif calculate_score(user_hand, choice) > calculate_score(dealer_hand, 'n'):
      print("You win 😁")

    # Check if it is a Draw
    elif calculate_score(user_hand, choice) == calculate_score(dealer_hand, 'n'):
      print("It's a draw 🙃")

    # Check if the user has lost
    else:
      print("You lose 😭")
    
# End of the game
step_seperator()
print("Goodbye!")
step_seperator()

  
  
  
  