# from services.flight_service import FlightService
# from services.passenger_service import PassengerService
# from services.booking_service import BookingService
# from services.payment_service import PaymentService
# from services.admin_service import AdminService
# from services.report_service import ReportService


# from ARS.utils.flight_menu import main_menu

# def main():

#     flight_service = FlightService()
#     passenger_service = PassengerService()
#     booking_service = BookingService()
#     payment_service = PaymentService()
#     report_service = ReportService()

#     while True:

#         choice = main_menu()

#         # -------- Flight --------
#         if choice == 1:
#             flight_service.flight_menu()

#         # -------- Passenger --------
#         elif choice == 2:

#             while True:
#                 print("\n--- Passenger Menu ---")
#                 print("1. Add Passenger")
#                 print("2. View Passengers")
#                 print("3. Search Passenger")
#                 print("4. Back")

#                 ch = int(input("Enter choice: "))

#                 if ch == 1:
#                     passenger_service.add_passenger()
#                 elif ch == 2:
#                     passenger_service.view_passengers()
#                 elif ch == 3:
#                     passenger_service.search_passenger()
#                 elif ch == 4:
#                     break
#                 else:
#                     print("Invalid choice.")

#         # -------- Booking --------
#         elif choice == 3:

#             passenger = passenger_service.search_passenger()
#             if passenger is None:
#                 continue

#             flight = flight_service.search_flight()
#             if flight is None:
#                 continue

#             booking_service.create_booking(passenger, flight)

#         # -------- Payment --------
#         elif choice == 4:

#             booking_service.view_bookings()
#             if not booking_service.booking_list:
#                 continue

#             booking = booking_service.booking_list[-1]  # latest booking
#             payment_service.make_payment(booking)

#         # -------- Reports --------
#         elif choice == 5:
#             report_service.generate_report(
#                 flight_service.flight_list,
#                 booking_service.booking_list
#             )

#         # -------- Exit --------
#         elif choice == 6:
#             print("Thank you for using system.")
#             break

#         else:
#             print("Invalid choice.")


# if __name__ == "__main__":
#     main()




# from services.flight_service import FlightService
# from services.passenger_service import PassengerService
# from services.booking_service import BookingService
# from services.payment_service import PaymentService
# from services.report_service import ReportService


# def admin_menu():
#     print("\n========== ADMIN MENU ==========")
#     print("1. Flight Management")
#     print("2. Passenger Management")
#     print("3. Booking")
#     print("4. Payment")
#     print("5. Reports")
#     print("6. Logout")

#     return int(input("Enter your choice: "))


# def passenger_menu():
#     print("\n========== PASSENGER MENU ==========")
#     print("1. Search Flight")
#     print("2. Book Ticket")
#     print("3. Make Payment")
#     print("4. Back")

#     return int(input("Enter your choice: "))


# def main():

#     flight_service = FlightService()
#     passenger_service = PassengerService()
#     booking_service = BookingService()
#     payment_service = PaymentService()
#     report_service = ReportService()

#     while True:

#         print("\n========================================")
#         print("      AIRLINE RESERVATION SYSTEM")
#         print("========================================")
#         print("1. Admin")
#         print("2. Passenger")
#         print("3. Exit")

#         role = int(input("Enter your choice: "))

#         # ================= ADMIN =================
#         if role == 1:

#             while True:

#                 choice = admin_menu()

#                 # Flight
#                 if choice == 1:
#                     flight_service.flight_menu()

#                 # Passenger Management
#                 elif choice == 2:

#                     while True:

#                         print("\n----- Passenger Management -----")
#                         print("1. Add Passenger")
#                         print("2. View Passengers")
#                         print("3. Search Passenger")
#                         print("4. Back")

#                         ch = int(input("Enter choice: "))

#                         if ch == 1:
#                             passenger_service.add_passenger()

#                         elif ch == 2:
#                             passenger_service.view_passengers()

#                         elif ch == 3:
#                             passenger_service.search_passenger()

#                         elif ch == 4:
#                             break

#                         else:
#                             print("Invalid choice.")

#                 # Booking
#                 elif choice == 3:

#                     passenger = passenger_service.search_passenger()

#                     if passenger is None:
#                         continue

#                     flight = flight_service.search_flight()

#                     if flight is None:
#                         continue

#                     booking_service.create_booking(passenger, flight)

#                 # Payment
#                 elif choice == 4:

#                     booking_service.view_bookings()

#                     if not booking_service.booking_list:
#                         continue

#                     booking = booking_service.booking_list[-1]
#                     payment_service.make_payment(booking)

#                 # Reports
#                 elif choice == 5:

#                     report_service.generate_report(
#                         flight_service.flight_list,
#                         booking_service.booking_list
#                     )

#                 # Logout
#                 elif choice == 6:
#                     break

#                 else:
#                     print("Invalid choice.")

#         # ================= PASSENGER =================
#         elif role == 2:

