#My first project in Python - Game of hangman
import random

def graf(lives):
    gallows_graf = [
        """
    -------
    |     |
    |     O
    |    /|\\
    |    / \\
    |     
    -------
    """,
     """
    -------
    |     
    |     O
    |    /|\\
    |    / \\
    |     
    -------
    """,
     """
    -------
    |     |
    |     
    |    /|\\
    |    / \\
    |    
    -------
    """,
     """
    -------
    |     |
    |     
    |    
    |    
    |     
    -------
    """
    ]
    return gallows_graf[lives]

def game(words: list, lives: int):
    word_to_guess = random.choice(words).upper()
    display_word = "_ " * len(word_to_guess)
    good_guesses = set()

    while lives > 0 and "_" in display_word:
        print(f"Try guessing this word: {display_word}")
        print(graf(lives)) 
        letter = input("Try guessing the letter: ").upper()
        if letter in word_to_guess:
            good_guesses.add(letter)
            display_word = ""
            for character in word_to_guess:
                if character in good_guesses:
                    display_word += character
                else:
                    display_word += "_"
                display_word += " "
        else:
            lives -= 1
            if lives > 0:
                print(f"You miss! but still you have {lives} tries")
            else:
                print("GAME OVER")
                print(graf(lives))
    if lives > 0:
        print("You are the best! \n You won!!!")
    else: 
        print("You lost the game :(")


def main():
    countries = [ 
        "France", "Germany", "Italy", "Spain", "Greece", "Austria", "Hungary", "Poland", "Portugal"
    ]
    capitals = [
        "Paris", "Berlin", "Rome", "Madrid", "London",  
        "Budapest", "Warsaw", "Prague", "Stockholm",
        "Oslo", "Dublin", "Copenhagen", 
    ]
    lives = 3

    answer = input("Do you want to start new game? Y/N ")
    while answer.lower() == "y":
        category = input("Do you prefer to guess the name of the capital or the country? \n 1 - capital \n 2 - coutry: ")
        if category == '2':
            game(countries, lives)
        else:
            game(capitals, lives)
        answer = input("Do you want to start new game? Y/N ")


main()