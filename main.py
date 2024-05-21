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

def main():
    countries = [ 
        "France", "Germany", "Italy", "Spain", "Greece", "Austria", "Hungary", "Poland", "Portugal"
    ]
    lives = 3

    answer = input("Do you want to start new game? Y/N ")


main()