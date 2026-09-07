from ARS.models.flight import Flight

class FlightService:

    def __init__(self):
        self.flight_list = []

    # ---------------- Add Flight ----------------
    def add_flight(self):

        flight_no = input("Enter Flight Number: ")

        # Check duplicate flight number
        for flight in self.flight_list:
            if flight.flight_no == flight_no:
                print("Flight already exists.")
                return

        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        departure = input("Enter Departure Time: ")
        arrival = input("Enter Arrival Time: ")
        price = float(input("Enter Ticket Price: "))
        total_seats = int(input("Enter Total Seats: "))

        flight = Flight(
            flight_no,
            source,
            destination,
            departure,
            arrival,
            price,
            total_seats
        )

        self.flight_list.append(flight)

        print("\nFlight Added Successfully.")

    # ---------------- View Flights ----------------
    def view_flights(self):

        if len(self.flight_list) == 0:
            print("\nNo Flights Available.")
            return

        print("\n========== FLIGHT LIST ==========")

        for flight in self.flight_list:

            print("-----------------------------------")
            print("Flight No :", flight.flight_no)
            print("Source :", flight.source)
            print("Destination :", flight.destination)
            print("Departure :", flight.departure)
            print("Arrival :", flight.arrival)
            print("Price :", flight.price)
            print("Total Seats :", flight.total_seats)
            print("Booked Seats :", flight.booked_seats)
            print("Available Seats :", flight.total_seats - flight.booked_seats)

    # ---------------- Search Flight ----------------
    def search_flight(self):

        flight_no = input("Enter Flight Number: ")

        for flight in self.flight_list:

            if flight.flight_no == flight_no:

                print("\nFlight Found")
                print("---------------------------")
                print("Flight No :", flight.flight_no)
                print("Source :", flight.source)
                print("Destination :", flight.destination)
                print("Departure :", flight.departure)
                print("Arrival :", flight.arrival)
                print("Price :", flight.price)
                print("Available Seats :", flight.total_seats - flight.booked_seats)

                return flight

        print("Flight Not Found.")
        return None

    # ---------------- Update Flight ----------------
    def update_flight(self):

        flight_no = input("Enter Flight Number to Update: ")

        for flight in self.flight_list:

            if flight.flight_no == flight_no:

                print("\nEnter New Details")

                flight.source = input("Source: ")
                flight.destination = input("Destination: ")
                flight.departure = input("Departure Time: ")
                flight.arrival = input("Arrival Time: ")
                flight.price = float(input("Price: "))
                flight.total_seats = int(input("Total Seats: "))

                print("Flight Updated Successfully.")
                return

        print("Flight Not Found.")

    # ---------------- Delete Flight ----------------
    def delete_flight(self):

        flight_no = input("Enter Flight Number to Delete: ")

        for flight in self.flight_list:

            if flight.flight_no == flight_no:

                self.flight_list.remove(flight)

                print("Flight Deleted Successfully.")
                return

        print("Flight Not Found.")

    # ---------------- Seat Availability ----------------
    def seat_availability(self):

        flight_no = input("Enter Flight Number: ")

        for flight in self.flight_list:

            if flight.flight_no == flight_no:

                available = flight.total_seats - flight.booked_seats

                print("Available Seats :", available)
                return available

        print("Flight Not Found.")
        return 0

    # ---------------- Flight Menu ----------------
    def flight_menu(self):

        while True:

            print("\n========== FLIGHT MANAGEMENT ==========")
            print("1. Add Flight")
            print("2. Update Flight")
            print("3. Delete Flight")
            print("4. View Flights")
            print("5. Search Flight")
            print("6. Seat Availability")
            print("7. Back")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.add_flight()

            elif choice == 2:
                self.update_flight()

            elif choice == 3:
                self.delete_flight()

            elif choice == 4:
                self.view_flights()

            elif choice == 5:
                self.search_flight()

            elif choice == 6:
                self.seat_availability()

            elif choice == 7:
                break

            else:
                print("Invalid Choice.")