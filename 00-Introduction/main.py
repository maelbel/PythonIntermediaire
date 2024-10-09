# lambda arguments : expression

add_ten = lambda x: x + 10
add_ten(5)

multiply = lambda x,y: x * y
multiply(10, 8)

numbers = [1, 2, 3, 4]

result = map(lambda x: x + 10, numbers)

print(list(result))

numbers = [1, 2, 3, 4, 5, 6]

pairs = filter(lambda x: x % 2 == 0, numbers)

print(list(pairs))

# Décorateur: permet d'ajouter un comportement à une fonction

def mon_decorateur(fonction: any) -> None:
    def enveloppe():
        print("Exécuté avant la fonction principale")
        fonction()
        print("Exécuté après la fonction principale")
    return enveloppe

@mon_decorateur
def dit_bonjour() -> None:
    print("Bonjour!")

dit_bonjour()

# Context

import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try:
        
        yield cursor

    finally:
        conn.commit()
        conn.close()


# with database_connection('exemple.db') as cursor:
#     cursor.execute('SELECT * FROM users')
#     print(cursor.fetchall())

# Itérables et itérateurs

numbers = [1, 2, 3, 4]

it = iter(numbers)

print(next(it, 'not found'))
print(next(it, 'not found'))
print(next(it, 'not found'))
print(next(it, 'not found'))
print(next(it, 'not found'))

numbers = [1, 3, 7, 9, 15, 17, 4]

# Trouve le premier nombre pair
first_even = next((n for n in numbers if n % 2 == 0), None)
print(first_even)


# Imports
from math import sqrt, pi
from datetime import datetime as dt
from math_utils import add, substract

print(sqrt(9))
print(pi)

print(dt.now())

print(add(10, 5))
print(substract(10, 5))