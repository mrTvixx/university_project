from tkinter import *
from tkinter import ttk

from interface.create_aggreement_add_form import create_aggreement_add_form
from interface.create_aggreements_listing import create_aggreements_listing
from interface.delete_aggreement_modal import create_delete_aggreement_modal

from utils.fake_database import db

def create_aggreement_interface(master):
  # СОЗДАНИЕ ДОГОВОРА
  def set_insert_method(method):
    global insert_to_table 
    insert_to_table = method

  def insert_aggreement(id):
    global insert_to_table
    
    aggreement = db.read_aggrement(id)
    insert_to_table('', END, values=(aggreement['id'], aggreement['person'], aggreement['type'], aggreement['status'], aggreement['number'], aggreement['data_open'], aggreement['data_clouse']))

  create_person_button = Button(text='Создать договор', master=master, command= lambda: create_aggreement_add_form(insert_aggreement))
  create_person_button.pack(anchor=NW, padx=5, pady=5)

  # УДАЛЕНИЕ ДОГОВОРА
  def on_select(value, delete_row):
    global row_delete_method
    global id_for_delete

    id_for_delete = value[0]
    row_delete_method = delete_row

  def delete_aggreement():
    global row_delete_method
    global id_for_delete

    if (row_delete_method and id_for_delete):
      row_delete_method()
      db.delete_aggrement(id_for_delete)

      row_delete_method = None
      id_for_delete = None
 
  delete_btn = Button(text='удалить', master=master, command=lambda: create_delete_aggreement_modal(delete_aggreement))
  delete_btn.pack(anchor=NW, padx=5, pady=5)

  # ТАБЛИЦА
  create_aggreements_listing(master, on_select, set_insert_method)
