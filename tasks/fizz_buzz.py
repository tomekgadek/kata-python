"""
    Popularna dziecieca gra 'FizzBuzz'.

    Wypisz wszystkie liczby od 1 do 100. Jezeli liczba jest podzielna przez:

    * 3 - wypisz 'Fizz',
    * 5 - wypisz 'Buzz',
    * 3 i 5 - wypisz 'FizzBuzz'.
"""

class FizzBuzzGame:
    def __init__(self):
        self.limit = 100
    
    def play(self):
        for digit in range(1, self.limit + 1):
            if digit % 3 == 0:
                print("Fizz", end="")
            
            if digit % 5 == 0:
                print("Buzz", end="")
            
            if digit % 3 != 0 and digit % 5 != 0:
                print(digit, end="")
            
            print()

game = FizzBuzzGame()
game.play()
