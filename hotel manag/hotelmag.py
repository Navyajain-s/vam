import pymysql  # Instead of mysql.connector

# Connect to the MySQL database
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="navyajain",  # Replace with your MySQL password
        database="hotel_management"
    )


# Client Check-in Module
def client_check_in():
    db = connect_db()
    cursor = db.cursor()

    client_name = input("Enter client name: ")
    print("Available rooms: ")
    cursor.execute("SELECT room_id, room_type, price FROM rooms WHERE is_occupied = FALSE")
    available_rooms = cursor.fetchall()

    if not available_rooms:
        print("Sorry, no rooms are available.")
        db.close()
        return

    for room in available_rooms:
        print(f"Room ID: {room[0]}, Type: {room[1]}, Price: {room[2]}")

    room_id = int(input("Choose a room ID for check-in: "))
    check_in_date = datetime.now().date()
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    cursor.execute("UPDATE rooms SET is_occupied = TRUE WHERE room_id = %s", (room_id,))
    cursor.execute("INSERT INTO clients (client_name, room_id, check_in_date, check_out_date) VALUES (%s, %s, %s, %s)",
                   (client_name, room_id, check_in_date, check_out_date))
    db.commit()

    print(f"Check-in successful for {client_name} in Room {room_id}.")

    db.close()

# Room Service Module
def room_service():
    db = connect_db()
    cursor = db.cursor()

    room_id = int(input("Enter room ID for room service: "))
    service = input("Enter service request (e.g., towels, food, etc.): ")

    # Store room service request (simple logging for now)
    cursor.execute("INSERT INTO room_service (room_id, service_request) VALUES (%s, %s)", (room_id, service))
    db.commit()

    print(f"Room service request for Room {room_id} has been logged: {service}.")
    db.close()

# View Occupied Room Details
def view_occupied_rooms():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT clients.client_name, rooms.room_id, rooms.room_type, clients.check_in_date, clients.check_out_date
        FROM clients
        JOIN rooms ON clients.room_id = rooms.room_id
        WHERE rooms.is_occupied = TRUE
    """)
    occupied_rooms = cursor.fetchall()

    if not occupied_rooms:
        print("No rooms are currently occupied.")
    else:
        print("Occupied Rooms:")
        for row in occupied_rooms:
            print(f"Client: {row[0]}, Room ID: {row[1]}, Room Type: {row[2]}, Check-in: {row[3]}, Check-out: {row[4]}")

    db.close()
#client-checkin module
from datetime import datetime

# Client Check-in Module
def client_check_in():
    db = connect_db()
    cursor = db.cursor()

    client_name = input("Enter client name: ")
    print("Available rooms: ")
    cursor.execute("SELECT room_id, room_type, price FROM rooms WHERE is_occupied = FALSE")
    available_rooms = cursor.fetchall()

    if not available_rooms:
        print("Sorry, no rooms are available.")
        db.close()
        return

    for room in available_rooms:
        print(f"Room ID: {room[0]}, Type: {room[1]}, Price: {room[2]}")

    room_id = int(input("Choose a room ID for check-in: "))
    check_in_date = datetime.now().date()  # Get today's date correctly
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    cursor.execute("UPDATE rooms SET is_occupied = TRUE WHERE room_id = %s", (room_id,))
    cursor.execute("INSERT INTO clients (client_name, room_id, check_in_date, check_out_date) VALUES (%s, %s, %s, %s)",
                   (client_name, room_id, check_in_date, check_out_date))
    db.commit()

    print(f"Check-in successful for {client_name} in Room {room_id}.")
    db.close()

# Client Check-out Module
def client_check_out():
    db = connect_db()
    cursor = db.cursor()

    room_id = int(input("Enter room ID for check-out: "))
    cursor.execute("SELECT client_name FROM clients WHERE room_id = %s", (room_id,))
    client = cursor.fetchone()

    if client:
        cursor.execute("UPDATE rooms SET is_occupied = FALSE WHERE room_id = %s", (room_id,))
        cursor.execute("DELETE FROM clients WHERE room_id = %s", (room_id,))
        db.commit()

        print(f"{client[0]} has successfully checked out of Room {room_id}.")
    else:
        print("No such room ID found or room not occupied.")

    db.close()


# Main menu to interact with the system
def main_menu():
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Client Check-in")
        print("2. Room Service")
        print("3. View Occupied Rooms")
        print("4. Client Check-out")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            client_check_in()
        elif choice == '2':
            room_service()
        elif choice == '3':
            view_occupied_rooms()
        elif choice == '4':
            client_check_out()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the system
if __name__ == "__main__":
    main_menu()
