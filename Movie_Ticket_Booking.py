import uuid

def print_headline():
    print("=" * 90 + "\n")
    print("                             \U0001F3AC WELCOME TO MOVIES & MAGIC \U0001F39F️")
    print("                      Your One-Stop Movie Ticket Booking Platform")
    print("\n" + "=" * 90 + "\n")

def select_city():
    print_headline()
    print("Hi! Welcome to movie ticket booking platform \U0001F3A5")
    print("Where do you want to watch the movie?")
    cities = {1: "Mumbai", 2: "Delhi", 3: "Kolkata", 4: "Bengaluru", 5: "Chennai"}
    for k, v in cities.items():
        print(f"{k}. {v}")
    try:
        choice = int(input("Choose your option: "))
        if choice in cities:
            select_theater()
        else:
            print("Invalid city choice.")
    except ValueError:
        print("Please enter a valid number.")

def select_theater():
    print("\n" + "=" * 90 + "\n")
    print("Select a theater:")
    theaters = {1: "PVR", 2: "Inox", 3: "Cinepolis", 4: "MovieMax", 5: "Back"}
    for k, v in theaters.items():
        print(f"{k}. {v}")
    try:
        choice = int(input("Choose your option: "))
        if choice in [1, 2, 3, 4]:
            select_movie()
        elif choice == 5:
            select_city()
        else:
            print("Invalid theater choice.")
    except ValueError:
        print("Please enter a valid number.")

def select_movie():
    print("\n" + "=" * 90 + "\n")
    print("Which movie do you want to watch?")
    movies = {
        1: "Memento \U0001F556", 2: "Prestige \U0001F4A1", 3: "Inception \U0001F4AD", 4: "Interstellar \U0001F680",
        5: "Dunkirk \U0001F6E6", 6: "Tenet \U0001F697", 7: "Oppenheimer \U0001F4A3", 8: "Back"
    }
    for k, v in movies.items():
        print(f"{k}. {v}")
    try:
        choice = int(input("Choose your movie: "))
        if choice in range(1, 8):
            proceed_to_booking(movies[choice])
        elif choice == 8:
            select_theater()
        else:
            print("Invalid movie choice.")
    except ValueError:
        print("Please enter a valid number.")

def proceed_to_booking(movie_name):
    ticket_types = {
        1: ("Classic", 200),
        2: ("Prime", 300),
        3: ("Recliner", 500)
    }

    rows = ["A", "B", "C", "D"]
    cols = [1, 2, 3, 4, 5]
    seats = {row: [f"{row}{col}" for col in cols] for row in rows}

    print("\n" + "=" * 90 + "\n")
    print("Select screen:")
    for i in range(1, 4):
        print(f"{i}. SCREEN {i}")
    try:
        screen = int(input("Choose your screen: "))
        if screen not in [1, 2, 3]:
            print("Invalid screen choice.")
            return

        print("\n" + "=" * 90 + "\n")
        print("Choose ticket type:")
        for k, v in ticket_types.items():
            print(f"{k}. {v[0]} - ₹{v[1]}")
        ticket_type = int(input("Enter your ticket type: "))
        if ticket_type not in ticket_types:
            print("Invalid ticket type.")
            return

        ticket_count = int(input("Number of tickets: "))
        ticket_name, ticket_price = ticket_types[ticket_type]
        total_price = ticket_price * ticket_count

        print("\n" + "=" * 90 + "\n")
        print("Available Seats:\n")
        for row in rows:
            print(f"{row} |", end=" ")
            for seat in seats[row]:
                print(seat, end="  ")
            print()

        selected_seats = []
        for i in range(ticket_count):
            while True:
                seat_input = input(f"Select seat #{i+1}: ").upper()
                found = False
                for row in seats:
                    if seat_input in seats[row]:
                        seats[row].remove(seat_input)
                        selected_seats.append(seat_input)
                        found = True
                        break
                if found:
                    break
                else:
                    print("❌ Seat not available or invalid. Try again.")

        # 🎉 Add Food Section
        food_menu = {
            1: ("Popcorn", 200),
            2: ("Burger", 250),
            3: ("Cold Drink", 150),
            4: ("Nachos", 300),
            5: ("Combo (Popcorn + Drink)", 300),
            6: ("Skip", 0)
        }
        print("\n" + "=" * 90 + "\n")
        print("🍿 Add Food to Your Booking:")
        for k, v in food_menu.items():
            print(f"{k}. {v[0]} - ₹{v[1]}")
        food_choice = int(input("Select food option: "))
        food_name, food_price = food_menu.get(food_choice, ("None", 0))
        total_price += food_price

        # 🎟️ Apply Discount Coupon
        print("\nDo you have a coupon code? (e.g., MAGIC10 for 10% off)")
        coupon = input("Enter coupon code (or press Enter to skip): ").strip().upper()
        discount = 0
        if coupon == "MAGIC10":
            discount = int(0.10 * total_price)
            total_price -= discount
            print(f"✅ Coupon applied! You saved ₹{discount}.")

        print("\n" + "=" * 90 + "\n")
        print(f"🧾 You selected {ticket_name} ticket(s) × {ticket_count}")
        print("🎫 Seats:", ", ".join(selected_seats))
        print(f"🍔 Food  : {food_name}")
        print(f"💰 Total Price: ₹{total_price}")
        confirm = input("Do you want to continue with booking? (y/n): ").strip().lower()
        if confirm == "y":
            select_time(screen, ticket_name, ticket_count, selected_seats, total_price, movie_name, food_name, discount)
        else:
            print("❌ Booking cancelled.")
    except ValueError:
        print("Please enter a valid number.")


def select_time(screen, ticket_name, ticket_count, seats, total_price, movie_name, food_name, discount):
    times = {
        1: {"1": "10.00 AM - 1.00 PM", "2": "1.15 PM - 4.15 PM", "3": "4.30 PM - 7.30 PM", "4": "7.45 PM - 10.45 PM"},
        2: {"1": "10.15 AM - 1.15 PM", "2": "1.30 PM - 4.30 PM", "3": "4.45 PM - 7.45 PM", "4": "8.00 PM - 11.00 PM"},
        3: {"1": "10.30 AM - 1.30 PM", "2": "1.45 PM - 4.45 PM", "3": "5.00 PM - 8.00 PM", "4": "8.15 PM - 11.15 PM"}
    }

    print("\n" + "=" * 90 + "\n")
    print("Choose your time:")
    for k, v in times[screen].items():
        print(f"{k}. {v}")
    t = input("Select your time: ")
    if t in times[screen]:
        booking_time = times[screen][t]
        booking_id = str(uuid.uuid4())[:8]
        print("\n" + "=" * 90 + "\n")
        print("\U0001F39F️ Booking Confirmed!")
        print("-" * 40)
        print(f"Booking ID   : {booking_id}")
        print(f"Movie        : {movie_name}")
        print(f"Ticket Type  : {ticket_name}")
        print(f"Tickets      : {ticket_count}")
        print(f"Seats        : {', '.join(seats)}")
        print(f"Screen       : {screen}")
        print(f"Show Time    : {booking_time}")
        print(f"Food         : {food_name}")
        if discount:
            print(f"Discount     : ₹{discount}")
        print(f"Total Amount : ₹{total_price}")
        print("-" * 40)
        print("✅ Enjoy your movie!")
    else:
        print("❌ Invalid time choice.")


# Start the program
select_city()
