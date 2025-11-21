class ClinicAppointment:
    def __init__(self):
        self.appointments = {}
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.max_per_slot = 3

    def book_appointment(self):
        print("\n--- Book Appointment ---")
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")

        if doctor not in self.appointments:
            self.appointments[doctor] = {s: [] for s in self.slots}

        print("\nAvailable Slots:")
        for s in self.slots:
            count = len(self.appointments[doctor][s])
            print(f"{s} -> {count}/3 booked")

        slot = input("Choose a slot: ")

        if slot not in self.slots:
            print("❌ Invalid Slot!")
            return

        if len(self.appointments[doctor][slot]) >= self.max_per_slot:
            print("❌ Slot Full! Try another.")
            return

        self.appointments[doctor][slot].append({
            "name": name,
            "age": age,
            "mobile": mobile
        })

        print(f"✔ Appointment booked with Dr. {doctor} at {slot}")

    def view_appointment(self):
        print("\n--- View Appointment ---")
        mobile = input("Enter mobile number: ")

        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for p in patients:
                    if p["mobile"] == mobile:
                        print("\n✔ Appointment Found:")
                        print(f"Name: {p['name']}")
                        print(f"Doctor: {doctor}")
                        print(f"Slot: {slot}")
                        print(f"Age: {p['age']}")
                        return
        print("❌ No appointment found.")

    def cancel_appointment(self):
        print("\n--- Cancel Appointment ---")
        mobile = input("Enter mobile number: ")

        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for p in patients:
                    if p["mobile"] == mobile:
                        patients.remove(p)
                        print("✔ Appointment cancelled successfully.")
                        return
        print("❌ No appointment found to cancel.")

    def doctor_availability(self):
        print("\n--- Doctor Availability ---")
        doctor = input("Enter doctor name: ")

        if doctor not in self.appointments:
            print("❌ No such doctor or no bookings yet.")
            return

        print(f"\nAvailability for Dr. {doctor}:")
        for s in self.slots:
            count = len(self.appointments[doctor][s])
            print(f"{s}: {count}/3 booked")

def main():
    clinic = ClinicAppointment()

    while True:
        print("\n========== Clinic Appointment System ==========")
        print("1. Book Appointment")
        print("2. View Appointment")
        print("3. Cancel Appointment")
        print("4. Doctor Availability")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            clinic.book_appointment()

        elif choice == "2":
            clinic.view_appointment()

        elif choice == "3":
            clinic.cancel_appointment()

        elif choice == "4":
            clinic.doctor_availability()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()