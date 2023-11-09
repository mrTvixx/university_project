from tkinter import *
from tkinter import ttk
from utils.fake_database import db

def create_person_listing():
  person_create_interface = Tk()

  persons_list = db.read_person()

  table = ttk.Treeview(columns=('inn', 'type', 'shifer', 'data'), show='headings', master=person_create_interface)
  table.pack(fill=BOTH, expand=1)
  
  table.heading('inn', text='ИНН')
  table.heading('type', text='Тип клиента')
  table.heading('shifer', text='Шифр')
  table.heading('data', text='Дата регистрации')

  for _, value in persons_list.items():
    table.insert('', END, values=(value['inn'], value['type'], value['shifer'], value['data']))

  person_create_interface.title('Клиенты')