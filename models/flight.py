class Flight:

    def __init__(self, flight_no, source, destination,
                 departure, arrival,
                 price, total_seats):

        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def display(self):
        print("--------------------------------")
        print("Flight No :", self.flight_no)
        print("Source :", self.source)
        print("Destination :", self.destination)
        print("Departure :", self.departure)
        print("Arrival :", self.arrival)
        print("Price :", self.price)
        print("Available :", self.available_seats())