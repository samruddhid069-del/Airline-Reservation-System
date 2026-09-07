# from ARS.models.passenger import Passenger

# class PassengerService:

#     def __init__(self):
#         self.passenger_list = []

#     def add_passenger(self):
#         pid = input("Enter Passenger ID: ")

#         for p in self.passenger_list:
#             if p.pid == pid:
#                 print("Passenger already exists.")
#                 return

#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         gender = input("Enter Gender: ")

#         passenger = Passenger(pid, name, age, gender)
#         self.passenger_list.append(passenger)

#         print("Passenger Added Successfully.")

#     def view_passengers(self):
#         if not self.passenger_list:
#             print("No passengers found.")
#             return

#         for p in self.passenger_list:
#             print(p.pid, p.name, p.age, p.gender)

#     def search_passenger(self):
#         pid = input("Enter Passenger ID: ")

#         for p in self.passenger_list:
#             if p.pid == pid:
#                 print("Passenger Found:", p.name)
#                 return p

#         print("Passenger Not Found.")
#         return None



from ARS.models.passenger import Passenger


class PassengerService:

    def __init__(self):
        self.passenger_list = []

    # Add Passenger
    def add_passenger(self):

        pid = input("Enter Passenger ID: ")

        for p in self.passenger_list:
            if p.pid == pid:
                print("Passenger already exists.")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        phone = input("Enter Phone Number: ")

        passenger = Passenger(pid, name, age, gender, phone)

        self.passenger_list.append(passenger)

        print("\nPassenger Added Successfully.")

    # View All Passengers
    def view_passengers(self):

        if len(self.passenger_list) == 0:
            print("\nNo Passenger Found.")
            return

        print("\n========== Passenger List ==========")

        for p in self.passenger_list:
            print("----------------------------------")
            print("Passenger ID :", p.pid)
            print("Name         :", p.name)
            print("Age          :", p.age)
            print("Gender       :", p.gender)
            print("Phone        :", p.phone)

    # Search Passenger
    def search_passenger(self):

        pid = input("Enter Passenger ID: ")

        for p in self.passenger_list:
            if p.pid == pid:
                print("\nPassenger Found")
                print("---------------------------")
                print("Passenger ID :", p.pid)
                print("Name         :", p.name)
                print("Age          :", p.age)
                print("Gender       :", p.gender)
                print("Phone        :", p.phone)
                return p

        print("\nPassenger Not Found.")
        return None

    # Delete Passenger
    def delete_passenger(self):

        pid = input("Enter Passenger ID to Delete: ")

        for p in self.passenger_list:
            if p.pid == pid:
                self.passenger_list.remove(p)
                print("Passenger Deleted Successfully.")
                return

        print("Passenger Not Found.")

    # Update Passenger
    def update_passenger(self):

        pid = input("Enter Passenger ID: ")

        for p in self.passenger_list:
            if p.pid == pid:

                p.name = input("Enter New Name: ")
                p.age = int(input("Enter New Age: "))
                p.gender = input("Enter New Gender: ")
                p.phone = input("Enter New Phone Number: ")

                print("Passenger Updated Successfully.")
                return

        print("Passenger Not Found.")