from tkinter import *
from tkinter import ttk

from utils.fake_database import db

def create_aggreements_listing(master, on_select, set_insert_method):
  persons_list = db.read_aggrement()

  table = ttk.Treeview(columns=('id', 'person', 'type', 'status', 'number', 'data_open', 'data_clouse'), show='headings', master=master)
  table.pack(fill=BOTH, expand=1)

  set_insert_method(table.insert)
  
  table.heading('id', text='ID договора')
  table.heading('person', text='Клиент')
  table.heading('type', text='Тип договора')
  table.heading('status', text='Статус')
  table.heading('number', text='Номер договора')
  table.heading('data_open', text='Дата открытия')
  table.heading('data_clouse', text='Дата закрытия')

  for _, value in persons_list.items():
    table.insert('', END, values=(value['id'], value['person'], value['type'], value['status'], value['number'], value['data_open'], value['data_clouse']))

  def on_row_click(event):
    for selected_item in table.selection():
        item = table.item(selected_item)
        data = item["values"]
        on_select(data, lambda : table.delete(selected_item))

  table.bind("<<TreeviewSelect>>", on_row_click)
  