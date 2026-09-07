from  ARS.models.booking import Booking

class BookingService:

    def __init__(self):
        self.booking_list = []

    def create_booking(self, passenger, flight):

        if flight.total_seats - flight.booked_seats <= 0:
            print("No seats available.")
            return

        booking_id = input("Enter Booking ID: ")

        booking = Booking(booking_id,passenger, flight )
        self.booking_list.append(booking)

        flight.booked_seats += 1

        print("Booking Successful.")


    
    def view_bookings(self):
        if not self.booking_list:
            print("No bookings found.")
            return

        for b in self.booking_list:
            print(b.booking_id, b.passenger.name, b.flight.flight_no)

        