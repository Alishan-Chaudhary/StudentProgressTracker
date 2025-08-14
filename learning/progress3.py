import tkinter as tk
from tkinter import ttk
import json


data_file = "students_details.json"

window = tk.Tk()
window.title("Treeview without Listbox")


def enroll():
        name_window = tk.Toplevel()
        name_window.title("name")
        name_window.geometry("300x300")
        text = tk.Label(name_window,text="Enter Student Name")
        text.pack()
        name = tk.Entry(name_window)
        name.pack()
        
        def add_name():
            

            with open(data_file,'r') as file:
                data = json.load(file)
                
            data['Name'].append(name.get())
            
            with open(data_file,'w') as file:
                json.dump(data,file)

            email_window = tk.Toplevel()
            email_window.title("Email")
            email_window.geometry("300x300") 
            email = tk.Entry(email_window) 
            email.pack()
            name_window.destroy()   
            def add_email():
                with open(data_file,"r") as file:
                    data= json.load(file)
                    
                    
                data["Email Address"].append(email.get())

                with open(data_file,'w') as file:
                    json.dump(data,file)
       
            ok_button = tk.Button(email_window,text="Ok",command=add_email)
            ok_button.pack() 
        ok_button = tk.Button(name_window,text="Ok",command=add_name)
        ok_button.pack()

        def add_email():
            # email_window = tk.Toplevel()
            # email_window.title("Email")
            # email_window.geometry("300x300")  

            with open(data_file,"r") as file:
                data= json.load(file)

            data["Email Address"].append(email.get())

            with open(data_file,'w') as file:
                json.dump(data,file)
       
        ok_button = tk.Button(email_window,text="Ok",command=add_email)
        ok_button.pack()

enroll_button = tk.Button(window,text="Enroll Student",command=enroll)
enroll_button.grid(row=0,column=0,padx=10,pady=10)    

def edit():
    new_window = tk.Toplevel()
    new_window.title("Edit Name")
    new_window.geometry("300x300")
    text = tk.Label(new_window,text="Edit Student Name")
    text.pack()
    name = tk.Entry(new_window)
    name.pack()
    

    def edit_name():
        new_window.destroy()

        with open(data_file,'r') as file:
            data = json.load(file)

        # data['Name'].append(name.get())
        
        with open(data_file,'w')as file:
            json.dump(name.get(),file)
        

    ok_button = tk.Button(new_window,text="ok",command=edit_name)
    ok_button.pack()

   

    def edit_email():

        email_window.destroy()



        email = tk.Entry(new_window)
        email.pack()  

        with open(data_file,'r') as file:
            data=json.load(file)

        # data["Email Address"].appendI(email.get())

        with open(data_file,'w') as file:
            json.dump(file)

    email_window = tk.Tk()
    email_window.title("Email")
    email_window.geometry("300x300")

    ok_button = tk.Button(email_window,text="ok",command=edit_email)
    ok_button.pack()
    new_window.mainloop()



edit_button = tk.Button(window,text="Edit Student",command=edit)
edit_button.grid(row=0,column=1,padx=10,pady=10)


data_file
with open(data_file,'r') as file:
    data = json.load(file)


headings = list(data.keys())

max_len = max(len(values) for values in data.values())


for key in data:
    while len(data[key])<max_len:
        data[key].append("")

# tree = ttk.Treeview(window, columns=["Name", "Email Address","Progress","Pending Exercise","Completed Exercise"], show="headings")
# tree.headings("Name", text="Name")
# tree.headings("Email Address", text="Email")
# tree.headings("Progress", text="Progress(%)")
# tree.headings("Pending Exercise", text="Pending Exercise")
# tree.headings("Completed Exercise", text="Completed Exercise")

tree = ttk.Treeview(window,columns=headings,show="headings")
for heading in headings:
    tree.heading(heading,text=heading)
    tree.column(heading,width=150,anchor="center")
    

# for name, email,progress,pending,completed in zip(data["Name"],data["Email Address"],data["Progress%"],data["Pending Exercise"], data["Completed Exercise"]):
#     tree.insert("", "end",values=(name,email,progress,pending,completed) )

for row in zip(*[data[key] for key in headings]):
    tree.insert("","end",values=row)

tree.grid()

window.mainloop()
