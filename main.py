# Imports random package to choose random question.
import random

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

print(separator)

# Question database.
questions = [
  # Geography section.
  "How many states are in the USA?",
  "What continent is Nepal in?",
  "What is the capital of Scotland?",
  "Where is Dunedin?",
  "What is the line drawn around the Earth halfway between both poles called?",
  "What is the population of China?",
  "Which of these oceans is the smallest?",
  # History section.
  "When did World War II start?",
  "How long ago was the extinction of the dinosaurs?",
  "When was the Treaty of Waitangi signed?",
  "Who was the American Civil War between?",
  "What language did they speak in Ancient Rome?",
  "How many capital cities has New Zealand had?",
  "When was Google founded?",
  # Politics section.
  "As of April 2023, who is the President of the United States?",
  "How often are elections held in New Zealand?",
  "About how many countries are there in the world?",
  "Where was the first democracy?",
  "What is the voting age in New Zealand?",
  "What is a dictatorship?",
  "Random bonus point!",
]

# Question chooser.
