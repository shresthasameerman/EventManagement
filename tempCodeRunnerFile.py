from tkinter import *

from Book import Book 
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket

top = Tk()
top.geometry('415x450')
top.title('Event Management')

Label(
    text="Event Management System", 
    bg="purple", 
    fg="white", 
    font=("Arial", 18), 
    width=30, 
    height=2
).grid(row=0, column=0, columnspan=2, pady=(10, 20))

Button(top, text='Book Ticket', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda: Book()).grid(row=1, column=0, padx=25, pady=30)
Button(top, text='Create Event', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda:CreateEvent()).grid(row=1, column=1)
Button(top, text='View Tickets', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda:ViewTickets()).grid(row=2, pady=20, column=0)
Button(top, text='View Events', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda:ViewEvents()).grid(row=2, column=1)
Button(top, text='Cancel Ticket', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda: CancelTicket()).grid(row=3, pady=25, column=0)
Button(top, text='Quit App', bg='red', fg='white', width=12, font=('Poppins', 18), command=lambda: top.destroy()).grid(row=3, column=1)

top.mainloop()