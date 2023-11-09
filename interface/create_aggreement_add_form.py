from tkinter import *
from tkinter import ttk
from utils.fake_database import db
from utils.list_formatters import *

from models.agreement import Agreement

def create_aggreement_add_form(insert_aggreement):
  aggreement_add_form_interface = Tk()

  types_list = format_types(db.read_type())
  statuses_list = format_statuses(db.read_status())
  persons_list = format_person(db.read_person())

  person_label = ttk.Label(text='Клиент', master=aggreement_add_form_interface)
  person_label.pack(anchor=NW, padx=5, pady=5)
  person_value = StringVar(aggreement_add_form_interface)
  person_value.set('Выберите клиента')
  question_menu = OptionMenu(aggreement_add_form_interface, person_value, *list(persons_list.keys())) 
  question_menu.pack(fill=BOTH) 

  type_label = ttk.Label(text='Тип договора', master=aggreement_add_form_interface)
  type_label.pack(anchor=NW, padx=5, pady=5)
  type_value = StringVar(aggreement_add_form_interface)
  type_value.set('Выберите тип')
  question_menu = OptionMenu(aggreement_add_form_interface, type_value, *list(types_list.keys())) 
  question_menu.pack(fill=BOTH) 

  status_label = ttk.Label(text='Стутус договора', master=aggreement_add_form_interface)
  status_label.pack(anchor=NW, padx=5, pady=5)
  status_value = StringVar(aggreement_add_form_interface)
  status_value.set('Выберите статус')
  question_menu = OptionMenu(aggreement_add_form_interface, status_value, *list(statuses_list.keys())) 
  question_menu.pack(fill=BOTH) 

  number = ttk.Entry(master=aggreement_add_form_interface)
  number_label = ttk.Label(text='Номер договора', master=aggreement_add_form_interface)
  number_label.pack(anchor=NW, padx=5, pady=5)
  number.pack(fill=BOTH)

  data_open = ttk.Entry(master=aggreement_add_form_interface)
  data_open_label = ttk.Label(text='Дата открытия', master=aggreement_add_form_interface)
  data_open_label.pack(anchor=NW, padx=5, pady=5)
  data_open.pack(fill=BOTH)

  data_clouse = ttk.Entry(master=aggreement_add_form_interface)
  data_clouse_label = ttk.Label(text='Дата закрытия', master=aggreement_add_form_interface)
  data_clouse_label.pack(anchor=NW, padx=5, pady=5)
  data_clouse.pack(fill=BOTH)

  # СОЗДАНИЕ ДОГОВОРА
  def create_aggreement():
    aggreement = Agreement(
      persons_list[int(person_value.get())],
      types_list[type_value.get()],
      statuses_list[status_value.get()],
      number.get(),
      data_open.get(),
      data_clouse.get()
    ).get_data()
    db.write_aggrement(aggreement)
    insert_aggreement(aggreement['id'])

  create_person_button = Button(text='Создать', master=aggreement_add_form_interface, command=create_aggreement)
  create_person_button.pack(fill=BOTH, padx=5, pady=5)

  aggreement_add_form_interface.geometry('300x600')
  aggreement_add_form_interface.title('Создать договор')