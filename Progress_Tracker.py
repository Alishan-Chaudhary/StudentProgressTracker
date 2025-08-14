import tkinter as tk
import json,csv,smtplib,email
from tkinter import messagebox


window = tk.Tk()
window.title("Progress Tracker")
window.geometry("800x600")

data_file = "students_details.json"
exerciese = ['Basics','Sting Operations','Input/Output','Fromatting','Conditional','List','Data Structure','Set','Dictionary','Loop','Function','File Handling','Exception Handling','OOP','Project_1','Project_2']

button1 = tk.Button(window,text="Enroll Student")
button2= tk.Button(window,text="Edit Student")
button3 = tk.Button(window,text="Remove Student")
button4 = tk.Button(window,text="Check Exercise")
button5 = tk.Button(window,text="Send Report")
button6 = tk.Button(window,text="Import from CSV")
button1.grid(row=0,column=0,padx=10,pady=10)
button2.grid(row=0,column=1,padx=10)
button3.grid(row=0,column=2,padx=10)
button4.grid(row=0,column=3,padx=10)
button5.grid(row=0,column=4,padx=10)
button6.grid(row=0,column=5,padx=10)

headers = {
    "Name": [],
    "Email Address": [],
    "Progress%": [],
    "Pending Exercise": [exerciese],
    "Completed Exercise": []
}
with open(data_file,'w') as json_file:
    json.dump(headers,json_file)

def load_data():
    try:
        with open(data_file,'r') as f:
            data = json.load(f)
            if isinstance(data,list):
                return data
            else:
                return[]
            
    except(FileNotFoundError,json.JSONDecodeError):
        return[]
    
def save_data(data):
    with open(data_file,'w') as f:
        json.dump(data,f)

# def add_students():
#     name = entry_name.get()
#     email = entry_email.get()

#     if not (name and email):
#         messagebox.showerror("erro")
#         return
    

#     studetn = {
#         "Mame" = name,
#         "Email Address" = email
#     }
window.mainloop()
