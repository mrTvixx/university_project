from tkinter import *
from tkinter import ttk
from utils.fake_database import db

def create_status_listing():
  status_listing_interface = Tk()

  statuses_list = db.read_status()

  table = ttk.Treeview(columns=('name'), show='headings', master=status_listing_interface)
  table.pack(fill=BOTH, expand=1)
  
  table.heading('name', text='Статус')

  for _, value in statuses_list.items():
    table.insert('', END, values=value['status'])

  status_listing_interface.title('Статусы договора')
  status_listing_interface.geometry('500x300')