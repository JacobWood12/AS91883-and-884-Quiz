# String of dashes to print to seperate text.
seperator = str("--------------------")

# Welcome messages.
print("Welcome to this quiz!")
print("Today, your topics will be geography, history, and politics.")
print("This is a multi-player quiz, so make sure you're both here.")

# Get player names.
print(seperator)
player_1 = str(input("Player 1 - what is your name? \n"))
#2 Tests if player names have numbers in them, and rejects them if they are.
if any(char.isdigit() for char in player_1):
  print("Please input a name with letters only.")
else:
  player_2 = str(input("Player 2 - what about you? \n"))
  if any(char.isdigit() for char in player_2):
    print("Please input a name with letters or characters only.")
  # After testing if player names have numbers, tests if they're both identical and rejects them if they are.
  else:
    if player_1 == player_2:
      print("Please choose different names from each other.")
    else:
      print(f"Welcome, {player_1} and {player_2}, let's get started.")

print(seperator)

# Question database.
# TODO