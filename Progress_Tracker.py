import tkinter as tk
import json,csv,smtplib,email
window = tk.Tk()
window.title("Progress Tracker")
window.geometry("800x600")

data_file = "students.json"
exerciese = ['Basics','Sting Operations','Input/Output','Fromatting','Conditional','List','Data Structure','Set','Dictionary','Loop','Function','File Handling','Exception Handling','OOP','Project_1','Project_2']

def say_hello():
    print("hello!")


button = tk.Button(window,text="Enroll Student")
button.pack()
button = tk.Button(window,text="Edit Student")
button.pack()

print('hello')

window.mainloop()