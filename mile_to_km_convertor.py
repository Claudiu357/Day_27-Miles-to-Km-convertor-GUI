from tkinter import *

def transform_to_km():
    miles = int(input_miles.get())
    km_transform = miles * 1.6
    km.config(text=km_transform)

win = Tk()
win.title("Mile convertor")
win.minsize(width=400, height=200)

input_miles = Entry(width=10)
input_miles.place(x=150, y=50)

miles_label = Label(text="Miles")
miles_label.place(x=250,y=50)

is_equal_to = Label(text="is equal to")
is_equal_to.place(x=80, y= 80)

km = Label(text="0")
km.place(x=190,y=80)

km_label = Label(text="Km")
km_label.place(x=250,y=80)

button = Button(text="Calculate", command=transform_to_km)
button.place(x=150, y = 110)



win.mainloop()