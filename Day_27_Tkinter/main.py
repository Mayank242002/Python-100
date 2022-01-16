from itertools import count
from pydoc import text
from tkinter import *

def miles_to_km():
    miles=input_miles.get()
    
    total_km=int(miles)*1.609
    print(miles)
    output_km.config(text=total_km)


window=Tk()
window.title("Mile to km Converter")
window.minsize(width=500, height=300)
window.config(padx=30,pady=30)


input_miles=Entry(width=30)
input_miles.grid(column=1,row=0)


mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)
mile_label.config(padx=20,pady=20)

is_equal=Label(text="is equal to")
is_equal.grid(column=0,row=1)
is_equal.config(padx=20,pady=20)

output_km=Label(text=0)
output_km.grid(column=1,row=1)
output_km.config(padx=20,pady=20)

km=Label(text="Km")
km.grid(column=2,row=1)
km.config(padx=20,pady=20)

calc_button=Button(window,text="calculate",command=miles_to_km)
calc_button.grid(column=1,row=2)


window.mainloop()