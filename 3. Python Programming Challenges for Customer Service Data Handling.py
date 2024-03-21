# Objective:
# This assignment is designed to test and enhance your Python programming 
# skills, focusing on real-world applications in customer service data 
# management. You will practice correcting code, organizing customer data, 
# and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating 
# a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

#     Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#     Implement functions to:
#         Open a new service ticket.
#         Update the status of an existing ticket.
#         Display all tickets or filter by status.
#     Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


#create a new ticket
def createTicket(customer, issue):
    global service_tickets
    # new ticket key number = service_tickets[-1] + 1
    #print(f"creating new ticket for {customer} for issue '{issue}'")
    latest_ticket = list(service_tickets)[-1].removeprefix("Ticket")
    newTicketNum = "Ticket" + str((int(latest_ticket)+1)).zfill(3)

    service_tickets[newTicketNum] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print("\nYour new ticket has been added!")
    print("Now your list of tickets looks like...\n")
    displayTickets()

    

#update the status of an existing ticket
def updateStatus(name):
    global service_tickets
    found = False
    for ticket, info in service_tickets.items():
        for keys in info:
            if keys == "Customer" and info[keys].lower() == name and service_tickets[ticket]["Status"] == "open":
                service_tickets[ticket]["Status"] = "closed"
                print(f"\nOk {name}, we succesfully updated your ticket status from open to closed!\n")
                found = True
                displayTickets()
                
            elif keys == "Customer" and info[keys].lower() == name and service_tickets[ticket]["Status"] == "closed":
                service_tickets[ticket]["Status"] = "open"
                print(f"\nOk {name}, we succesfully updated your ticket status from closed to open!\n")
                found = True
                displayTickets()
    if found == False:
        print("\nSorry, couldn't find a ticket under that name")
    else:
        pass
        
                


    



#display all tickets, or display tickets of either 'open' or 'closed' status.
def displayTickets(filter="no"):
    for ticket, info in service_tickets.items():
        print(f"{ticket}")
        for key in info:
            print(f" -{key}, {info[key]}")

    pass

while True:
    print("\nWelcome to technical support. What would you like to do?")
    command = input("Please select an option from the list: open a ticket, update ticket status, display tickets, quit\n").strip().lower()
    
    if command == "open a ticket":
        print("Ok lets open a new ticket!\n")

        name=input("What's your name?").strip()
        issue=input("\nWhat title would you like to give the issue?").strip()

        createTicket(name, issue)
        
    
    elif command == "update ticket status":
        print("\nOk lets update the status of your ticket!")
        name = input("what's your name?").strip().lower()
        
        updateStatus(name)
        
    
    elif command == "display tickets":
        displayTickets()
        

    elif command == "quit":
        print("\nOk, thanks for stopping by!")
        

    else:
        print("\nAn error occurred! Please make sure you select a valid list option")
