import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="miauuu", font=("Arial", 23, "bold"))
my_label.pack()
my_label["text"] = "new text"

#Button
def button_clicked():
    my_label["text"] = input.get()
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry()
input.pack()
window.mainloop()