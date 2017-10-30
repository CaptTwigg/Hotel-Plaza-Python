import random
from guest import Guest

guests = []


def generateGuest(numberOfGuests, array):

    for i in range(numberOfGuests):
        array.append(Guest(randomFirstName(), randomFirstName(), randomNumber()))


def randomFirstName():
    nameList = ["Jay", "Hae", "Sindy", "Carmon", "Janeth", "Vernon", "Olin", "Inger",
                "Lindsey", "Michael", "Benton", "Marcy", "Caleb", "Olsen", "Cay", "Kenneth"]

    return random.choice(nameList)


def randomNumber():
    return random.randrange(10000000, 99999999)


generateGuest(3, guests)
print(guests[0].toString())
