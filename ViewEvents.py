from tkinter import *
from DataBase import EventDetails
from DataBase import TicketDetails

def ViewEvents():
    
    event_details = EventDetails()[5]
    top4 = Tk()
    top4.geometry('550x400')
    top4.title('View tickets')
        
    Label(top4, text="Event Name").grid(row=0, column=0, padx=10, pady=10)
    Label(top4, text="Event ID").grid(row=0, column=1, padx=10)
    Label(top4, text="Event Date").grid(row=0, column=2, padx=10)
    Label(top4, text="Event Time(24 hrs)").grid(row=0, column=3, padx=10)
    Label(top4, text="Event Duration(in hrs)").grid(row=0, column=4, padx=10)
    
    Label(top4, text='------------------'*6).grid(row=1, column=0, columnspan=5)
                
    for i in range(len(event_details)):
        Label(top4, text=event_details[i][0], font=('Arial', 12), width=10).grid(row=i+2, column=0)
        Label(top4, text=event_details[i][1], font=('Arial', 12), width=10).grid(row=i+2, column=1)
        Label(top4, text=event_details[i][2], font=('Arial', 12), width=10).grid(row=i+2, column=2)
        Label(top4, text=event_details[i][3], font=('Arial', 12), width=10).grid(row=i+2, column=3)
        Label(top4, text=event_details[i][4], font=('Arial', 12), width=10).grid(row=i+2, column=4)
    
    top4.mainloop()