import tkinter as tk
import json


data_file = "students_details.json"
with open(data_file, "r") as file:
    data = json.load(file)

# Create the main Tkinter window
root = tk.Tk()
root.title("Name List")

# Create a Listbox widget
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(padx=20, pady=20)

# Insert only the names into the Listbox
for name in data["Name"]:
    listbox.insert(tk.END, name)

# Run the Tkinter main loop
root.mainloop()
