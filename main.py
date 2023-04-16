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
  "How many states are in the USA? \n 1 - 51. \n 2 - 50. \n 3 - 60. \n",
  "What continent is Nepal in? \n 1 - America. \n 2 - Europe. \n 3 - Asia \n",
  "What is the capital of Scotland? \n 1 - Edinburgh. \n 2 - Glasgow. \n 3 - Cardiff. \n",
  "Where is Dunedin? \n 1 - The North Island. \n 2 - The South Island. \n 3 - England. \n",
  "What is the line drawn around the Earth halfway between both poles called? \n 1 - The Meridian. \n 2 - The Equator. \n 3 - The Interpolar Line. \n",
  "What is the population of China? \n 1 - About 10 million. \n 2 - About 200 million. \n About 1.4 billion. \n",
  "Which of these oceans is the smallest? \n 1 - The Pacific Ocean. \n 2 - The Atlantic Ocean \n 3 - The Arctic Ocean. \n",
  # History section.
  "When did World War II start \n 1 - 1945. \n 2 - 1940. \n 3 - 1941. \n?",
  "How long ago was the extinction of the dinosaurs? \n 1 - 300 million y ars ago. \n 2 - 1 billion years ago. \n 3 - 65 million years ago. \n",
  "When was the Treaty of Waitangi signed? \n 1 - 1850. \n 2 - 1840. \n 3 - 1799. \n",
  "Who was the American Civil War between? \n 1 - The USA and Britain \n 2 - The USA and Mexico. \n 3 - The USA and the Confederacy. \n",
  "What language did they speak in Ancient Rome? \n 1 - Italian. \n 2 - Latin. \n 3 - Roman. \n",
  "How many capital cities has New Zealand had? \n 1 - One. \n 2 - Two. \n 3 - Three. \n",
  "When was Google founded? \n 1 - 2007. \n 2 - 1998. \n 3 - 1992. \n",
  # Politics section.
  "As of April 2023, who is the President of the United States? \n 1 - Joe Biden. \n 2 - Donald Trump. \n 3 - Chris Hipkins. \n",
  "How often are elections held in New Zealand? \n 1 - Every three years. \n 2 - Every five years. \n 3 - Every four years. \n",
  "About how many countries are there in the world? \n 1 - About 250. \n 2 - About 195. \n 3 - About 300. \n",
  "Where was the first democracy? \n 1 - England. \n 2 - China. \n 3 - Greece. \n",
  "What is the voting age in New Zealand? \n 1 - 18. \n 2 - 16. \n 3 - 21. \n",
  "What is a dictatorship? \n 1 - A system where the people choose how they are governed. \n 2 - A system where the wealthy govern. \n 3 - A system where one individual rules over all. \n",
  "Random bonus point.",
]

# Sets score variable
score = int(0)

# Question chooser.
for i in range(1,10):
  question = random.choice(questions)
  if question == "Random bonus point.":
    print("You both get a bonus point!")
    score = score+1
  else:
    print(f"Question {i}")
    answer = input(question)
    print(separator)