from tkinter import *
from GenerateNewCode import random_id
from DataBase import EventDetails
from DataBase import CreateNewEvent
from Message import show_message
from tkcalendar import DateEntry
from datetime import date
def CreateEvent():
    
    event_ids = EventDetails()[1]
    
    top2 = Tk()
    top2.geometry('300x350')
    top2.title('Create new Event')
    
    event_name = StringVar(top2)
    event_id = StringVar(top2)
    event_date = StringVar(top2)
    event_date.set(date.today())
    event_time = StringVar(top2)
    event_duration = StringVar(top2)
    
    while True:
        new_event_id = random_id()
        if new_event_id not in event_ids:
            event_id.set(new_event_id)
            break
        continue
    
    def CreateNow():
        if len(event_name.get())<5:
            show_message('Error', 'Enter valid details')
            return
        event_status = CreateNewEvent(event_name.get(), event_id.get(), event_date.get(), event_time.get(), event_duration.get())
        if event_status == 'Success':
            show_message('Success', 'Event created successfully')
            return
        else:
            show_message('Error', event_status)
    
    Label(top2, text='Enter details', font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    
    Label(top2, text='Event Name', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_name).grid(row=1, column=1)
    
    Label(top2, text='Event Id', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_id, state='disabled').grid(row=2, column=1)
    
    Label(top2, text='Event Date', font=('Arial', 12)).grid(row=3, column=0, padx=10, sticky='w', pady=10)
    DateEntry(top2, selectmode='day', year=2023, month=1, day=25, textvariable=event_date).grid(row=3, column=1)
    
    Label(top2, text='Event Time(24hrs)', font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_time).grid(row=4, column=1)
    
    Label(top2, text='Event Duration', font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_duration).grid(row=5, column=1)
    
    Button(top2, text='Submit', bg='green', fg='white', font=('Arial', 17), width=9, command=lambda:CreateNow()).grid(row=6, column=0, pady=10, columnspan=2)
    
    top2.mainloop()