from tkinter import *
from DataBase import TicketDetails
from DataBase import DeleteTicket
from Message import show_message
def CancelTicket():
    top3 = Tk()
    top3.geometry('790x300')
    top3.title('Cancel Tickets')
    
    Label(top3, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=0, pady=10)
    Label(top3, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=1, pady=10)
    Label(top3, text='Event Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=2, pady=10)
    Label(top3, text='Event Date', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=3, pady=10)
    
    def delete_rows(ticket_id):
        delete_status = DeleteTicket(ticket_id)
        if delete_status == 'Success':
            show_message('Success', 'Ticket deleted successfully')
            return
        else:
            show_message('Error', delete_status)
            return
    
    for i in range(len(TicketDetails()[7])):
        Label(top3, text=TicketDetails()[7][i][0], borderwidth=1, relief="solid", width=20).grid(row=i+1,  column=0)
        Label(top3, text=TicketDetails()[7][i][1], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=1)
        Label(top3, text=TicketDetails()[7][i][2], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=2)
        Label(top3, text=TicketDetails()[7][i][4], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=3)
        Button(top3, text='Delete', command=lambda current_id=TicketDetails()[7][i][1]: delete_rows(current_id)).grid(row=i+1, column=4)
    top3.mainloop()