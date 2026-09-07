class Ticket:

    def __init__(self,
                 ticket_no,
                 booking_id):

        self.ticket_no = ticket_no
        self.booking_id = booking_id

    def display(self):

        print("Ticket No :", self.ticket_no)
        print("Booking :", self.booking_id)