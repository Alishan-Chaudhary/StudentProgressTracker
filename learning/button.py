import tkinter as tk
import json

window = tk.Tk()
window.title("button use")
window.geometry("300x200")


data_file = "students_details.json"

initial_data = {
    "Name": [],
    "Email Address": [],
    "Progress%": [],
    "Pending Exercise": [],
    "Completed Exercise": []
}



def add():
    with open(data_file,'w') as json_file:
        json.dump(initial_data,json_file)

    with open(data_file,'r') as file:
       data = json.load(file)

    data['Name'].append("alishan")


    with open(data_file,'w') as file:
        json.dump(data,file)

# def add_details():
#      with open(data_file,'r') as file:
#        data = json.load(file)

#      data['Name'].append(name)

        

def enroll():
 
    name_window = tk.Tk()
    name_window.title("name")
    name_window.geometry("300x300")
    name = tk.Entry(name_window)
    name.pack()

    def add_name():
        with open(data_file,'r') as file:
            data = json.load(file)

        data['Name'].append(name.get())

        with open(data_file,'w') as file:
            json.dump(data,file)

    ok_button = tk.Button(name_window,text="Ok",command=add_name)
    ok_button.pack()

button = tk.Button(window,text="Enroll Students",command=enroll)
button.pack()

window.mainloop()