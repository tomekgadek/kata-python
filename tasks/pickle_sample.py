"""
    Jak dziala modul 'pickle'?

    Modul pickle umozliwia serializacje i deserializacje struktur / obiektow 
    (w tym konkretnym przypadku jest to slownik) z / do pliku.
"""

import pickle

class Database:
    def __init__(self, name):
        self.name = name
    
    def save(self, data):
        file = open(self.name, "wb") # otworz plik do zapisu w trybie binarnym
        pickle.dump(data, file) # zapisz obiekt do pliku
        file.close()
    
    def read(self):
        file = open(self.name, "rb") # otworz plik do odczytu w trybie binarnym
        data = pickle.load(file) # odczytaj obiekt z pliku
        file.close()

        return data

students = { 
    "14910": "John Doe",
    "12345": "Mike Tyson"
}

students_database = Database("students.dat")
students_database.save(students)

load_students = students_database.read()

print(load_students)

"""
    Output:

    {'14910': 'John Doe', '12345': 'Mike Tyson'}
"""