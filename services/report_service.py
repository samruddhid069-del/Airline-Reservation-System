class ReportService:

    def generate_report(self, flights, bookings):

        print("\n===== REPORT =====")

        print("Total Flights:", len(flights))
        print("Total Bookings:", len(bookings))

        total_revenue = 0

        for b in bookings:
            total_revenue += b.flight.price

        print("Total Revenue:", total_revenue)