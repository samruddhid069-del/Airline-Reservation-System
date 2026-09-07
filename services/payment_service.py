from ARS.models.payment import Payment

class PaymentService:

    def __init__(self):
        self.payment_list = []

    def make_payment(self, booking):

        payment_id = input("Enter Payment ID: ")
        amount = booking.flight.price
        method = input("Enter Payment Method: ")

        payment = Payment(payment_id, booking, amount, method)
        self.payment_list.append(payment)

        print("Payment Successful.")

    def view_payments(self):
        if not self.payment_list:
            print("No payments found.")
            return

        for p in self.payment_list:
            print(p.payment_id, p.amount, p.method)