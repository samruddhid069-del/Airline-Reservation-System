class Passenger:

    def __init__(self, pid, name, age, gender, phone):

        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display(self):

        print(self.pid,
              self.name,
              self.age,
              self.gender,
              self.phone)