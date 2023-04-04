# String of dashes to print to seperate text.
seperator = str("--------------------")

# Welcome messages.
print("Welcome to this quiz!")
print("Today, your topics will be geography, history, and politics.")
print("This is a multi-player quiz, so make sure you're both here.")

# Get player names.
print(seperator)
player_1 = str(input("Player 1 - what is your name? \n"))
player_2 = str(input("Player 2 - what about you? \n"))
print(f"Welcome, {player_1} and {player_2}, let's get started.")

print(seperator)