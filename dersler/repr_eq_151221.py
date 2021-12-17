class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.first_name == other.first_name

john = Person('John', 'Doe', 25)
jane = Person('John', 'Doe', 25)
print(john)
print(jane)
print(john == jane)  # True