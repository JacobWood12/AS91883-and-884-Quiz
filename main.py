# Imports sys package to end program if users choose the same or put a number in their names.
import sys

# String of dashes to print to seperate text.
separator = str("--------------------")

# Welcome messages.
print("Welcome to this quiz!")
print("Today, your topics will be geography, history, and politics.")
print("This is a multi-player quiz, so make sure you're both here.")


# Defines functions when answering questions for...
# ...correct answers...
def answerCorrect(name):
  print(f"{name}, you're correct! 🥳")
  print("A point to you.")
  print(separator)


# ... and incorrect answers.
def answerIncorrect(name):
  print(f"{name}, you're incorrect. 🫤")
  print("No points to you.")
  print(separator)


# Defines function to print scores after each question.
def scores():
  print(f"{player_1}, you're now at {player_1Score} points.")
  print(f"{player_2}, you're now at {player_2Score} points.")
  print(separator)


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
  "When did World War II start? \n 1 - 1945. \n 2 - 1940. \n 3 - 1939. \n?",
  "How long ago was the extinction of the dinosaurs? \n 1 - 300 million years ago. \n 2 - 1 billion years ago. \n 3 - 65 million years ago. \n",
  "When was the Treaty of Waitangi signed? \n 1 - 1850. \n 2 - 1840. \n 3 - 1799. \n",
  # Politics section.
  "How often are elections held in New Zealand? \n 1 - Every three years. \n 2 - Every five years. \n 3 - Every four years. \n",
  "About how many countries are there in the world? \n 1 - About 250. \n 2 - About 195. \n 3 - About 300. \n",
  "Where was the first system of democracy? \n 1 - England. \n 2 - China. \n 3 - Greece. \n",
]

# Tells users how to answer questions.
print("Don't forget - to select your answer, enter the number next to it.")
print(separator)

# Sets score variables.
player_1Score = int(0)
player_2Score = int(0)

# Question chooser.
for i in range(1, 10):
  print(f"Question {i}")
  question = questions[i]
  # Question 1
  if question == "How many states are in the USA? \n 1 - 51. \n 2 - 50. \n 3 - 60. \n":
    # Section to ask player 1.
    print(separator)
    player_1Answer = input(str(f"{player_1}, {question}"))
    # Section to ask player 2.
    print(separator)
    player_2Answer = input(str(f"{player_2}, {question}"))
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "2":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "2":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 2
  elif question == "What continent is Nepal in? \n 1 - America. \n 2 - Europe. \n 3 - Asia \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "3":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "3":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 3
  elif question == "What is the capital of Scotland? \n 1 - Edinburgh. \n 2 - Glasgow. \n 3 - Cardiff. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "1":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "1":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 4
  elif question == "When did World War II start? \n 1 - 1945. \n 2 - 1940. \n 3 - 1939. \n?":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "3":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "3":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
  # Question 5
  elif question == "How long ago was the extinction of the dinosaurs? \n 1 - 300 million years ago. \n 2 - 1 billion years ago. \n 3 - 65 million years ago. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "3":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "3":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 6
  elif question == "When was the Treaty of Waitangi signed? \n 1 - 1850. \n 2 - 1840. \n 3 - 1799. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "2":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "2":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 7
  elif question == "How often are elections held in New Zealand? \n 1 - Every three years. \n 2 - Every five years. \n 3 - Every four years. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "1":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "1":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 8
  elif question == "About how many countries are there in the world? \n 1 - About 250. \n 2 - About 195. \n 3 - About 300. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "2":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "2":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    scores()
  # Question 9
  elif question == "Where was the first system of democracy? \n 1 - England. \n 2 - China. \n 3 - Greece. \n":
    # Section to ask player 1.
    player_1Answer = input(str(f"{player_1}, {question}"))
    print(separator)
    # Section to ask player 2.
    player_2Answer = input(str(f"{player_2}, {question}"))
    print(separator)
    # Calculate and print player 1 score.
    playerName = player_1
    if player_1Answer == "3":
      player_1Score = player_1Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
    # Calculate and print player 2 score.
    playerName = player_2
    if player_2Answer == "3":
      player_2Score = player_2Score + 1
      answerCorrect(playerName)
    else:
      answerIncorrect(playerName)
  else:
    print("Looks like there's been an error. Try starting again.")

# Print final scores.
print("It's the end of the quiz now.")
print("And the winner is...")
# If player 1 wins.
if player_1Score > player_2Score:
  print(f"{player_1}, with {player_1Score} points!")
  print(f"And in second place is {player_2} with {player_2Score} points.")
# If player 2 wins.
elif player_1Score < player_2Score:
  print(f"{player_2}, with {player_2Score} points!")
  print(f"And in second place is {player_1} with {player_1Score} points.")
# If it's a tie.
else:
  print("Everyone!")
  print(f"{player_1} and {player_2} both tied on {player_1Score} points!")
