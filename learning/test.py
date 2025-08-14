import tkinter as tk
import json,csv,smtplib,email
from tkinter import messagebox



data_file = "students_details.json"
exerciese = ['Basics','Sting Operations','Input/Output','Fromatting','Conditional','List','Data Structure','Set','Dictionary','Loop','Function','File Handling','Exception Handling','OOP','Project_1','Project_2']
initial_data = {
    "Name": [],
    "Email Address": [],
    "Progress%": [],
    "Pending Exercise": [],
    "Completed Exercise": []
}



def load_json():
    with open(data_file,'r') as file:
        data = json.load(file)
        return data
    
def display_students_details():
    student_details = load_json()
    
    if not student_details:
        return
    
    window = tk.Tk()
    window.title("Progress Tracker")
    window.geometry("800x600")

    # heading_button = tk.Button(window, text="Student Names", font=("Helvetica", 16, "bold",), bg="red", relief="flat",fg='blue')
    # heading_button.grid(row=0, column=0, pady=10)

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

        name_window.mainloop()
    
    enroll_button = tk.Button(window,text="Enroll Student",command=enroll)
    enroll_button.grid(row=0,column=0,padx=10,pady=10)


    edit_button = tk.Button(window,text="Edit Student")
    remove_button = tk.Button(window,text="Remove Student")
    check_button = tk.Button(window,text="Check Exercise")
    report_button = tk.Button(window,text="Send Report")
    csv_button = tk.Button(window,text="Import from CSV")
    
    edit_button.grid(row=0,column=1,padx=10)
    remove_button.grid(row=0,column=2,padx=10)
    check_button.grid(row=0,column=3,padx=10)
    report_button.grid(row=0,column=4,padx=10)
    csv_button.grid(row=0,column=5,padx=10)



    name_label =tk.Label(window,text="Name")
    name_label.grid(row=1,column=0)

    for name_index,name in enumerate(student_details['Name']): #enumerate() function is used to get both the index and the value of each element in a iterable./helps to track index
        name_value = tk.Label(window,text=name)
        name_value.grid(row=name_index+2,column=0,padx=10)


    email_label = tk.Label(window,text="Email Address")
    email_label.grid(row=1,column=2,padx=10)

    for email_index, email in enumerate(student_details['Email Address']):
        email_value = tk.Label(window,text=email)
        email_value.grid(row=email_index+2,column=2,padx=10)


    progress_label = tk.Label(window,text="Progress(%)")
    progress_label.grid(row=1,column=3,padx=10)

    progress_value = tk.Label(window,text=int("2"))
    progress_value.grid(row=2,column=3,padx=10)   

    pending_exercise_label = tk.Label(window,text="Pending Exercise")
    pending_exercise_label.grid(row=1,column=4,padx=30)

    pending_exercise_value = tk.Label(window,text="")
    pending_exercise_value.grid(row=2,column=4,padx=30)


    completed_exercise_label = tk.Label(window,text="Completed Exercise")
    completed_exercise_label.grid(row=1,column=5,padx=30)

    completed_exercise_value = tk.Label(window,text="")
    completed_exercise_value.grid(row=2,column=5,padx=30)


    
    window.mainloop()


display_students_details()


































# headers = ["SN","Name","Email Address","Progress%","Pending Exercise","Completed Exercise"]
# initial_data = {
#     "Name": [],
#     "Email Address": [],
#     "Progress%": [],
#     "Pending Exercise": [exerciese],
#     "Completed Exercise": []
# }


# with open(data_file,'w') as json_file:
#     json.dump(initial_data,json_file)

# with open(data_file,'r') as file:
#     data = json.load(file)

# data['Name'].append("alishan")


# with open(data_file,'w') as file:
#     json.dump(data,file)
