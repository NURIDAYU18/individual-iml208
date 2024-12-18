import datetime
import random

class BookingSystem:
    def __init__(self):
        self.customers = []
        self.room_numbers = []
        self.customer_ids = []
        self.package_prices = {
            'REDANG ISLAND': 250,
            'PERHENTIAN ISLAND': 300,
            'HATYAI, THAILAND': 350,
            'PHUKET, THAILAND': 450
        }

    def validate_date(self, date_str):
        """Validates the date format."""
        try:
            datetime.datetime.strptime(date_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def date_difference(self, checkin, checkout):
        """Returns the number of days between check-in and check-out."""
        ci = datetime.datetime.strptime(checkin, '%d/%m/%Y')
        co = datetime.datetime.strptime(checkout, '%d/%m/%Y')
        return (co - ci).days

    def is_valid_checkout(self, checkin, checkout):
        """Checks if check-out is after check-in."""
        return self.date_difference(checkin, checkout) > 0

    def generate_unique_room_and_id(self):
        """Generate a unique room number and customer ID."""
        while True:
            room_number = random.randint(300, 359)
            customer_id = random.randint(10, 59)
            if room_number not in self.room_numbers and customer_id not in self.customer_ids:
                self.room_numbers.append(room_number)
                self.customer_ids.append(customer_id)
                return room_number, customer_id

    def book_package(self):
        """Handle the booking process for a new customer."""
        print("---- Booking New Package ----")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")

        # Validate that all fields are filled
        while not name or not phone or not address:
            print("\nName, Phone number & Address cannot be empty.")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
        
        # Get check-in and check-out dates
        checkin = input("Enter Check-In date (dd/mm/yyyy): ")
        while not self.validate_date(checkin):
            print("Invalid Check-In date format. Please try again.")
            checkin = input("Enter Check-In date (dd/mm/yyyy): ")

        checkout = input("Enter Check-Out date (dd/mm/yyyy): ")
        while not self.validate_date(checkout):
            print("Invalid Check-Out date format. Please try again.")
            checkout = input("Enter Check-Out date (dd/mm/yyyy): ")

        if not self.is_valid_checkout(checkin, checkout):
            print("\nError: Check-Out date must be after Check-In date.")
            return  # Return to restart the booking process
        
        # Calculate the days of stay
        days = self.date_difference(checkin, checkout)
        
        print("----SELECT PACKAGE TYPE----")
        print(" 1. REDANG ISLAND")
        print(" 2. PERHENTIAN ISLAND")
        print(" 3. HATYAI, THAILAND")
        print(" 4. PHUKET, THAILAND")
        
        # Select package
        package_choice = int(input("Choose a package: "))
        if package_choice == 1:
            room_type = 'REDANG ISLAND'
            price = 250
        elif package_choice == 2:
            room_type = 'PERHENTIAN ISLAND'
            price = 300
        elif package_choice == 3:
            room_type = 'HATYAI, THAILAND'
            price = 350
        elif package_choice == 4:
            room_type = 'PHUKET, THAILAND'
            price = 450
        else:
            print("Invalid choice, please try again.")
            return  # Restart booking if the choice is invalid
        
        # Generate unique room number and customer ID
        room_number, customer_id = self.generate_unique_room_and_id()

        # Store customer data
        self.customers.append({
            'name': name,
            'phone': phone,
            'address': address,
            'checkin': checkin,
            'checkout': checkout,
            'room_type': room_type,
            'price': price,
            'days': days,
            'room_number': room_number,
            'customer_id': customer_id
        })

        print(f"\nBooking successful!\nRoom Number: {room_number}\nCustomer ID: {customer_id}")

    def show_records(self):
        """Display all booking records."""
        if not self.customers:
            print("No bookings found.")
            return
        print("\n--- Booking Records ---")
        for customer in self.customers:
            total_price = customer['price'] * customer['days']
            print(f"\nName: {customer['name']}\nPhone: {customer['phone']}\nAddress: {customer['address']}")
            print(f"Check-In: {customer['checkin']}, Check-Out: {customer['checkout']}")
            print(f"Room Type: {customer['room_type']}\nTotal Price: RM {total_price}")

    def update_record(self):
        """Update a customer record based on their phone number."""
        phone = input("Enter the phone number of the customer to update: ")
        customer_to_update = next((cust for cust in self.customers if cust['phone'] == phone), None)
        
        if customer_to_update:
            print(f"--- Current details for {customer_to_update['name']} ---")
            print(f"Name: {customer_to_update['name']}")
            print(f"Phone: {customer_to_update['phone']}")
            print(f"Address: {customer_to_update['address']}")
            print(f"Check-In: {customer_to_update['checkin']}")
            print(f"Check-Out: {customer_to_update['checkout']}")
            print(f"Room Type: {customer_to_update['room_type']}")
            print(f"Total Price: RM {customer_to_update['price'] * customer_to_update['days']}")
            
            print("\n--- Update Fields ---")
            name = input(f"Enter new name (current: {customer_to_update['name']}): ") or customer_to_update['name']
            phone = input(f"Enter new phone number (current: {customer_to_update['phone']}): ") or customer_to_update['phone']
            address = input(f"Enter new address (current: {customer_to_update['address']}): ") or customer_to_update['address']
            checkin = input(f"Enter new check-in date (current: {customer_to_update['checkin']}): ") or customer_to_update['checkin']
            checkout = input(f"Enter new check-out date (current: {customer_to_update['checkout']}): ") or customer_to_update['checkout']
            room_type = input(f"Enter new room type (current: {customer_to_update['room_type']}): ") or customer_to_update['room_type']
            
            # Validate new dates
            while not self.validate_date(checkin):
                print("Invalid Check-In date format. Please try again.")
                checkin = input("Enter Check-In date (dd/mm/yyyy): ")

            while not self.validate_date(checkout):
                print("Invalid Check-Out date format. Please try again.")
                checkout = input("Enter Check-Out date (dd/mm/yyyy): ")

            if not self.is_valid_checkout(checkin, checkout):
                print("\nError: Check-Out date must be after Check-In date.")
                return  # Do not update if the dates are invalid
            
            # Update the customer record
            customer_to_update['name'] = name
            customer_to_update['phone'] = phone
            customer_to_update['address'] = address
            customer_to_update['checkin'] = checkin
            customer_to_update['checkout'] = checkout
            customer_to_update['room_type'] = room_type

            # Recalculate the number of days for the new dates
            customer_to_update['days'] = self.date_difference(checkin, checkout)
            print("\nBooking updated successfully!")
        else:
            print("No booking found with that phone number.")

    def delete_record(self):
        """Delete a customer record based on their phone number."""
        phone = input("Enter the phone number of the customer to delete: ")
        customer_to_delete = next((cust for cust in self.customers if cust['phone'] == phone), None)
        
        if customer_to_delete:
            self.customers.remove(customer_to_delete)
            print("\nBooking deleted successfully!")
        else:
            print("No booking found with that phone number.")

# Main Function
def home():
    booking_system = BookingSystem()
    
    while True:
        print("\n\t\t\t\t WELCOME TO PORORO TRAVEL\n")
        print("1. Book a Package\n2. Show Records\n3. Update Record\n4. Delete Existence Data\n0. Exit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            booking_system.book_package()
        elif choice == 2:
            booking_system.show_records()
        elif choice == 3:
            booking_system.update_record()
        elif choice == 4:
            booking_system.delete_record()
        elif choice == 0:
            print("Thank you for using Pororo Travel!")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program
if __name__ == "__main__":
    home()
