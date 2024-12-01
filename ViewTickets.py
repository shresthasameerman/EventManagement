from tkinter import *
from DataBase import EventDetails
from DataBase import TicketDetails

def ViewTickets():
    top4 = Tk()
    top4.geometry('480x400')
    top4.title('View tickets')
    
    event_names_list = EventDetails()[0]
    
    event_name = StringVar(top4)
    
    event_name.set('Select event')
    
    def ShowTickets():
        Label(top4, text="Customer Name").grid(row=3, column=0, padx=10, pady=10)
        Label(top4, text="Ticket ID").grid(row=3, column=1, padx=10, pady=10)
        Label(top4, text="Event Name").grid(row=3, column=2, padx=10, pady=10)
        Label(top4, text="Event Date").grid(row=3, column=3, padx=10, pady=10)
        required_tickets = []
        for i in TicketDetails()[7]:
            if event_name.get() in i:
                required_tickets.append(i)
        for i in range(len(required_tickets)):
            Label(top4, text=required_tickets[i][0], font=('Arial', 12), width=10).grid(row=i+4, column=0)
            Label(top4, text=required_tickets[i][1], font=('Arial', 12), width=10).grid(row=i+4, column=1)
            Label(top4, text=required_tickets[i][2], font=('Arial', 12), width=10).grid(row=i+4, column=2)
            Label(top4, text=required_tickets[i][4], font=('Arial', 12), width=10).grid(row=i+4, column=3)
    
    Label(top4, text='Select Event', font=('Arial', 16)).grid(row=0, column=0, padx=10, sticky='w', pady=10)
    OptionMenu(top4, event_name, *event_names_list).grid(row=0, column=1)
    
    Button(top4, text='Submit', command=ShowTickets, bg='green', fg='white', font=('Arial', 12)).grid(row=2, column=0, columnspan=3)
    
    top4.mainloop()