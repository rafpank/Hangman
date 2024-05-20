#My first project in Python - Game of hangman
import random

name = str(input("Hi! what's your name? "))
print(f'Hello {name}.\nWelcom in the game of Hangman.\n')
      
countries = [
    'Francja', 'Australia', 'Brazylia', 'Indie', 'Kanada', 'Niemcy', 'Japonia', 'Włochy', 'Argentyna', 'Hiszpania',
    ]

guessing_password = random.choice(countries).upper()
presented_state = "_ " * len(guessing_password)
strike = set()

print("Guessing : ",presented_state)

lives = 5

while lives > 0:
    print("You have:", lives, "lives")
    letter = input("Try to guess letter:").upper()
    if letter in guessing_password:
        print("Great shot")   
        #for i in guessing_password:
        #    if guessing_password(i) == letter:
         #       guessing_password = letter
    else:
         print("You miss :(") 
         lives -=1
    