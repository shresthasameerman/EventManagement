# Event Management System

This is an Event Management System built using Python and Tkinter for a graphical user interface (GUI). The system allows users to create events, view events, book and cancel tickets, and manage event-related tasks. Below is a detailed overview of the files included in this system.

## Features

- **Create Event:** Admins can create events and store event details.
- **Book Ticket:** Users can book tickets for available events.
- **Cancel Ticket:** Users can cancel previously booked tickets.
- **View Events:** Displays a list of all available events.
- **View Tickets:** Allows users to view their booked tickets.

## Requirements

- Python 3.x
- Tkinter (Usually comes pre-installed with Python)
- Any standard Python libraries for database management

## Files Description

### 1. `Book.py`
This file contains the logic for booking tickets for available events. It interacts with the database to check availability and book tickets accordingly.

### 2. `Cancelticket.py`
This file allows users to cancel their booked tickets. It handles removing ticket details from the database.

### 3. `createevent.py`
This script is responsible for creating new events. It allows admins to enter event details such as name, date, and location, and saves these details to the database.

### 4. `database.py`
This file contains the database-related logic, including saving and retrieving event and ticket information. It defines the `TicketDetails` and `EventDetails` classes to handle database interactions.

### 5. `generatenewcode.py`
Generates a new unique code for each ticket booking. This file contains a function to generate random IDs for tickets, ensuring that each ticket has a unique identifier.

### 6. `main.py`
The entry point for the application. This file initializes the Tkinter GUI and integrates all the functionalities like creating events, booking tickets, and viewing events.

### 7. `message.py`
This file contains the function `show_message`, which is used to display pop-up messages to users throughout the application. It informs users of actions like successful bookings or cancellations.

### 8. `tempCodeRunnerfilerunner.py`
A temporary file used for testing or running specific sections of code. This file is not essential for the overall system but may be used for debugging purposes during development.

### 9. `viewEvents.py`
Allows users to view all the available events. It fetches event data from the database and displays it in the GUI.

### 10. `ViewTickets.py`
This file displays the list of tickets booked by the user. It interacts with the database to fetch the user's ticket details and displays them on the GUI.

## Installation

1. Clone or download the repository.
2. Make sure you have Python 3.x installed.
3. Ensure that Tkinter is installed on your system.
4. Run `main.py` to start the Event Management System.

```bash
python main.py
