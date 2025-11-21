class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Mysore": 450,
            "Ahmedabad to Surat": 300
        }

        self.tickets = {}
        self.seats_booked = {route: 0 for route in self.routes}
        self.next_ticket_id = 1

    def show_routes(self):
        print("\n--- Available Routes ---")
        for route, price in self.routes.items():
            seats = self.seats_booked[route]
            print(f"{route} - ₹{price} | Seats booked: {seats}/40")

    def book_ticket(self):
        print("\n--- Book Ticket ---")
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        print("\nSelect Route:")
        route_list = list(self.routes.keys())

        for i, r in enumerate(route_list, 1):
            print(f"{i}. {r} - ₹{self.routes[r]}")

        choice = int(input("Choose route (1-4): "))

        if choice < 1 or choice > len(route_list):
            print("Invalid route.")
            return

        route = route_list[choice - 1]

        if self.seats_booked[route] >= 40:
            print("No seats available on this route.")
            return

        self.seats_booked[route] += 1
        seat_no = self.seats_booked[route]
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "price": self.routes[route]
        }

        print(f"\nTicket Booked Successfully!")
        print(f"Ticket ID: {ticket_id}")
        print(f"Seat No: {seat_no}")

    def view_ticket(self):
        print("\n--- View Ticket ---")
        ticket_id = int(input("Enter ticket ID: "))

        if ticket_id in self.tickets:
            t = self.tickets[ticket_id]
            print("\n✔ Ticket Details:")
            print(f"Name: {t['name']}")
            print(f"Age: {t['age']}")
            print(f"Mobile: {t['mobile']}")
            print(f"Route: {t['route']}")
            print(f"Seat No: {t['seat']}")
            print(f"Price: ₹{t['price']}")
        else:
            print("❌ Ticket not found.")

    def cancel_ticket(self):
        print("\n--- Cancel Ticket ---")
        ticket_id = int(input("Enter ticket ID: "))

        if ticket_id in self.tickets:
            route = self.tickets[ticket_id]["route"]

            self.seats_booked[route] -= 1

            del self.tickets[ticket_id]
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")

def main():
    system = BusReservation()

    while True:
        print("\n========== Bus Reservation System ==========")
        print("1. Show Available Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            system.show_routes()
        elif choice == "2":
            system.book_ticket()
        elif choice == "3":
            system.view_ticket()
        elif choice == "4":
            system.cancel_ticket()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()