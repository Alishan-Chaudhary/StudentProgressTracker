import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview without Listbox")

tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# tree.insert("", "end", values=("Alice", 30))
# tree.insert("", "end", values=("Bob", 25))

tree.pack()

root.mainloop()
