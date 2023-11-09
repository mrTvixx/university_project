from tkinter import *  
from tkinter import Menu, ttk 

from interface.status_listing import create_status_listing
from interface.types_listing import create_types_listing
from interface.person_listing import create_person_listing
from interface.aggreements import create_aggreement_interface
  
def create_interface():
  window = Tk()
  window.title("Ведения договоров клиентов")

  create_aggreement_interface(window)

  menu = Menu(window)  

  # Пункт меню Клиент
  client = Menu(menu)
  client.add_command(label='Просмотр', command=create_person_listing)
  menu.add_cascade(label='Клиент', menu=client)

  # Пункт меню Статус договора
  agreement_status = Menu(menu)
  agreement_status.add_command(label="Просмотр", command=create_status_listing)
  menu.add_cascade(label='Статус договора', menu=agreement_status)

  # Пункт меню Тип договора
  agreement_type = Menu(menu)
  agreement_type.add_command(label="Просмотр", command=create_types_listing)
  menu.add_cascade(label='Тип договора', menu=agreement_type)

  window.config(menu=menu)  
  window.mainloop()