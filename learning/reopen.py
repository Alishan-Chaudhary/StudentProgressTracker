import tkinter as tk

Window = tk.Tk()
Window.title("reopen")
Window.geometry("800x800")

tk.Label(Window,text="main window")

def mulit_window():
    def third_page():
        third_window = tk.Tk()
        third_window.title("fsecond")
        third_window.geometry("200x200")

        label = tk.Label(third_window,text="third window")
        label.pack()
        
        button = tk.Button(third_window,text="ok")
        button.pack()
        third_window.mainloop()

        
        def second_Page():
            # first_window.destroy()
        
            second_window = tk.Tk()
            second_window.title("fsecond")
            second_window.geometry("200x200")
        

            label = tk.Label(second_window,text="second window")
            label.pack()
        
            button = tk.Button(second_window,text="ok",command=third_page)
            button.pack()
            second_window.mainloop()


        first_window = tk.Tk()
        first_window.title("first")
        first_window.geometry("200x200")
        button = tk.Button(first_window,text="ok",command=second_Page)
        button.pack()
        first_window.mainloop()


button = tk.Button(Window,text="first_window",command=mulit_window)
button.pack()
Window.mainloop()

  

