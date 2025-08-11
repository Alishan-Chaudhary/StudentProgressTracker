import tkinter as tk
window = tk.Tk() # creates the main application window
window.title("My first App") # .title give the title for the window
window.geometry("400x400") #determines the size of the window

# Label - Display text
label = tk.Label(window, text="hello world")
label.pack(side="right")

# Button - Clickable action
def say_hello():
    print("hello!")

button = tk.Button(window,text='click me', command=say_hello)
button.pack()

# Entry - single-line text input
entry = tk.Entry(window) # used to take the input
entry.pack()
# entry.grid(row=0,column=1)

def get_text(): # writting a function to print the input text
    print(entry.get())

button = tk.Button(window, text="Click This to print what you write", command=get_text)
button.pack()

# Text - Multi-line input
text = tk.Text(window, height=5, width= 30) # this line meas 5 lines tall and 30 characters wide or 1 line wiil be 30 character wide
text.pack()

# Checkbutton - Checkbox(True/False)
var = tk.BooleanVar()
chcekbox = tk.Checkbutton(window,text="Tick", variable=var)
chcekbox.pack()

def show_status():
    print(var.get())

button= tk.Button(window, text='check box',command=show_status)
button.pack(pady=10)





window.mainloop()
