# Import modulow w jezyku Python.

import lesson13     # mozna importowac wlasne moduly
from lesson13 import add
import sys          # mozna importowac moduly wbudowane (systemowy)
import math         # modul matematyczny
import random       # modul odpowiedzialny za generowanie zmiennych losowych

# przyklad dostepu do metod z modulu
print(add(5, 6))
print(lesson13.mul(1.5, 4))

# przyklad dostepu do metod modulow wbudowanych
print(random.random())
print(sys.version)
print(math.sin(math.pi / 2))
