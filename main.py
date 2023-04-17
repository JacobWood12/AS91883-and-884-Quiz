# Imports sys package to end program if users choose the same or put a number in their names.
import sys

# String of dashes to print to seperate text.
separator = str("--------------------")

# Welcome messages.
print("Welcome to this quiz!")
print("Today, your topics will be geography, history, and politics.")
print("This is a multi-player quiz, so make sure you're both here.")

# Get player names.
print(separator)
player_1 = str(input("Player 1 - what is your name? \n"))
# Tests if player names have numbers in them, and rejects them if they are.
if any(char.isdigit() for char in player_1):
  sys.exit("Please input a name without numbers only.")
else:
  player_2 = str(input("Player 2 - what about you? \n"))
  if any(char.isdigit() for char in player_2):
    sys.exit("Please input a name without numbers only.")
  # After testing if player names have numbers, tests if they're both identical and rejects them if they are.
  else:
    if player_1 == player_2:
      sys.exit("Please choose different names from each other.")
    else:
      print(f"Welcome, {player_1} and {player_2}, let's get started.")

print(separator)

# Question database.
questions = [
  "Filler.",
  # Geography section.
  "How many states are in the USA? \n 1 - 51. \n 2 - 50. \n 3 - 60. \n",
  "What continent is Nepal in? \n 1 - America. \n 2 - Europe. \n 3 - Asia \n",
  "What is the capital of Scotland? \n 1 - Edinburgh. \n 2 - Glasgow. \n 3 - Cardiff. \n",
  # History section.
  "When did World War II start? \n 1 - 1945. \n 2 - 1940. \n 3 - 1941. \n?",
  "How long ago was the extinction of the dinosaurs? \n 1 - 300 million y ars ago. \n 2 - 1 billion years ago. \n 3 - 65 million years ago. \n",
  "When was the Treaty of Waitangi signed? \n 1 - 1850. \n 2 - 1840. \n 3 - 1799. \n",
  # Politics section.
  "How often are elections held in New Zealand? \n 1 - Every three years. \n 2 - Every five years. \n 3 - Every four years. \n",
  "About how many countries are there in the world? \n 1 - About 250. \n 2 - About 195. \n 3 - About 300. \n",
  "Where was the first democracy? \n 1 - England. \n 2 - China. \n 3 - Greece. \n",
]

# Tells users how to answer questions.
print("Don't forget - to select your answer, enter the number next to it.")

# Sets score variables.
player_1Score = int(0)
player_2Score = int(0)


# Defines functions when answering questions for...
# ...correct answers...
def answerCorrect():
  print("You're correct! 🥳")
  print("A point to you.")


# ...incorrect answers...
def answerIncorrect():
  print("You're incorrect. 🫤")
  print("No points to you.")


# ...and errors.
def answerError():
  print(
    "Did you enter your answer as a number corresponding to the answer you picked? If not, that's probably the issue here"
  )
  print("If you did do that, then looks like I made a mistake somewhere.")


# Question chooser.
for i in range(1, 10):
  print(f"Question {i}")
  question = questions[i]
