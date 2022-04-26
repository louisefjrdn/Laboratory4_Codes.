import datetime

class Person:

    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate



    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Roma Eloisa",
    "Fajardan",
    datetime.date(2002, 3, 6), # year, month, day

)

print(person.name)
print(person.age())