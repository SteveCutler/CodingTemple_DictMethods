# Objective:
# The aim of this assignment is to deepen your knowledge and practical 
# skills in handling complex data structures using Python. You will work 
# on real-world inspired tasks that require advanced manipulation of 
# dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

#     Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
#     Implement functions to:
#         Book a room (mark as booked and assign to a customer).
#         Check-out a customer (mark room as available and remove customer name).
#         Display the status of all rooms.

# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

#book a room: mark as booked and assign customer name
def bookRoom(number, name):
    global hotel_rooms
    print(f"\n booking room number {number} under name '{name}' now...")
    try:
        availability = hotel_rooms[number]["status"]
    except KeyError:
        print("\nThat room number doesn't exist! Make sure you choose a real room to book.\n")
    except:
        print("\nAn error occured in your booking. Try again!\n")
    else:
        if availability == "available":
            print(f"\nRoom {number} is available! Let's book it for you...")
            hotel_rooms[number]["status"] = "booked"
            hotel_rooms[number]["customer"] = name
            print("Booking succesful!\n")
        else:
            print(f"\nRoom {number} isn't available. Sorry! Try another room..\n")


#check out a customer: mark as available and remove customer name
def checkOut(number):
    global hotel_rooms
    #check if room is booked, if not print an error, if it is mark as available and remove name
    try:
        availability = hotel_rooms[number]["status"]
    except KeyError:
        print("\nThat room number doesn't exist! Make sure you choose a real room to book.\n")
    except:
        print("\nAn error occured in your booking. Try again!\n")
    else:
        if availability != "available":
            print(f"\nOk let's check you out of room {number}...")
            hotel_rooms[number]["status"] = "available"
            hotel_rooms[number]["customer"] = ""
            print("Check out succesful!\n")
        else:
            print(f"\nRoom {number} isn't booked. Sorry! You must be in another room..\n")


#display the status of all rooms - loop
def displayRooms():
    #loop through and print out in user friendly way
    print(f"\n Displaying rooms now...")
    for room, info in hotel_rooms.items():
        print(f"Room {room}:")
        for key in info:
            print(f" -{key}: {info[key]}")





#Functional While loop
while True:
    action = input("\nWhat action would like to take? (Please choose one of the following: book a room, check out, display rooms, quit)\n").strip()
    if action.lower() == "book a room":
        print("\nOk lets book a room...")
        name = input("What name would you like to make the booking under?\n").strip()
        try:
            number = int(input("What room would you like to book?\n").strip())
        except ValueError:
            print("\nAn error occured! Make sure you enter a valid room number. (Please use an integer)")
        else:
            print(f"\nGreat you want to book room number {number} under the name '{name}'")
            print("Let's make that booking now...\n")
            numstr = str(number)
            bookRoom(numstr, name)
    elif action.lower() == "check out":
        print("\nGreat, you'd like to check out...")
        try:
            number = int(input("What room number would you like to check out of?\n").strip())
        except ValueError:
            print("\nAn error occured! Make sure you enter a valid room number. (please you an integer)")
        else:
            print(f"\nGreat! You'd like to check out of room number {number}...")
            print("Lets check you out of that room now...")
            numstr = str(number)
            checkOut(numstr)
        
    elif action.lower() == "display rooms":
        print("Ok, lets take a look at the status of our rooms...")
        displayRooms()

    elif action.lower() == "quit":
        print("Thanks for visiting the hotel!")
        break

    else:
        print("\nAn error occured! Make sure you make a valid choice from the list!")


# Task 2: E-commerce Product Search Feature
# Put your data handling and string manipulation skills to the test by 
# creating a product search feature for an e-commerce platform.

# Problem Statement:
# Create a system that:

#     Holds a dictionary of products where each product has attributes like name, category, and price.
#     Implement a search function that allows searching for products by name, 
# returning a list of matching products (case-insensitive search).
#     Handle cases where no matches are found.

# Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}


#Implement a search function that allows searching for products by name, 
def searchProduct(product):

    productsMatch = []
    for item in products.values():
        for key, value in item.items():
            #print(f"{key}, {value}")
            if key == "name":
                if value.lower() == product:
                    productsMatch.append(item)
                else:
                    continue
            else:
                continue

    print(f"found: {productsMatch}")


searchProduct("shirt")
