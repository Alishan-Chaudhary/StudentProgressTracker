import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Example JSON data (you'd load it from a file in real use)
students_json = '''
[
    {"name": "John Doe", "email": "john@example.com", "progress": "85%", "completed_exercises": 12},
    {"name": "Jane Smith", "email": "jane@example.com", "progress": "90%", "completed_exercises": 15}
]
'''

# Load JSON data
students_data = json.loads(students_json)

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        
        # Listbox to display students
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.listbox.pack(pady=20)
        
        # Buttons to edit and delete
        self.edit_button = tk.Button(root, text="Edit", command=self.edit_student)
        self.edit_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_student)
        self.delete_button.pack(side=tk.LEFT)
        
        self.load_students()
        
    def load_students(self):
        """Load students into the listbox"""
        for student in students_data:
            display_text = f"{student['name']} ({student['email']})"
            self.listbox.insert(tk.END, display_text)
    
    def edit_student(self):
        """Edit selected student's details"""
        try:
            selected_index = self.listbox.curselection()[0]
            selected_student = students_data[selected_index]
            
            # Prompt for new details
            new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=selected_student['name'])
            new_email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=selected_student['email'])
            new_progress = simpledialog.askstring("Edit Progress", "Enter new progress:", initialvalue=selected_student['progress'])
            new_completed_exercises = simpledialog.askinteger("Edit Exercises", "Enter new completed exercises:", initialvalue=selected_student['completed_exercises'])
            
            # Update student data
            selected_student['name'] = new_name
            selected_student['email'] = new_email
            selected_student['progress'] = new_progress
            selected_student['completed_exercises'] = new_completed_exercises
            
            # Refresh the listbox
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, f"{new_name} ({new_email})")
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a student to edit.")
    
    def delete_student(self):
        """Delete selected student's details"""
        try:
            selected_index = self.listbox.curselection()[0]
            confirm = messagebox.askyesno("Delete Student", "Are you sure you want to delete this student?")
            if confirm:
                self.listbox.delete(selected_index)
                del students_data[selected_index]
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a student to delete.")

# Set up Tkinter window
root = tk.Tk()
app = StudentApp(root)
root.mainloop()
