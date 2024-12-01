from tkinter import *
from GenerateNewCode import random_id
from DataBase import TicketDetails
from DataBase import EventDetails
from DataBase import BookTicket
from Message import show_message
def Book():
    
    ticket_ids = TicketDetails()[1]
    event_names_list = EventDetails()[0]
    
    top1 = Tk()
    top1.geometry('300x280')
    top1.title('Book ticket')
    
    customer_name = StringVar(top1)
    ticket_id = StringVar(top1)
    event_name = StringVar(top1)
    
    event_name.set('Select event')
    
    while True:
        new_ticket_id = random_id()
        if new_ticket_id not in ticket_ids:
            ticket_id.set(new_ticket_id)
            break
        continue
    
    def BookNow():
        if len(customer_name.get())<5:
            show_message('Error', 'Enter valid details')
            return
        booking_status = BookTicket(customer_name.get(), ticket_id.get(), event_name.get())
        if booking_status == 'Success':
            show_message('Success', 'booking successful')
            return
        else:
            show_message('Error', booking_status)
    
    Label(top1, text='Enter details', font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    
    Label(top1, text='Name', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=customer_name).grid(row=1, column=1)
    
    Label(top1, text='Ticket Id', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=ticket_id, state='disabled').grid(row=2, column=1)
    
    Label(top1, text='Event', font=('Arial', 12)).grid(row=3, column=0, padx=10, sticky='w', pady=10)
    OptionMenu(top1, event_name, *event_names_list).grid(row=3, column=1)
    
    Button(top1, text='Confirm', bg='green', fg='white', font=('Arial', 17), width=9, command=lambda:BookNow()).grid(row=4, column=1, pady=10)
    
    top1.mainloop()
