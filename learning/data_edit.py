import tkinter as tk

def third_page():
    third_window = tk.Toplevel()
    third_window.title("Third Window")
    third_window.geometry("200x200")

    label = tk.Label(third_window, text="This is the third window")
    label.pack()

    button = tk.Button(third_window, text="Finish", command=third_window.destroy)
    button.pack()

def second_page(current_window):
    current_window.destroy()  # Close previous window

    second_window = tk.Toplevel()
    second_window.title("Second Window")
    second_window.geometry("200x200")

    label = tk.Label(second_window, text="This is the second window")
    label.pack()

    button = tk.Button(second_window, text="Next", command=lambda: third_page_and_close(second_window))
    button.pack()

def third_page_and_close(current_window):
    current_window.destroy()
    third_page()

def first_page():
    first_window = tk.Toplevel()
    first_window.title("First Window")
    first_window.geometry("200x200")

    label = tk.Label(first_window, text="This is the first window")
    label.pack()

    button = tk.Button(first_window, text="Next", command=lambda: second_page(first_window))
    button.pack()

# Main root window
root = tk.Tk()
root.title("Main Window")
root.geometry("800x800")

tk.Label(root, text="Main Window").pack()
tk.Button(root, text="Start", command=first_page).pack()

root.mainloop()
