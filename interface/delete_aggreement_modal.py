from tkinter import *
from tkinter import ttk
from utils.fake_database import db

def create_delete_aggreement_modal(on_delete):
  delete_form = Tk()

  person_label = ttk.Label(text='Вы уверены?', master=delete_form)
  person_label.pack(anchor=NW, padx=5, pady=5)

  def submit_delete():
    on_delete()
    delete_form.destroy()

  delete_btn = Button(text='Удалить', master=delete_form, command=submit_delete)
  delete_btn.pack(fill=BOTH, padx=5, pady=5)

  cancel_btn = Button(text='Отмена', master=delete_form, command= lambda: delete_form.destroy())
  cancel_btn.pack(fill=BOTH, padx=5, pady=5)


  delete_form.title('Предупреждение')