#My first project in Python - Game of hangman

imie = str(input("Cześć, jak masz na imie? "))
print(f'Witaj {imie}.\nZapraszam Cię do gry.\n')
      
zgadywane_haslo = 'KOLEJKA'

#Tablica wypisująca znaki podkreślenia czyli pętla która będzie się iterowała po zgadywanym haśle i wpisywała podkreslenia do listy 

podreslenia = list(zgadywane_haslo)

for podloga in range(len(podreslenia)):
    podreslenia[podloga] = "_ "
print("Oto miejsce na nasze hasło: ",podreslenia)