#             while True:

#                 choice = passenger_menu()

#                 # Search Flight
#                 if choice == 1:
#                     flight_service.search_flight()

#                 # Book Ticket
#                 elif choice == 2:

#                     passenger = passenger_service.search_passenger()

#                     if passenger is None:
#                         continue

#                     flight = flight_service.search_flight()

#                     if flight is None:
#                         continue

#                     booking_service.create_booking(passenger, flight)

#                 # Payment
#                 elif choice == 3:

#                     booking_service.view_bookings()

#                     if not booking_service.booking_list:
#                         continue

#                     booking = booking_service.booking_list[-1]
#                     payment_service.make_payment(booking)

#                 # Back
#                 elif choice == 4:
#                     break

#                 else:
#                     print("Invalid choice.")

#         # ================= EXIT =================
#         elif role == 3:
#             print("\nThank you for using Airline Reservation System.")
#             break

#         else:
#             print("Invalid choice.")


# if __name__ == "__main__":
#     main()





from services.flight_service import FlightService
from services.passenger_service import PassengerService
from services.booking_service import BookingService
from services.payment_service import PaymentService
from services.report_service import ReportService


def admin_menu():
    print("\n========== ADMIN MENU ==========")
    print("1. Flight Management")
    print("2. Passenger Management")
    print("3. Booking")
    print("4. Payment")
    print("5. Reports")
    print("6. Logout")

    return int(input("Enter your choice: "))


def passenger_menu():
    print("\n========== PASSENGER MENU ==========")
    print("1. Register Passenger")
    print("2. Search Flight")
    print("3. Book Ticket")
    print("4. View My Bookings")
    print("5. Make Payment")
    print("6. Back")

    return int(input("Enter your choice: "))


def main():

    flight_service = FlightService()
    passenger_service = PassengerService()
    booking_service = BookingService()
    payment_service = PaymentService()
    report_service = ReportService()

    while True:

        print("\n========================================")
        print("      AIRLINE RESERVATION SYSTEM")
        print("========================================")
        print("1. Admin")
        print("2. Passenger")
        print("3. Exit")

        role = int(input("Enter your choice: "))

        # ================= ADMIN =================
        if role == 1:

            while True:

                choice = admin_menu()

                # Flight Management
                if choice == 1:
                    flight_service.flight_menu()

                # Passenger Management
                elif choice == 2:

                    while True:

                        print("\n========== PASSENGER MANAGEMENT ==========")
                        print("1. Add Passenger")
                        print("2. View Passengers")
                        print("3. Search Passenger")
                        print("4. Update Passenger")
                        print("5. Delete Passenger")
                        print("6. Back")

                        ch = int(input("Enter your choice: "))

                        if ch == 1:
                            passenger_service.add_passenger()

                        elif ch == 2:
                            passenger_service.view_passengers()

                        elif ch == 3:
                            passenger_service.search_passenger()

                        elif ch == 4:
                            passenger_service.update_passenger()

                        elif ch == 5:
                            passenger_service.delete_passenger()

                        elif ch == 6:
                            break

                        else:
                            print("Invalid choice.")

                # Booking
                elif choice == 3:

                    passenger = passenger_service.search_passenger()

                    if passenger is None:
                        continue

                    flight = flight_service.search_flight()

                    if flight is None:
                        continue

                    booking_service.create_booking(passenger, flight)

                # Payment
                elif choice == 4:

                    booking_service.view_bookings()

                    if not booking_service.booking_list:
                        print("No bookings available.")
                        continue

                    booking = booking_service.booking_list[-1]
                    payment_service.make_payment(booking)

                # Reports
                elif choice == 5:

                    report_service.generate_report(
                        flight_service.flight_list,
                        booking_service.booking_list
                    )

                # Logout
                elif choice == 6:
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid choice.")

        # ================= PASSENGER =================
        elif role == 2:

            while True:

                choice = passenger_menu()

                # Register Passenger
                if choice == 1:
                    passenger_service.add_passenger()

                # Search Flight
                elif choice == 2:
                    flight_service.search_flight()

                # Book Ticket
                elif choice == 3:

                    passenger = passenger_service.search_passenger()

                    if passenger is None:
                        print("Passenger not found. Please register first.")
                        continue

                    flight = flight_service.search_flight()

                    if flight is None:
                        continue

                    booking_service.create_booking(passenger, flight)

                # View My Bookings
                elif choice == 4:

                    booking_service.view_bookings()

                # Payment
                elif choice == 5:

                    booking_service.view_bookings()

                    if not booking_service.booking_list:
                        print("No bookings available.")
                        continue

                    booking = booking_service.booking_list[-1]
                    payment_service.make_payment(booking)

                # Back
                elif choice == 6:
                    break

                else:
                    print("Invalid choice.")

        # ================= EXIT =================
        elif role == 3:
            print("\nThank you for using Airline Reservation System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()