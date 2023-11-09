from tkinter import *
from tkinter import ttk
from utils.fake_database import db

def create_types_listing():
  types_listing_interface = Tk()

  typess_list = db.read_type()

  table = ttk.Treeview(columns=('name'), show='headings', master=types_listing_interface)
  table.pack(fill=BOTH, expand=1)
  
  table.heading('name', text='Тип договора')

  for _, value in typess_list.items():
    table.insert('', END, values=value['type'])

  types_listing_interface.title('Типы договора')
  types_listing_interface.geometry('500x300')