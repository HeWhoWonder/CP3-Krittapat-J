from currency_converter import CurrencyConverter
import math
from tkinter import *
from tkinter import ttk

currency = CurrencyConverter(fallback_on_missing_rate=True, fallback_on_wrong_date=True)


def get_value():
    fiat1 = from_box.get()
    fiat2 = to_box.get()
    first_date, last_date = currency.bounds[fiat2]
    date_lbl.configure(text=last_date)
    amount = entry_box.get()
    result = math.ceil(currency.convert(amount, fiat1, fiat2))
    result_box.delete(0, 'end')
    result_box.insert(0, result)


def clear():
    from_box.delete(0, END)
    to_box.delete(0, END)
    entry_box.delete(0, END)
    result_box.delete(0, END)


main_page = Tk()
main_page.geometry("400x130")
main_page.title('Currency Converter')

# content1
content1 = Frame(main_page, borderwidth=4, relief="ridge")
content1.grid(column=0, row=0)

# From Combobox
from_lbl = Label(content1, text='From')
from_lbl.grid(column=0, row=0)
from_box = ttk.Combobox(content1, values=list(currency.currencies), width=5)
from_box.grid(column=0, row=1,)

# To Combobox
to_lbl = Label(content1, text='To')
to_lbl.grid(column=0, row=2)
to_box = ttk.Combobox(content1, values=list(currency.currencies), width=5)
to_box.grid(column=0, row=3)

# Entry box
entry_box = Entry(content1)
entry_box.grid(column=1, row=1, padx=7)

# Result box
result_box = Entry(content1)
result_box.grid(column=1, row=3, padx=7)

# Date
date_lbl = Label(content1, text='Latest Update')
date_lbl.grid(column=1, row=4)

# content2
content2 = Frame(main_page)
content2.grid(column=1, row=0)
convert_button = Button(content2, text='convert', command=get_value, width=5)
convert_button.grid(column=0, row=0, padx=15)

clear_button = Button(content2, text='clear', command=clear, width=5)
clear_button.grid(column=0, row=1, padx=15)

main_page.mainloop()